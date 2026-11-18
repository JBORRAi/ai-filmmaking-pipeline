# Méthode de production de films IA (tirée de KIMKATCHER épisode 1)

Valable pour tout projet, quel que soit le style (réaliste, cartoon, animation).

## Le principe
La plupart des vidéos IA ne se montent pas : les personnages dérivent, les directions s'inversent, la
caméra fait ce qu'elle veut. On traite donc le film comme une **production** : on décide tout ce que le
modèle devinerait (références, caméra, raccords) **avant** de générer, et un agent fait respecter ces décisions.

## Le pipeline en 7 étapes
| # | Étape | Outils (épisode 1) | Qui |
|---|---|---|---|
| 1 | Découpage : valeur de plan, focale, durée | `SEQUENCE.md` | réalisateur |
| 2 | Bible visuelle verrouillée : une référence par état de personnage, décors, lumière | Grok Imagine, GPT Image 2 | réalisateur |
| 3 | Blocking 3D : décor, caméras réelles, timing | Blender via MCP | agent |
| 4 | Prompt généré depuis la scène 3D | `scripts_communs/prompt_depuis_scene.py` | agent |
| 5 | Keyframes : première et dernière image quand un plan change d'état | GPT Image 2 | réalisateur |
| 6 | Vidéo : interpolation entre images validées | Seedance 2.5 (Runway) | agent ou réalisateur |
| 7 | Post-production : son, upscale, montage | Suno, MMAudio, ElevenLabs, Topaz Proteus, Final Cut | réalisateur |

## Les règles qui marchent
1. **Bible d'abord.** La cohérence vient de la réutilisation des références, pas du volume de générations.
2. **La caméra se décide en 3D.** Un prompt ne tient pas une focale ; une caméra Blender, si. Le rendu gris sert
   d'image de contrôle (légender : « les boîtes grises sont des personnes », sinon le modèle en fait des murs).
3. **Plan pilote** : un plan de bout en bout avant tout le reste, pour calibrer le pipeline.
4. **Keyframes** : le modèle vidéo interpole, il n'invente pas. Générer la dernière image depuis les références,
   pas en éditant la première (sinon grain et artefacts cumulés). Une seule édition par image.
5. **Raccords** : règle des 180°, continuité de mouvement, regard amené par le mouvement, raccord dans le geste,
   progression d'échelle.
6. **Visage** : joindre la référence visage dès qu'un visage peut apparaître.
7. **Coûts** : une génération à la fois, accord explicite, solde avant et après dans `COUTS.md`.
8. **Tout consigner** : journal et Git transforment une suite de prompts en production reproductible.

## Repères techniques
- Runway exporte en H.264 4:4:4, illisible par Apple : convertir en ProRes 422 HQ **avec l'audio**
  (`scripts_communs/sync_finalcut.py`).
- Suno : décrire en positif (« beatless »), jamais « no drums » ; tempo et balises avec timecodes dans Paroles.
- Upscale : Proteus (non génératif) pour la cohérence ; exporter en ProRes, jamais en H.264 bas débit.
- Final Cut ne relie pas un clip muet à un fichier qui a du son : remplacer dans la timeline.
