# Othello

Pour comprendre le jeu : [Othello](https://www.eothello.com/).

## Créer un joueur

Vous devez écrire un fichier python contenant une classe appelée **exactement** ``MyPlayer`` qui hérite de la classe ``Player``. Un exemple est donné dans le fichier ``base_player.py``.

Vous n'avez alors qu'à implémenter la fonction ``choose_next_move`` qui choisit quel coup jouer sous la forme d'un tuple ``(ligne, colonne)``. 

Vous avez accès aux fonctions de ``board.py``, pensez à aller les voir elles peuvent être utile. Vous pouvez aussi les réimplémenter vous même, notamment si vous voulez les rendre plus rapide.

## Ajouter le joueur aux compétitions

Rendez-vous sur [ce lien](https://aaguilamultn.zzz.bordeaux-inp.fr/ladder/).
Vous y trouverez un formulaire permettant d'upload un fichier. Si le fichier est correct, votre joueur apparaitra à la prochaine itération !

**ATTENTION** : pour ajouter un nouveau joueur, vous devez être connecté au réseau de l'enseirb. C'est à dire soit sur le wifi Bordeaux-INP, soit sur les ordis de l'école, soit connecté en ssh. Sinon vous ne verrez que le classement.

Le nom de votre joueur est le nom du fichier. Si vous uploadez un fichier avec le même nom qu'un joueur existant, ce dernier sera écrasé. Servez-vous en pour ne pas avoir trop de versions différentes de votre joueur.

## Comment fonctionne la ladder

Chaque joueur joue un match aller-retour contre tous les autres. Le score est (actuellement) le nombre de cases que le joueur possède à la fin de la partie. Si le joueur joue un coup invalide ou cause une erreur pendant son tour, son score est de -500.
Le classement est ensuite calculé en fonction du nombre de points total.

Si vous remarquez un bug sur le jeu ou la ladder, remontez le moi assez vite svp.

Le jeu a été codé par Cléa (cléa#2543 sur discord) allez lui dire merci 🙂.