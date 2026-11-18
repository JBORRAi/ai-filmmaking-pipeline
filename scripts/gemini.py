#!/usr/bin/env python3
"""Client Gemini réutilisable : réflexion étendue, reprise et bascule de modèle.

    from gemini import demande
    print(demande("ton prompt"))
    print(demande("compare", image=["controle.png", "genere.png"]))
"""
import os
import pathlib
import sys
import time

RACINE = pathlib.Path(__file__).resolve().parent.parent
# Du plus récent au plus ancien : on bascule si l'un sature (503).
MODELES = ["gemini-3.8-flash", "gemini-3.7-flash", "gemini-3.5-flash"]


def _env():
    f = RACINE / ".env"
    for ligne in f.read_text().splitlines():
        if "=" in ligne and not ligne.startswith("#"):
            k, _, v = ligne.partition("=")
            os.environ.setdefault(k.strip(), v.strip())


_env()

from google import genai
from google.genai import types

_client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])


def demande(prompt, image=None, etendu=True):
    """Interroge Gemini.

    `image` : un chemin, ou une LISTE de chemins. Les images sont envoyées
    dans l'ordre donné — indispensable pour comparer un cadrage de contrôle
    à une image générée.
    """
    contenu = [prompt]
    if image:
        chemins = [image] if isinstance(image, (str, pathlib.Path)) else list(image)
        for c in chemins:
            p = pathlib.Path(c)
            if not p.is_absolute():
                p = RACINE / p
            contenu.append(types.Part.from_bytes(
                data=p.read_bytes(),
                mime_type="image/png" if p.suffix.lower() == ".png" else "image/jpeg",
            ))

    cfg = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="high" if etendu else "low")
    )

    prefere = os.environ.get("GEMINI_MODEL", "").strip()
    ordre = [prefere] + [m for m in MODELES if m != prefere] if prefere else MODELES

    derniere = None
    for modele in ordre:
        for essai in range(3):
            try:
                return _client.models.generate_content(
                    model=modele, contents=contenu, config=cfg
                ).text
            except Exception as err:
                derniere = err
                if "503" in str(err) or "UNAVAILABLE" in str(err):
                    time.sleep(4)  # saturation passagère
                    continue
                break  # autre erreur : on passe au modèle suivant
    raise RuntimeError(f"Tous les modèles ont échoué. Dernière erreur : {derniere}")


if __name__ == "__main__":
    print(demande(" ".join(sys.argv[1:]) or "Dis bonjour en une phrase."))
