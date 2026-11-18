# La démarche créative — ordre de création

Deux inversions par rapport au cinéma classique, à garder en tête :
le **budget de plans précède l'écriture**, et la **bible visuelle se verrouille
avant toute génération**. C'est là qu'on se plante sinon.

## 1. L'intention — une phrase
Un personnage, un désir, un obstacle. Une situation, pas un thème.
Si la phrase est molle, aucun outil ne rattrape le film.

## 2. Le budget de plans — AVANT l'écriture
Les crédits Veo sont finis ; un plan généré dure ~8 s.
On décide d'abord le nombre de plans, ce qui fixe la durée du film.
Repère : 40 plans × 6 s ≈ 4 minutes. La contrainte force la concision.

## 3. Le séquencier
5 à 8 séquences, une ligne chacune. Vérifier que l'arc tient dans le budget
avant d'écrire une ligne de dialogue.

## 4. Le découpage — le document central
Par plan : valeur, focale, mouvement, durée, action.
C'est ce document que Claude traduit en scènes Blender. **Un plan = une ligne = un script.**
Contrainte dure : **une seule idée par plan** — la génération IA ne tient pas deux actions.

## 5. La bible visuelle — à verrouiller
La cohérence est le problème n°1 de la vidéo IA (visages, décors qui dérivent).
Figer avant toute génération :
- **personnages** : images de référence, plusieurs angles, réutilisées à chaque plan
- **palette** : 4-5 couleurs maximum
- **lumière** : une logique unique
- **focales** : 2-3 maximum — c'est la signature visuelle
- **format** : ratio et grain

### Où intervient Grok
C'est **sa** fenêtre — et la seule. Outil de divergence, pas de production.
- personnages en dix variantes, puis la bonne sous plusieurs angles
- décors en plusieurs ambiances
- la même scène en plusieurs lumières (le test le plus rentable)
- palette : observer ce qui revient dans les images qui plaisent

Générer beaucoup, jeter presque tout. Ce qui survit va dans `REFERENCES/` et fait loi.
Nommer clairement (`perso_gardien_face.png`) : Claude peut lire ces images et les
analyser avec Gemini (extraire la palette, vérifier qu'un rendu respecte la lumière choisie).

Second usage : **la répétition**. Grok Imagine fait de l'image→vidéo rapide ; tester
une idée de mouvement chez lui avant d'investir un crédit Veo. C'est un brouillon, pas une prise.

**Grok s'arrête dès la bible verrouillée.** Continuer à générer pendant la production
réintroduit la dérive qu'on cherche à éliminer : chaque génération repart de zéro.
La cohérence vient de la réutilisation des références, pas de nouvelles générations.
Étapes 1-5 : Grok à fond. Étapes 6-9 : Grok fermé.

Ses images ne sont pas les plans finaux (style marqué, pas de contrôle du cadrage).
Pas de clé API via l'abonnement : usage manuel, par l'utilisateur. C'est voulu —
la direction visuelle est une décision de réalisateur.

## 6. Le plan pilote
UN plan de bout en bout (blocking → critique Gemini → Veo → export) avant les autres.
Calibre tout pour le prix d'un plan au lieu de quarante. Ne pas sauter cette étape.

## 7. L'animatique
Tous les plans en blocking grossier, montés au bon timing, **sans aucune génération**.
Des cubes gris suffisent. On voit le film avant de dépenser un crédit.
C'est là qu'on coupe les plans inutiles — il y en a toujours, et c'est du budget récupéré.

## 8. La production
Plan par plan. **Commencer par les plans les plus difficiles** : s'ils sont
infaisables, autant le savoir tôt.

## 9. Montage, son, étalonnage
Le son se fabrique en dernier mais se **pense dès le découpage** : il porte la moitié
de l'émotion et corrige beaucoup des faiblesses de l'image générée.

---

## Répartition
- **Toi** : intention, écriture, découpage, bible visuelle. Le vrai travail de réalisation.
- **Claude** : blocking Blender, scripts, critique automatisée, animatique, assemblage.

## À retenir
1. Le découpage et la bible visuelle sont le cœur du travail ; le reste est exécution.
2. Verrouiller avant de générer — toute décision reportée se paie en crédits gaspillés.
3. Faire l'animatique : dernier moment où le film peut encore changer gratuitement.
