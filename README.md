# Analyse et Suppression des Amis Inactifs sur Discord

Ce script Python vous permet d'analyser l'activité de vos amis sur Discord et de supprimer automatiquement ceux qui sont inactifs depuis une semaine.

![Discord Friends](images/discord-friends.png)

## Installation

1. Assurez-vous d'avoir Python 3.x installé sur votre machine.
2. Clonez ce dépôt ou téléchargez le fichier [discord_friends.py](discord_friends.py).

## Configuration

1. Obtenez votre token Discord 
2. Remplacez `VOTRE_TOKEN_DISCORD` par votre token dans le fichier `discord_friends.py`.

## Utilisation

1. Ouvrez une invite de commande (terminal) et naviguez vers le répertoire contenant le fichier `discord_friends.py`.
2. Installez les dépendances nécessaires en exécutant la commande suivante :

   ```shell
   pip install discord.py
Exécutez le script avec la commande suivante :

shell

python discord_friends.py
Le script analysera l'activité de vos amis après une semaine et affichera les amis inactifs.

Si vous souhaitez supprimer les amis inactifs, décommentez la dernière section du code dans discord_friends.py.

Vous serez invité à confirmer chaque suppression avant qu'elle ne soit effectuée.

Avertissement
Veuillez noter que la suppression automatique d'amis va à l'encontre des directives de Discord. Assurez-vous de comprendre les conséquences de cette action et communiquez avec vos amis avant de supprimer quiconque.



© 2023 Akan. Distribué sous la licence MIT. Voir LICENSE pour plus d'informations.
