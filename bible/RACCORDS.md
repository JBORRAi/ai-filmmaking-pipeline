# Raccords — la grammaire du montage

Ce que l'IA rate le plus souvent : non pas la beauté du plan, mais **l'enchaînement**.
Une séquence IA raconte mal parce que l'œil du spectateur est renvoyé n'importe où
d'un plan à l'autre. Ce document est la loi de continuité de la séquence.

## Les cinq règles

1. **L'axe ne se franchit pas** (règle des 180°). Une ligne imaginaire relie Kim aux
   motos. La caméra reste **d'un seul côté** de cette ligne pour toute la séquence.
   La franchir inverse les directions et perd le spectateur.

2. **Continuité de vecteur.** Deux mouvements de caméra opposés ne s'enchaînent
   jamais : **jamais un travelling avant sur un travelling arrière**. Un mouvement
   se prolonge, se ralentit, ou passe à un fixe — il ne s'inverse pas.

3. **Le regard ne saute pas, il est amené.** On ne change pas l'orientation d'un
   regard par une coupe. Si Kim doit regarder ailleurs, **c'est un mouvement du
   personnage ou de la caméra qui l'y conduit**, dans le plan.

4. **Raccord dans le mouvement.** On coupe **pendant** le geste, jamais après.
   Le mouvement commencé au plan A se termine au plan B : l'œil ne voit pas la coupe.

5. **Progression de l'échelle.** On ne passe pas d'un très grand large à un très gros
   plan. On monte ou on descend par paliers — sinon la coupe se voit.

---

## L'axe de la séquence

**Kim se déplace et regarde vers la DROITE du cadre. Pour toute la séquence.**

- Il marche vers la droite (plans 1-5).
- L'avenue fuit vers la droite et vers le fond.
- Les motos arrivent du fond et filent **vers la droite**.
- **L'homme au costume est à GAUCHE**, sur le trottoir opposé.
- Kim le regarde à gauche, puis **pivote vers la droite** pour partir.
- Il s'élance vers la droite. La traînée rouge part vers la droite.

Ce pivot (plan 20) est le seul changement de regard de la séquence — **et il est joué,
pas coupé**. C'est le mouvement du corps qui amène l'œil de gauche à droite.
C'est exactement l'application de la règle 3.

Caméra **toujours du même côté de l'avenue**. Jamais de plan pris du trottoir d'en face.

---

## Audit du découpage — trois fautes corrigées

### Faute 1 — alternance dos / face / dos (plans 1 → 4)
Version fautive : plan 1 de dos, plan 2 caméra qui le précède (donc de face),
plan 3 de dos à nouveau. L'œil est ballotté d'un côté à l'autre du personnage.

**Correction** : on tourne progressivement autour de lui, en arc.
`dos (1) → dos rapproché (2) → profil latéral (3) → face (4)`.
Le regard du spectateur est **amené** au visage au lieu d'y être jeté.

### Faute 2 — travelling arrière suivi d'un travelling latéral (plans 2 → 3)
Deux vecteurs contradictoires collés. Corrigé par l'arc ci-dessus : le travelling
devient **un seul mouvement continu** réparti sur trois plans, toujours dans le même sens.

### Faute 3 — filé violent suivi d'un fixe (plans 15 → 16)
Les motos traversent en filé, puis coupe sèche sur un gros plan fixe. L'œil s'écrase.

**Correction** : le plan 16 conserve un **résidu de mouvement** — léger filé qui
s'immobilise, cheveux et vêtements encore agités par le souffle. La vitesse meurt
dans le plan au lieu de mourir dans la coupe.

---

## Table des vecteurs — vérification plan par plan

| Plans | Vecteur | Enchaînement |
|---|---|---|
| 1 → 5 | arc continu autour de Kim, sens unique | dos → profil → face, puis fixe |
| 6 → 12 | **immobilité** | tout est fixe : le son seul travaille |
| 13 → 15 | gauche → droite (les motos) | accélération progressive jusqu'au filé |
| 16 | résidu de mouvement | absorbe le filé du 15 |
| 17 → 19 | regard à **gauche** (l'homme) | fixes, échelle qui se resserre |
| 20 | **le pivot** : gauche → droite | joué par le corps, pas par la coupe |
| 21 → 28 | immobilité + descente d'échelle | large → moyen → gros → insert |
| 29 → 32 | droite, accélération | la fissure prépare le vecteur du départ |
| 33 → 35 | droite, décélération | poursuite → foule figée → avenue vide |

Le plan **30** (la caméra suit la fissure au ras du sol) est le pivot technique de
la fin : il **installe le vecteur droite à pleine vitesse** avant même que Kim ne
démarre. Quand il part au plan 32, l'œil est déjà lancé dans le bon sens.

---

## Le panoramique vertical n'est pas un mouvement de caméra comme un autre

Sur un plan frontal où le sujet marche **vers** l'objectif, un cadre strictement
verrouillé **perd sa tête** : le sujet grandit, son visage monte, ses pieds sortent.
Un opérateur compense par un léger **tilt vers le haut**. C'est une correction de
cadrage, pas un effet.

Et cela ne contredit pas la règle 2 (continuité de vecteur) : **un mouvement vertical
n'entre pas en conflit avec un vecteur horizontal**. Le tilt du plan 2 laisse intact
l'axe droite installé au plan 3.

Règle : sur tout plan frontal en approche, autoriser le tilt vertical de suivi,
interdire tout le reste (avance, zoom, panoramique horizontal, orbite).

**Dimensionnement** : à ~100 mm, un sujet à 13 m qui marche 5 s à allure normale
parcourt 7 m et finit hors cadre. Le tilt ne suffit pas — il faut aussi **ralentir
la marche** dans la demande (« trois ou quatre pas sur tout le plan »).

## La direction doit être ÉCRITE, pas seulement montrée

Constat du 2026-09-08, sur le plan 3 : le blocage Blender plaçait Kim en déplacement
vers la droite — **vérifié par calcul** (produit scalaire 0,61). Le générateur a
quand même produit un plan **frontal orienté vers la gauche**.

**Le générateur ne lit pas la direction dans l'image de contrôle.** Il en tire le
cadrage, l'échelle et la lumière, mais pas le vecteur.

Règle : sur **chaque** plan, écrire la direction en toutes lettres dans le prompt —
« travelling from the LEFT side of the frame toward the RIGHT », « shoulders angled
to the right » — et interdire explicitement les autres (`frontal walk toward camera`,
`walking to the left`).

L'image de contrôle sert la composition. **Les mots servent le montage.**

**Nuance importante, apportée par l'auteur le 2026-09-08** : sur un plan animé, la
direction peut aussi être installée **par la rotation du personnage à l'intérieur du
plan**, plutôt que par une pose déjà orientée. C'est même préférable — c'est
l'application de la règle 3 (le regard est amené par un mouvement). Une image de départ
en léger trois-quarts qui se résout en profil vaut mieux qu'un profil figé d'emblée.

Raisonner sur les cinq secondes, pas sur le photogramme.

## Les trois blocs de rythme

- **Plans 6 à 12 — tout est fixe.** Aucun mouvement de caméra pendant l'alerte.
  L'immobilité crée l'impuissance ; c'est le son qui porte. Bouger ici tuerait l'effet.
- **Plans 21 à 28 — tout est fixe aussi**, mais l'échelle se resserre par paliers.
  La tension monte par le cadre, pas par le mouvement.
- **Plans 29 à 35 — tout bouge, dans un seul sens.** La libération.

La séquence est donc : mouvement → **immobilité** → immobilité resserrée → explosion.
Les deux blocs fixes rendent le départ violent. C'est le contraste qui fait l'effet,
pas la vitesse elle-même.

## Contraintes optiques mesurées (à ne pas redécouvrir)

Hauteur de capteur en 2.39:1 = 36 / 2,39 = **15,06 mm**.
Distance minimale pour contenir un corps de 1,78 m : **1,78 × focale / 15,06**.

| Focale | Distance mini | Conséquence |
|---|---|---|
| 35 mm | **4,1 m** | focale d'accompagnement : elle encaisse les passages rapprochés |
| 85 mm | **10,0 m** | coupe la tête en deçà — inutilisable pour un passage devant l'objectif |
| 200 mm | **23,6 m** | **rien ne peut être placé entre la caméra et le sujet** |

Le cas du 200 mm est le plus contraignant : tout objet intermédiaire — piéton,
voiture, mât de feu — remplit la hauteur du cadre et le noie en flou. La profondeur
doit venir de ce qui est **à la distance du sujet ou au-delà**, jamais devant lui.
Vérifier la ligne de vue par `scene.ray_cast` avant de rendre.

## Le point de vue du film — décidé le 2026-09-29

**Plan 4 : panoramique, pas poursuite.** La caméra *regarde passer* Kim, elle ne le
suit pas. Le film garde un regard posé, observateur : personne n'est derrière
l'objectif. La présence qui poursuit reste réservée au finale, où c'est Kim qui poursuit.

**Plans 2 et 4bis : deux 200 mm, une rime et non un doublon.** Même focale, deux axes :
de face au plan 2 (il vient vers nous, prisonnier de la foule), de profil au 4bis (il la
traverse). La compression revient sous un autre angle ; c'est la ville qui l'enserre.

## D'où vient le danger — tranché par l'auteur le 2026-09-29

**Le danger vient de la DROITE de Kim : de l'avenue elle-même, côté chaussée (+Y).**
Kim est tourné vers −X ; sa droite est +Y, le côté de la chaussée et des caméras.

Conséquence : au cri, les passants se tournent vers la chaussée, donc **face aux caméras
placées côté chaussée** — en particulier celle du plan 4bis. Un mur de visages se retourne
vers le spectateur ; Kim, lui, reste de profil. Son regard glisse vers **sa droite**.

(Hypothèse antérieure, fausse : « le danger vient de derrière lui, +X ». Abandonnée.)

### Position exacte de la source du cri (2026-09-29)

Sur l'avenue, **en avant de Kim et à sa droite** : direction −X / +Y depuis sa position.
Vérifié dans les deux axes :
- plan 6 (caméra devant lui) → **gauche du cadre**, légèrement vers la caméra ✓ (généré ainsi)
- plan 7 (axe 4bis, caméra de l'autre côté de l'avenue) → **droite du cadre**, vers la caméra :
  visages de trois-quarts, sans regard caméra
C'est aussi la direction de fuite des motos et du départ de Kim : tout converge.

### Correction — la source est DERRIÈRE et à droite de Kim (2026-09-29, plus tard)

Précision de l'auteur au plan 7 : Kim regarde **d'où il vient** (+X) et la chaussée est **à sa
gauche**. La source du cri est donc en **arrière et à droite** de sa position d'arrêt (+X / +Y),
et non en avant (−X / +Y) comme noté juste au-dessus. Plan 6 reste cohérent (tête vers la gauche
du cadre). L'homme à terre gît sur le trottoir, à ~36 m en +X ; une moto arrive de là, vers lui.
