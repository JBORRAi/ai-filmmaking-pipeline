# Scripts réutilisables

Copies des scripts de KIMKATCHER épisode 1 qui servent à tout projet. Les originaux restent dans
`KIMKATCHER/EP01/scripts/` et `KIMKATCHER/EP01/MAKING-OF/scripts/`.

**À adapter avant usage** : le chemin de base en tête de fichier (constante `B`, `BASE` ou `PROJ`),
qui pointe encore vers `KIMKATCHER/EP01/`.

| Script | Rôle |
|---|---|
| `sync_finalcut.py` | Convertit les `*_FINAL.*` en ProRes 422 HQ avec l'audio, dans `MONTAGE/FINALCUT/` |
| `prompt_depuis_scene.py` | Lit une caméra Blender et écrit un prompt structuré dans `2_A_ENVOYER/` |
| `rendu.py` | Rendus de contrôle Blender, dossiers de plan |
| `voir.py` | Dans Blender : lister les caméras, basculer sur un plan |
| `mannequin.py` · `foule.py` | Personnages et foule de blockout pour Blender |
| `gemini.py` | Critique d'image par l'API Gemini |
| `build_deck.py` | Deck making-of FR/EN en PPTX (puis PDF avec LibreOffice) |
| `banniere_linkedin.py` | Bannière LinkedIn 1584 × 396 |
| `vue_aerienne_blender.py` | Vue aérienne d'une scène Blender, rendu en arrière-plan |
