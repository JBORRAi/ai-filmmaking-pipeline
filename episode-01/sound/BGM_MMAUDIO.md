# BGM — nappes de tension (MMAudio, texte → musique de fond)

But : un **lit sonore** cohérent sur les 17 extraits, pas de mélodie. Des cordes de suspense et des
nappes de tension, pour poser plus tard un thème par-dessus.

## Les 3 règles de cohérence
1. **La même phrase socle** au début de CHAQUE prompt (copier-coller exact).
2. **La même graine (seed) : `1717`** partout.
3. **Le même negative prompt** partout.
Seule la partie « intensité » change d'un extrait à l'autre.

**Phrase socle (à coller en premier) :**
`Dark cinematic underscore in D minor, no melody, sustained string ensemble and low synth pad drone, tense and restrained, dry modern thriller sound,`

**Negative prompt (partout) :**
`melody, theme, lead instrument, piano, drums, percussion beat, vocals, voice, singing, choir, humming, whispering, spoken words, breathing, guitar, electronic dance, upbeat, major key, happy, epic trailer brass`

**Graine :** `1717`

## Les 17 prompts (socle + intensité)

| # | Extrait (timecode) | Durée | Intensité (à ajouter après le socle) |
|---|---|---|---|
| 01 | 0:00.00 | 5.0 s | barely audible, a soft low cello drone, calm but uneasy, city at rest |
| 02 | 0:05.04 | 7.8 s | very quiet, low cello drone with faint high violin harmonics, subtle unease |
| 03 | 0:12.86 | 7.8 s | quiet and intimate, a single high violin harmonic held over the low drone, mysterious |
| 04 | 0:20.67 | 2.7 s | sudden sharp string stab then trembling tremolo violins, shock |
| 05 | 0:23.33 | 7.8 s | nervous tremolo violins over the drone, tension rising, heartbeat-like low pulse |
| 06 | 0:31.12 | 7.8 s | fast agitated tremolo strings, rising pitch, urgent tension |
| 07 | 0:38.92 | 5.5 s | tension suspended, strings hold one dissonant chord, uneasy stillness |
| 08 | 0:44.38 | 7.7 s | sorrowful and fragile, very soft sustained strings, low and grieving, sparse, lots of empty space |
| 09 | 0:52.12 | 5.6 s | almost silent, a thin high violin note slowly swelling, a decision forming |
| 10 | 0:57.75 | 5.6 s | pulsing low strings and a deep synth swell, power awakening, building |
| 11 | 1:03.38 | 6.4 s | driving low string ostinato, heavy and determined, intensity building |
| 12 | 1:09.75 | 9.5 s | massive slow crescendo, dense string clusters and deep sub drone, pressure rising |
| 13 | 1:19.25 | 9.5 s | extreme tension, strings climbing in pitch and volume, relentless crescendo to the breaking point, cut dead at the end |
| 14 | 1:28.75 | 2.0 s | **SILENCE — ne pas générer** |
| 15 | 1:30.75 | 1.4 s | a single held ultra-high violin note, breath before impact |
| 16 | 1:32.17 | 4.7 s | **pas de BGM** — laisser toute la place au mur du son |
| 17 | 1:36.83 | 4.0 s | aftermath, a low dark sustained string chord slowly fading into silence |

## Au montage
- Mettre les BGM sur une piste à part, **-18 à -24 dB** sous les bruitages : c'est un support.
- Fondus enchaînés de 0,5 à 1 s entre les extraits pour lisser les raccords.
- Couper net la BGM à la déflagration (fin du 13) : le silence du 14 doit être total.
- Le futur thème viendra en tonalité de **ré mineur** pour coller aux nappes.
