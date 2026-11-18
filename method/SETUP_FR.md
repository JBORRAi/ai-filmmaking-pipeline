# Installation technique — Blender piloté depuis Claude Code

Installé le **2026-09-08**. Machine : macOS (Darwin 25.6), `~`.

## Ce qui est en place

| Élément | Détail |
|---|---|
| Blender | 4.5.13 LTS, `/Applications/Blender.app` |
| `uv` / `uvx` | `~/.local/bin/` — installeur standalone Astral |
| Addon Blender | `~/Library/Application Support/Blender/4.5/scripts/addons/blender_mcp.py` (v1.6) |
| Copie de secours | `~/Desktop/blender_mcp.py` |
| Serveur MCP | déclaré dans `~/.claude.json` sous la clé `blender` |
| Port de liaison | `127.0.0.1:9876` (ouvert par l'addon) |

Config MCP :

```json
"blender": { "command": "~/.local/bin/uvx", "args": ["blender-mcp"] }
```

Le chemin vers `uvx` est **absolu volontairement** : le PATH de la session Claude Code
ne contient pas toujours `~/.local/bin`, ce qui faisait échouer les serveurs en `ENOENT`.

## Procédure de démarrage (à chaque session)

1. Lancer **Blender**.
2. Vue 3D → touche **N** → onglet **MCP for Blender** → **Start MCP Server**.
3. Lancer Claude Code. Vérifier avec `/mcp` que `blender` est *connected*.

Vérifier que le port écoute :

```bash
lsof -nP -iTCP:9876 -sTCP:LISTEN
```

## Pièges rencontrés (et leur solution)

- **`brew install uv` reste bloqué** sur la mise à jour des formules.
  → Utiliser l'installeur standalone : `curl -LsSf https://astral.sh/uv/install.sh | sh`
- **L'addon n'apparaît pas dans la liste des Add-ons.**
  → Blender ne scanne `scripts/addons` qu'**au démarrage**. Quitter avec `Cmd+Q`
    (pas juste fermer la fenêtre) et relancer. Il apparaît marqué *Legacy*.
  → Secours : `Preferences → Add-ons → ⌄ → Install from Disk…` et pointer le fichier du Bureau.
- **Ajout d'un serveur MCP en cours de session.** Il n'est chargé qu'au démarrage de
  Claude Code → redémarrer la session.
- **Les outils MCP exigent un argument `user_prompt`.** Même `get_scene_info` le réclame ;
  un appel sans argument échoue en erreur de validation pydantic.
- **`aws-mcp` échouait en `ENOENT`** faute de `uvx` dans le PATH ; corrigé avec le chemin
  absolu. Il renvoie désormais `-32602 Invalid request parameters` — **non résolu**,
  sans rapport avec Blender, à traiter si besoin d'AWS.

## Restauration

Sauvegardes horodatées de la config : `~/.claude.json.bak-*`

Réinstaller l'addon :

```bash
uvx blender-mcp install-addon
```

## Clé API Gemini (Google AI Studio)

Obtenue le 2026-09-08 sur [aistudio.google.com/apikey](https://aistudio.google.com/apikey),
**palier gratuit**, indépendante de l'abonnement Gemini Pro.

- Stockée dans `~/Desktop/COURT-METRAGE/.env` (permissions `600`, ignoré par git). Ne jamais la coller dans une conversation.
- Vérification : `uv run --with google-genai --python 3.11 python scripts/test_gemini.py`
- Modèle retenu : **`gemini-3.8-flash`** (le script choisit automatiquement le flash le plus récent).

### Pièges

- **Format de clé** : les nouvelles clés commencent par `AQ.Ab8...` et non `AIza...`.
  Un contrôle sur le préfixe `AIza` est obsolète.
- **`gemini-2.5-*` est retiré pour les nouveaux comptes** (404 `no longer available to new users`).
  Ne jamais coder un nom de modèle en dur : lister via `client.models.list()` et choisir dynamiquement.
- Cette clé donne accès au **texte et à la vision**, PAS à Veo (vidéo). La vidéo passe par
  l'abonnement Gemini Pro en manuel, via Flow.

## Runway connecté à Claude Code (2026-09-30)

Connecteur ajouté dans l'application Claude (compte claude.ai) → visible dans Claude Code après
redémarrage (`mcp__claude_ai_RUNWAY__*`). Espace « jeremie », forfait Pro. **Crédits partagés** avec
l'application Runway (1 412 au branchement).

Outils utiles : `generate_image` (modèle `gpt-image-2`), `generate_video` (`seedance-2.5`, startFrame,
endFrame, referenceImages, draft), `edit_video` (Aleph), `init_upload`/`complete_upload` (envoi des
fichiers locaux), `get_task`.

**Distinction clarifiée par l'auteur** : **GPT-6 Astra est l'agent LLM** de l'interface Runway, qui
réécrit les prompts ; **GPT Image 2 est le modèle d'image**. Par le MCP, Claude joue le rôle d'Astra :
le prompt part tel quel vers GPT Image 2.

**Règles de coût (auteur, 2026-09-30)** :
- **aucune génération sans accord explicite** (modèle, fichiers, prompt, coût) ;
- **une seule image ou vidéo par génération, jamais de variantes** (`count: 1`) ;
- **pas de mode brouillon** : une image validée suffit à garantir la vidéo — le procédé l a prouvé ;
- **coût mesuré** : solde relevé avant et après chaque génération, consigné dans `COUTS.md`.
