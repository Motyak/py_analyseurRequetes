# ANALYSEUR DE REQUETES TEXTUELLES
## Pourquoi les expressions régulières ?
L'avantage des regex c'est qu'on peut facilement les modifier ou faire évoluer de manière tout à fait contrôlée (contrairement
aux modèles IA). La plupart des langages possèdent une librairie
regex, nous utiliserons la syntaxe PCRE qui est la plus répandue.

## Objectif
Pouvoir dire :
- Joue Hotel California
- Joue Hotel California.
- Je veux que tu joues Hotel California.
- Jouer Hotel California.
- Lance Hotel California.
- Je veux que tu lances Hotel California.
- Lancer Hotel California.
- Je veux écouter Hotel California.
- Pause.
- Arrête la musique.
- Je veux que tu arrêtes la musique.
- Coupe le son.
- Couper.
- Je veux que tu coupes la musique.
- Stop la musique.
- Je veux que tu stoppes la musique.
- Stopper.
- Stoppe la musique.
- Reprend la lecture.
- Reprendre la lecture.
- Je veux que tu reprennes la lecture.
- Continue la lecture.
- Je veux que tu continues la lecture.
- Continuer.

## Comment on s'y prend ?
Dans une requête, on va chercher le premier verbe d'action, puis tout le reste représentera le sujet (pour lequel l'action porte).
Commandes et verbes d'action associés :
- Jouer (un morceau) : joue(s)/jouer, lance(s)/lancer, écouter
- Mettre sur pause : pause, arrête(s)/arrêter, stoppe(s)/stop, coupe(s)
- Reprendre : reprend/reprennes/reprendre, continue(s)/continuer

## Regex
Flags à utiliser : insensitive (, return at first match, single line)
Flags à utiliser pour le test : /img

```
LECTURE = joue(?:s|r)?|lance(?:s|r)?|écouter
PAUSE = pause|arrêtes?|coupe(?:s|r)?|stop(?:pes|per|pe)?
REPRENDRE = repren(?:d|nes)|continue(?:s|r)?

ACTION = .*(LECTURE|PAUSE|REPRENDRE)
       = (?P<ACTION>.*(?:(?P<LECTURE>joue(?:s|r)?|lance(?:s|r)?|écouter)|(?P<PAUSE>pause|arrêtes?|coupe(?:s|r)?|stop(?:pes|per|pe)?)|(?P<REPRENDRE>repren(?:d|nes)|continue(?:s|r)?)))
SUJET = [A-Za-z0-9\ ]*

COMMANDE = ACTION\ ?SUJET\.?
         = (?P<ACTION>.*(?:(?P<LECTURE>joue(?:s|r)?|lance(?:s|r)?|écouter)|(?P<PAUSE>pause|arrêtes?|coupe(?:s|r)?|stop(?:pes|per|pe)?)|(?P<REPRENDRE>repren(?:d|nes)|continue(?:s|r)?)))\ ?(?P<SUJET>[A-Za-z0-9\ ]*)\.?
```

## Output
```console
$ python3 regex.py
Joue Hotel California
  '-> LECTURE: Hotel California       

Joue Hotel California.
  '-> LECTURE: Hotel California       

Je veux que tu joues Hotel California.
  '-> LECTURE: Hotel California

Jouer Hotel California.
  '-> LECTURE: Hotel California

Lance Hotel California.
  '-> LECTURE: Hotel California

Je veux que tu lances Hotel California.
  '-> LECTURE: Hotel California

Lancer Hotel California.
  '-> LECTURE: Hotel California

Je veux écouter Hotel California.
  '-> LECTURE: Hotel California

Pause.
  '-> PAUSE

Arrête la musique.
  '-> PAUSE

Je veux que tu arrêtes la musique.
  '-> PAUSE

Coupe le son.
  '-> PAUSE

Couper.
  '-> PAUSE

Je veux que tu coupes la musique.
  '-> PAUSE

Stop la musique.
  '-> PAUSE

Je veux que tu stoppes la musique.
  '-> PAUSE

Stopper.
  '-> PAUSE

Stoppe la musique.
  '-> PAUSE

Reprend la lecture.
  '-> REPRENDRE

Reprendre la lecture.
  '-> REPRENDRE

Je veux que tu reprennes la lecture.
  '-> REPRENDRE

Continue la lecture.
  '-> REPRENDRE

Je veux que tu continues la lecture.
  '-> REPRENDRE

Continuer.
  '-> REPRENDRE
```
