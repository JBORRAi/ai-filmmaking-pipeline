# Sonorisation MMAudio — KIM RUNNER

Source : `MONTAGE KIM RUNNER.mp4` (1 min 40, 24 i/s). Extraits dans `SON/extraits/`, coupés sur les
coupes du montage (détection automatique), 10 s max. Le nom du fichier = son timecode de début :
posez le son généré à ce timecode dans Final Cut.

**Negative prompt commun (à mettre partout) :**
`music, melody, score, singing, speech, dialogue, voice, electronic beeps, cartoon sounds, magic sparkles, low quality, distortion`

Réglages conseillés : durée = durée de l'extrait, CFG ~4.5, 25 steps. Générer, écouter, garder le meilleur.

| # | Fichier | Timecode | Durée | Image | Prompt |
|---|---|---|---|---|---|
| 01 | 01_0m00.00s.mp4 | 0:00.00 | 5.0 s | Kim marche vers nous, foule | busy Manhattan sidewalk ambience, many footsteps on stone, crowd chatter, distant traffic and car horns |
| 02 | 02_0m05.04s.mp4 | 0:05.04 | 7.8 s | Foule qui traverse | dense city crowd walking past, footsteps, coats rustling, traffic passing, distant horns, New York street ambience |
| 03 | 03_0m12.86s.mp4 | 0:12.86 | 7.8 s | Gros plan oreille, marque 속 | muffled city ambience, close intimate breathing, soft wind, distant traffic |
| 04 | 04_0m20.67s.mp4 | 0:20.67 | 2.7 s | La foule sursaute | a woman screaming in the distance, crowd gasping in shock, sudden footsteps stopping |
| 05 | 05_0m23.33s.mp4 | 0:23.33 | 7.8 s | Par-dessus l'épaule, avenue | tense street ambience, murmuring crowd, a powerful sport motorcycle approaching fast, engine roaring |
| 06 | 06_0m31.12s.mp4 | 0:31.12 | 7.8 s | Pano, la moto passe | a sport motorcycle passing at extreme speed very close, loud engine whoosh and doppler, crowd reacting, wind |
| 07 | 07_0m38.92s.mp4 | 0:38.92 | 5.5 s | Kim se retourne vers l'homme à terre | uneasy murmuring crowd, distant traffic, a few footsteps, tense quiet street |
| 08 | 08_0m44.38s.mp4 | 0:44.38 | 7.7 s | Adam au sol | quiet tense street, distant murmuring crowd, heavy breathing close (voix d'Adam = P10_Adam_voix_FINAL.mp3 par-dessus) |
| 09 | 09_0m52.12s.mp4 | 0:52.12 | 5.6 s | Kim écoute | very quiet street, low wind, distant muffled city, heartbeat-like silence |
| 10 | 10_0m57.75s.mp4 | 0:57.75 | 5.6 s | Tempe, le masque s'assemble | precise mechanical clicks, servo motors whirring, metal plates locking into place one by one, a firm final snap, deep power hum rising |
| 11 | 11_1m03.38s.mp4 | 1:03.38 | 6.4 s | Il marche allumé, foule | heavy mechanical reactor spinning up, industrial turbine roar building, heavy footsteps, crowd gasping |
| 12 | 12_1m09.75s.mp4 | 1:09.75 | 9.5 s | Charge : main, manche, yeux | deep nuclear reactor hum rising, heavy industrial turbine, pressurised hiss, metallic resonance, ground rumbling |
| 13 | 13_1m19.25s.mp4 | 1:19.25 | 9.5 s | Basket, les 5 jauges | five heavy mechanical charge-up thumps, each louder and deeper, asphalt cracking, metallic resonance, pressurised hiss |
| 14 | 14_1m28.75s.mp4 | 1:28.75 | 2.0 s | Plongée aérienne | **silence** — ne pas générer : silence total au montage (éventuellement un acouphène très léger) |
| 15 | 15_1m30.75s.mp4 | 1:30.75 | 1.4 s | Ras du sol derrière lui | asphalt grinding and cracking under heavy pressure, deep rumble |
| 16 | 16_1m32.17s.mp4 | 1:32.17 | 4.7 s | Traînée / départ | massive sonic boom, sound barrier double crack, violent pressure blast, asphalt tearing apart |
| 17 | 17_1m36.83s.mp4 | 1:36.83 | 4.0 s | Cratère, poussière | debris and asphalt chunks raining down, dust settling, car alarms in the distance, ringing aftermath |

## À faire à la main au montage (MMAudio ne sait pas le faire)
- La **déflagration sèche puis le silence total** (fin du 13 → 14) : couper net.
- Le **mur du son** (16) : superposer la génération MMAudio et le son natif de `P15c_arrachement_FINAL`.
- Les sons natifs Seedance des plans 11 bis → 15 (dans les `_FINAL` de `FINALCUT/`) peuvent servir de couche.

> La détection de coupes a trouvé 12 coupes ; certaines coupes douces (même rue) ont pu être
> fusionnées. Les extraits > 10 s ont été divisés en parts égales.
