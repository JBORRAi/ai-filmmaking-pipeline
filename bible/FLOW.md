# Le pipeline

Principe directeur : **la mise en scène se décide en 3D, pas dans le prompt.**
Blender sert de storyboard vivant — cadrage, focale, mouvement, timing y sont
décidés et reproductibles. L'IA générative n'intervient qu'ensuite, guidée par
ces rendus, pour habiller ce qui est déjà composé.

## Les cinq étapes

| # | Étape | Outil | Qui |
|---|---|---|---|
| 1 | Direction visuelle, moodboard | Grok Imagine | toi, en manuel → `REFERENCES/` |
| 2 | Blocking 3D : décor, caméras, timing | Blender via MCP | Claude |
| 3 | Critique du rendu | API Gemini (vision) | Claude, automatisé |
| 3bis | **Habillage : blockout → image photoréaliste** | Nano Banana / Gemini image (abonnement) | toi, en manuel |
| 4 | Génération du plan final | Veo / Flow (abonnement Gemini Pro) | toi, en manuel → `renders/` |
| 5 | Assemblage, son, étalonnage | ffmpeg | Claude |

L'étape 3 est la boucle qui fait gagner du temps : elle corrige le cadrage et la
lumière **avant** de dépenser des crédits Veo, qui sont la ressource rare.

## La boucle de travail sur un plan

```
get_scene_info          →  lire l'état réel de la scène
execute_blender_code    →  poser décor, caméra, éclairage (script versionné)
get_viewport_screenshot →  regarder le résultat
scripts/gemini.py       →  critique : cadrage, lumière, lisibilité
                        →  ajuster, recommencer
rendu                   →  image de contrôle pour Veo
```

## L'étape 3bis — l'habillage (ne pas la sauter)

**Un rendu en blocs gris ne peut pas servir d'image de départ à Veo.** Donné tel quel
à un outil d'image→vidéo, il produit des blocs gris qui bougent. Aucun générateur ne
transforme un blockout en photoréalité.

Il faut une étape intermédiaire :

```
Blender (blocs gris)  →  modèle d'image  →  image photoréaliste  →  Veo  →  plan
     cadrage vrai         habillage          image de départ      animation
```

Le modèle d'image reçoit **deux entrées** : le rendu Blender (qui impose le cadrage,
la perspective, la place du sujet, la lumière) et `REFERENCES/perso_kim_face_visage_decouvert.jpg`
(qui impose le visage). Il en sort une image photoréaliste **à la composition imposée**.

C'est cette image, et elle seule, qui part vers Veo.

**Manuel, obligatoirement.** Les modèles d'image de l'API Gemini
(`gemini-3-pro-image`, `nano-banana-pro-preview`, `gemini-3.1-flash-image`) sont
**hors quota sur le palier gratuit** — testé le 2026-09-08, tous en 429. L'accès passe
par l'abonnement Gemini Pro, dans l'application.

## Le rôle exact de Blender

**Blender ne fabrique pas Manhattan. Blender EST la caméra.**

La photoréalité vient de Veo. Blender fournit ce que la génération IA ne sait pas
tenir seule : la géométrie, la focale, le timing et surtout **le vecteur**.

### Ce qu'on y construit
- L'avenue en **blocs gris à l'échelle réelle** : largeur de chaussée, hauteur des
  immeubles, largeur de trottoir. L'échelle est ce qui fait qu'un plan sonne
  new-yorkais plutôt que générique.
- Un **rig caméra à focales réelles** (24 / 35 / 85 mm sur capteur 35 mm).
- Les **trajectoires** : une courbe, une contrainte de suivi, des keyframes.

### Pourquoi c'est indispensable ici
- **Les plans 2-3-4 sont UN SEUL mouvement de caméra**, découpé en trois extraits.
  C'est la seule façon d'obtenir un arc réellement continu — un prompt ne sait pas
  faire ça, il regénère un mouvement différent à chaque plan.
- **Le plan 30** (ras du sol, suivi de la fissure à pleine vitesse) est impossible
  à obtenir par prompt. En 3D c'est une courbe et une contrainte.
- Chaque plan produit une **image de contrôle** (rendu gris, passe de profondeur)
  qui impose à Veo *notre* cadrage au lieu du sien.

### Vérification automatique de la grammaire
Les règles de `RACCORDS.md` deviennent **calculables** :
- **Règle des 180°** : l'axe Kim↔motos est une droite de la scène. Le signe du produit
  vectoriel dit de quel côté est chaque caméra. Une caméra qui franchit l'axe est
  détectée par script, pas par l'œil.
- **Continuité de vecteur** : on extrait le déplacement écran de chaque caméra et on
  détecte deux mouvements opposés collés.

À écrire dans `scripts/verifie_raccords.py`. C'est ce qui transforme la grammaire
d'intention en contrainte vérifiée.

### L'animatique
Les 35 plans en cubes gris, au bon timing, montés bout à bout — **avant tout crédit
dépensé**. C'est là qu'on sent si un raccord accroche.

## Paire d'états = paire de keyframes

**Toute transformation visuelle se fabrique en générant ses deux états en images fixes,
puis en les donnant comme première et dernière keyframe au modèle vidéo.**

Ne jamais demander à un modèle vidéo de *créer* une transformation : il improvise.
Lui demander seulement de *relier* deux états qu'on a validés.

Cela s'applique à toute la transformation de Kim (plans 22 à 28) :

| Plan | Keyframe A | Keyframe B |
|---|---|---|
| 23 | marque éteinte | marque rougeoyante |
| 24 | visage nu | masque déployé |
| 25 | iris normaux | iris rouges |
| 26 | LED éteintes | LED allumées en cascade |
| 27 | bitume intact | bitume craquelé |

Avantage décisif : **le détail exact est peint dans l'image**, où le modèle a le temps
et la référence pour le réussir. Le modèle vidéo n'a plus qu'à interpoler.

**Corollaire sur l'échelle** — constat du 2026-09-08 : un détail fin (l'idéogramme 속)
échoue en plan large, où il ne fait que quelques pixels : le modèle voit « tache
sombre » et improvise une forme. En gros plan, avec la référence, il le reproduit
fidèlement. **Réserver les détails signifiants aux gros plans**, et n'en attendre
qu'une présence — pas une lisibilité — dans les plans larges.

### Limite des keyframes : la foule figée (constaté le 2026-09-29)

Deux images d'appui qui partagent **la même foule aux mêmes places** (cas d'une image A
obtenue en éditant B) forcent chaque passant à finir là où il a commencé : le modèle
les laisse **immobiles**. Le décor est stable, mais la rue est morte.

Règle : les keyframes A→B conviennent quand **seul le sujet** doit changer d'état
(la marque qui s'allume, le masque qui se déploie). Dès que **l'environnement doit
vivre**, n'imposer que la **première image** et donner le personnage en **référence**,
puis décrire le mouvement de la foule explicitement.

## Le son — règle du film (auteur, 2026-09-30)

**Aucune musique. Aucun son d'ambiance généré.** Les générations ne produisent **que les voix**
(ex. Adam, voix Malachi). **Tout le sound design** — ville, foule, circulation, moto, impacts — se
fait **au montage**, par l'auteur, en pistes séparées. C'est ce qui garantit une ambiance continue
d'un plan à l'autre et permet le jeu dramatique du son (la rue qui s'éteint quand Adam chuchote,
puis revient d'un coup sur Kim).

Dans tout prompt vidéo : audio désactivé, ou réduit à la voix seule, et interdire « music, score,
soundtrack, ambient noise ».

## La chaîne de continuité

**Référence de continuité = le plan généré le plus proche dans le temps**, pas la
référence de personnage d'origine. Pour la fin d'un plan, c'est le début du **même**
plan ; pour un nouveau plan, c'est le plan précédent.

Plus la référence est proche temporellement, plus la contrainte est forte : elle porte
d'un coup le visage, la lumière, l'arrière-plan et le rendu de matière.

**Piège à surveiller — la dérive cumulée.** Enchaîner 35 plans en ne référençant que le
précédent fait dériver le personnage par petits pas, chacun invisible. Parade :
**réancrer périodiquement** (tous les 4 ou 5 plans) sur la référence canonique
`REFERENCES/perso_kim_pied_civil.jpg`, et comparer le plan produit au **plan 2** de temps en
temps, pas seulement à son voisin.

## Modèles verrouillés — ne pas changer en cours de film

| Étape | Modèle | Verrouillé le |
|---|---|---|
| 3bis — habillage (image) | **GPT Image 2** (via l'agent GPT-6 Astra ou directement par le MCP) | 2026-09-08 |
| 4 — animation (vidéo) | **Seedance 2.5** (dans Runway) | 2026-09-08 |

Chaque générateur a sa signature : rendu des visages, des peaux, des matières. Changer
de modèle en cours de production ferait dériver le film d'un plan à l'autre, et
rendrait impossible d'attribuer une dérive au pipeline ou au changement d'outil.

**L'homogénéité prime sur la qualité d'un plan isolé.** Même si un modèle plus
performant sort demain, on termine la séquence avec ceux-ci.

## Conventions

- Un plan = un script dans `scripts/plans/`, nommé `plan_XX_description.py`.
  Rejouable et corrigeable ; on ne travaille pas en code jetable.
- Les `.blend` vivent dans `scenes/`, les sorties dans `renders/` (non versionné).
- Les clés API restent dans `.env`, jamais committé.
- `JOURNAL.md` est mis à jour à chaque session de travail.

## Ce que chaque IA apporte

- **Claude (ici)** — pilote Blender, écrit les scripts, assemble. Voit les rendus.
- **Gemini 3.8 Flash (API)** — œil critique sur les images. Palier gratuit :
  les modèles `pro` sont hors quota, les 503 sont fréquents et passagers.
- **Veo / Flow (abonnement)** — génération vidéo, crédits limités, usage manuel.
- **Grok Imagine (abonnement)** — exploration visuelle jetable, en amont.
- **Seedance** — non branché. API seulement (Volcano Engine, fal.ai, Replicate).

## État actuel

Étapes 2 et 3 opérationnelles. Étape 1 à faire par toi. Étapes 4 et 5 à monter.
Le sujet et le style du film restent à définir — ils orienteront tout le reste.
