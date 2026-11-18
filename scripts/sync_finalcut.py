"""Remplit FINALCUT/ avec les vidéos retenues, converties en Apple ProRes 422 HQ.

Pourquoi : Runway/Seedance exporte en H.264 « High 4:4:4 Predictive » (yuv444p),
profil que le décodeur d'Apple ne lit pas (Finder, QuickTime, Final Cut). ProRes 422 HQ
est natif sur Mac, fluide au montage, et sans perte visible. Les originaux restent dans PLANS/.

    uv run --with imageio-ffmpeg python scripts/sync_finalcut.py
"""
import glob, os, subprocess, imageio_ffmpeg

ff = imageio_ffmpeg.get_ffmpeg_exe()
os.makedirs("MONTAGE/FINALCUT", exist_ok=True)
motifs = ("_FINAL.", "_prolongation.", "_brut.")


def infos(chemin):
    return subprocess.run([ff, "-i", chemin], capture_output=True, text=True).stderr


def a_jour(src, dst):
    """ProRes, plus récent que la source, et avec l'audio si la source en a."""
    if not os.path.exists(dst) or os.path.getmtime(dst) < os.path.getmtime(src):
        return False
    d = infos(dst)
    return "prores" in d.lower() and ("Audio:" in d or "Audio:" not in infos(src))


for src in sorted(glob.glob("PLANS/*/3_RESULTATS/*")):
    nom = os.path.basename(src)
    if not any(m in nom for m in motifs) or not nom.lower().endswith((".mov", ".mp4")):
        continue
    dst = os.path.join("MONTAGE/FINALCUT", os.path.splitext(nom)[0] + ".mov")
    if a_jour(src, dst):
        continue
    # Audio conservé en PCM 48 kHz (le son natif Seedance sert de base au montage)
    r = subprocess.run([ff, "-y", "-i", src, "-c:v", "prores_ks", "-profile:v", "3",
                        "-pix_fmt", "yuv422p10le", "-vendor", "apl0",
                        "-c:a", "pcm_s16le", "-ar", "48000", dst],
                       capture_output=True, text=True)
    print(("OK    " if r.returncode == 0 else "ÉCHEC ") + os.path.basename(dst))
