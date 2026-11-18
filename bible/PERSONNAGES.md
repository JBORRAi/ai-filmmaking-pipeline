# Personnages

## Kim Jeon-Ho — héros

Jeune homme coréen, la vingtaine. Visage fin, mâchoire nette, regard intense.
Cheveux noirs mi-longs, épais, ébouriffés, mèches tombant sur le front.

### Costume (constant)
- Perfecto en cuir noir, col à revers, boutons-pression argentés, zips obliques
- Col roulé noir en maille
- Pantalon cargo noir resserré aux chevilles, sangles et boucles tactiques
- **Baskets noires à semelle épaisse** — canonique, décidé le 2026-09-08.
  Ce sont elles qui portent les LED rouges dans l'état déchaîné. **Jamais de rangers** :
  un personnage à super-vitesse part en starting-block, pas en bottes militaires.
- Montre noire au poignet gauche

**Tout est noir.** Le rouge est la seule autre couleur du personnage — c'est ce qui
fait la signature visuelle.

### Les trois états — c'est la grammaire du personnage

| État | Signes | Sens |
|---|---|---|
| **Civil** | visage nu, aucune lumière, marque éteinte | il se cache |
| **Armé** | masque en place, LED rouges allumées | il est prêt |
| **Déchaîné** | énergie rouge courant sur les membres, sol qui se fissure | il lâche tout |

### Les accessoires signifiants
- **Le masque** — demi-masque cyberpunk carbone couvrant nez et bouche, nervures
  LED rouges, respirateur central. Les yeux restent visibles.
- **Les yeux** — iris rouges lumineux quand le pouvoir est actif (`detail_yeux_rouges_tgp`).
- **La marque 속** — idéogramme coréen (« intérieur », « ce qui est dedans ») derrière
  l'oreille droite. **Éteinte au repos, rougeoyante quand le pouvoir monte.**
  Deux images documentent les deux états : c'est un excellent indicateur discret,
  utilisable en gros plan pour signaler la bascule sans dialogue.
- **Les LED du costume** — trois niveaux existent dans les refs : baskets seules,
  baskets + jambes, ou rien. À utiliser comme jauge d'intensité.

### Le pouvoir
Super-vitesse. Manifestations documentées : gerbes d'étincelles sous les appuis,
sol qui se fissure au départ, débris projetés, flou de vitesse radial,
énergie rouge courant le long des bras et des jambes.

Départ en position de sprinteur, poings ou paume au sol — c'est sa posture signature.

---

## Cohérence — à surveiller

Deux images ont été **supprimées** le 2026-09-08 : ce n'était pas le même acteur
(cheveux bouclés, morphologie et visage différents, rue européenne en plein jour).
Grok avait dérivé. Elles restent récupérables dans l'historique git si besoin.

C'est exactement le problème annoncé dans `DEMARCHE.md`. Les images de référence
de visage, à réinjecter à chaque génération, sont `perso_kim_face_visage_decouvert.jpg` et
`perso_kim_planche_4poses.jpg` — ce sont elles qu'il faut réinjecter à chaque génération.

À noter aussi : dans les triptyques `pose_*` et les plans d'action, le visage paraît
plus âgé et plus dur que dans la planche de référence. Dérive légère, à corriger.

---

## Lumière et décor — VERROUILLÉ

**Journée d'avril à New York.** Décision prise le 2026-09-08, non négociable.

Ce que ça implique concrètement :
- Lumière naturelle de printemps : soleil encore bas, ciel clair à voilé, air froid
- Rues en canyon : façades hautes, **ombres portées profondes même en plein midi**
- Arbres à peine bourgeonnants, pas de feuillage dense
- Palette de fond : gris pierre, brique, bleu du ciel — donc **froide**

### Comment garder le rouge lisible en plein jour

C'était la réserve : les LED rouges risquent de disparaître dans une lumière forte.
Les parades, à appliquer au découpage :

1. **Jouer les côtés d'ombre.** Une avenue new-yorkaise a toujours un trottoir au
   soleil et un à l'ombre. Kim évolue du côté sombre, le fond reste lumineux :
   la silhouette noire se détache, le rouge revit.
2. **Le fond froid sert le rouge.** Gris et bleus sont les complémentaires du rouge —
   en étalonnage froid, le rouge saute aux yeux mieux qu'au crépuscule orangé,
   où il se noyait dans une lumière de même température.
3. **Réserver l'état « déchaîné » aux zones sombres** : passages sous échafaudage,
   bouches de métro, ruelles, sous-face de ponts. New York en regorge.
4. **La marque 속 en gros plan** fonctionne quelle que soit la lumière — c'est
   l'indicateur le plus fiable pour signaler la montée du pouvoir.
5. **Les étincelles et débris** restent lisibles de jour : ils jouent sur le
   mouvement et la matière, pas sur la luminescence.

### Références à regénérer

Huit images sont au **crépuscule dans une allée d'arbres** et ne correspondent plus :
`pose_accroupi_crepuscule_triptyque`, `pose_depart_sprint_triptyque`,
`plan_course_etincelles_01` et `_02`, `sequence_depart_blocks_6vignettes`,
`plan_impact_sol_debris`, `plan_coup_de_pied_explosion`,
`plan_activation_energie_sol_fissure`.

Elles restent utiles comme **références de posture et d'effet** (la gestuelle est bonne),
mais leur lumière et leur décor sont à refaire en rue new-yorkaise, jour d'avril.

Les trois `decor_*` sont en revanche **justes** : ce sont elles qui définissent l'ambiance.

---

## Manque dans la bible visuelle — à combler

**Il n'existe aucune référence de Kim en pied, visage découvert.**

- Les trois `costume_pied_*` sont toutes **masquées**
- `perso_kim_face_visage_decouvert.jpg` est un portrait serré
- `perso_kim_planche_4poses.jpg` s'arrête à la taille

Or les **plans 1 à 19 sont tous en état civil** — plus de la moitié de la séquence.
C'est donc la référence la plus utilisée du film, et elle manque.

**Comblé le 2026-09-08** : `perso_kim_pied_civil.jpg` — Kim en pied, visage nu, état
civil. Visage cohérent avec le portrait, pas de dérive d'acteur.

Remplacée le même jour par une version aux **baskets canoniques** (la première montrait
des rangers). C'est désormais la référence d'identité de tous les plans en état civil.

### Règle d'usage des références

Une référence par attribut, et **seulement pour ce que les mots ne savent pas dire** :
- **cadrage** → image (ne se décrit pas)
- **visage** → image (l'identité ne se décrit pas)
- **costume** → **mots**, dans le prompt

Ne jamais mélanger un état avec un autre : une référence masquée sur un plan en état
civil est une contradiction directe, et le générateur tranchera au hasard.

### Règle d'échelle des références

**La référence doit avoir la même échelle que le plan.**
- Plan en pied ou plan large → `perso_kim_pied_civil.jpg`
- Gros plan (plans 4, 19, 25) → `perso_kim_face_visage_decouvert.jpg`

Un portrait serré sur un plan large gaspille le détail du visage ; une image en pied
sur un gros plan ne fournit pas assez de pixels d'identité.

### Défaut des références de la marque (à regénérer)

`detail_marque_sok_eteinte.jpg` et `detail_marque_sok_allumee.jpg` forment une paire
d'états idéale pour le plan 23 — mais **inutilisables telles quelles** :

1. **L'iris est déjà rouge dans les deux.** Ce n'est donc pas « civil → pouvoir » mais
   « pouvoir actif, marque éteinte → allumée ». Or au plan 23 les yeux ne s'allument
   qu'au plan 25. Soit regénérer avec des yeux normaux, soit **inverser l'ordre**
   (yeux d'abord, marque ensuite) — choix de réalisation à trancher.
2. **Le fond est un parc verdâtre**, pas une rue de Manhattan en avril. Même en très
   gros plan, le vert végétal contredit le lieu.

À regénérer en gros plan, rue de Manhattan, en utilisant les images actuelles comme
**référence du glyphe** — à cette échelle il sera reproduit fidèlement.

**Trois images sont nécessaires** (le découpage a évolué le 2026-09-08) :

| # | Image | Usage | État |
|---|---|---|---|
| 1 | `detail_marque_sok_civil.jpg` | **plan 5**, l'insert d'ouverture | **obtenue le 2026-09-08** |
| 2 | marque éteinte, iris rouges | plan 23, keyframe A | à regénérer (fond de parc) |
| 3 | marque allumée, iris rouges | plan 23, keyframe B | à regénérer (fond de parc) |

`detail_marque_sok_civil.jpg` : glyphe 속 correct, encre noire, **iris normal**, fond
minéral urbain. Vérifiée — aucune trace de pouvoir. **Directement utilisable comme
image du plan 5**, sans passer par une génération d'image.

Note de continuité avec le plan 2 : **6,5/10**. Plus basse que les autres, mais sans
gravité : on compare un très gros plan de peau à un plan taille, produits par deux
générateurs différents. Surtout, **ce plan cache l'identité par construction** — on ne
voit qu'une oreille et une joue. C'est l'intention même de l'ouverture.
Sur un gros plan de visage, une telle note serait en revanche un signal d'alerte.

## Référence de visage officielle — `perso_kim_visage_film.png` (2026-09-30)

Choisie par l'auteur : un visage **extrait du plan 8 validé**, et non une image Grok d'origine.
Elle marche mieux parce qu'elle est **rendue dans la matière même du film** (même générateur, même
lumière, même grain) : le modèle n'a rien à traduire.

**Règle** : la référence de visage est le Kim **tel qu'il existe déjà dans le film**. Si un plan
ultérieur donne un visage plus juste ou plus net, on remplace cette référence par un extrait de ce plan.
Limite : 321 × 363 px — suffisant jusqu'au gros plan ; pour un très gros plan, extraire une image plus nette.

### Sangles du cargo — à proscrire (2026-09-30)

Au plan 9, les sangles du pantalon cargo ont été générées comme un long objet noir pendant de sa main,
qui **se lisait comme une arme**. Désormais : **cargo noir sobre, sans sangles pendantes, mains vides**,
précisé dans chaque prompt. Les sangles de la référence `perso_kim_pied_civil.jpg` ne sont pas à reproduire.


---

## Adam Stewart Jr. — l'homme au costume

Rôle : **Adam, un scientifique**, à qui on vient de tirer dessus pour lui voler quelque chose. À terre, blessé ; il chuchote « Catch him… please… we won't survive this… » et **Kim seul l'entend**.
Il ne réapparaît pas : il donne l'autorisation morale.

**Le regard est essentiel** (auteur) : la profondeur de sa détresse — des yeux **embués, sans larmes qui coulent** — et en même temps la **détermination** qu'il faut arrêter ce motard. Les deux dans le même regard. Il regarde **une seule personne** : Kim.

Signes du scientifique et du vol : badge de laboratoire, **mallette ouverte et vide**, lunettes brisées au sol. Blessure par balle à l'épaule, sans gore.

Créé de zéro dans **Grok**, comme Kim. Prompts : `PLANS/P10_chuchotement/2_A_ENVOYER/PROMPT_GROK_adam_*.txt`.

Inspiration de l'auteur : « une sorte de Denzel Washington ». **Traduite en description, jamais en
nom** : les générateurs refusent de reproduire une personne réelle, et un sosie poserait un problème de
droit à l'image. On garde l'esprit — Afro-Américain, la cinquantaine, autorité tranquille, regard à
la fois chaleureux et dur, cheveux courts grisonnants — sans la ressemblance.

Costume : **trois-pièces anthracite**, chemise blanche, cravate sombre. Sombre pour raccorder avec le
plan 7, où il n'est qu'une petite forme sombre sur le trottoir.

Référence : **`REFERENCES/perso_adam_visage.jpg`** (Grok, 2026-09-30) — yeux embués et regard dur, éraflure à la tempe, trois-pièces anthracite, badge de laboratoire.

Badge : « DR. ADAM STEWART JR. — Senior Theoretical Physics — Level 4 Clearance » (nom choisi par l'auteur ; la photo du badge est sans importance).

**Règle des outils** : Grok sert à **créer** les personnages (Kim, Adam) ; les **plans** du film se font en **GPT Image 2**, pour l'homogénéité du rendu.

**Voix d'Adam** : Malachi (Runway, eleven_v3), chuchotée — `PLANS/P10_chuchotement/3_RESULTATS/P10_Adam_voix_FINAL.mp3`. À réutiliser si Adam parle à nouveau.
