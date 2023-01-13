PROJET MOOD FOR TWEET

Projet étudiant dans le cadre de cours à Télécom SudParis
Vous trouverez le modèle de prédiction de mood dans le dossier mymodel_soft

Aucun dataset n'est présent sur ce repository, 

https://www.kaggle.com/code/nathanferet/tweets-good-bad pour exécuter le notebook sur kaggle

Liste des fichiers : 

- rapport.pdf : 
Rapport explicant la démarche du projet

- kaggle.ipynb : 
notebook permettant la construction et la sauvegarde d'un LSTM de prédiction de l'humeur d'un tweet
sauvegarde également séparement la couche de vectorisation dans un pickle

- tweet_maker.py : 
ce fichier python permet de créer un fichier csv contenant les tweets de certains utilisateurs, ainsi que des métadonnées a partir de credentials

- mood_for_tweet.ipynb : 
notebook permettant la construction d'un LSTM de prédiction de série temporelle, ie le mood des tweets, a partir des données générées par le tweet_maker.py

- gifmaker.py : 
script python permettant de générer le gif accuracy.gif

- move_img.sh : 
script utilitaire permettant de déplacer les 200 images servant a créer l'animation accuracy.gif

- accuracy.gif : 
animation montrant la prédiction de série temporelle par le LSTM
