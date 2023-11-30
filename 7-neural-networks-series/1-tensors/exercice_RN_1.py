import pandas as pd
import numpy as np
# import tensorflow as tf

#Le but de ces exercices est de manipuler une base de donnees des contrats futures de l'or
#Le but ici est de ne pas comprendre comment la dataset a ete genere en premier lieu

'''Exercie 01: Implementer la fonction read_data qui prend en parametre le chemin du fichier fourni
et qui retourne en uitlisant la methode de pandas read_csv la dataframe correspondante'''




'''Exercice 02: Implementer la fonction real_read_data qui prend en parametre le chemin du fichier fourni et
une liste des noms de chaque colonne  ["datetime", "open", "high", "low","close","volume"]
puis retourne le resultat'''




'''Exercice 03: On remarque que la forme de datetime n'est pas claire, pour regler ce probleme 
implementer la fonction prepare_data qui prend en parametre filepath, names et divise la colonne datetime en deux :
Date et Time avec Date de la forme annee-mois-jour et Time de la forme Heure:minute:seconde'''



    
    
'''Exercice 04: La dataset donnee est en heure UTC, implementer la fonction qui prend en parametre une chaine de caractere du type
heure:minute:seconde et la decale de n heures avec n entier relatif puis retourne la nouvelle chaine '''





'''Exericie 05: Implementer la fonction qui transfomre la data frame en array'''





"Exercice 06: Implementer la fonction compare_date qui prend en parametre qui les compare et puis  renvoie 1 si la première date est antérieure à la deuxième date, 0 sinon"




    
'''Exercice 07: Implemnter la fonction final_data qui transforme la base de donnees en un tenseur de rang 3 (voir cours partie : Donnees temporelles
et Sequentielles)'''





"""Question: pourquoi on a travaille avec des listes au lieu des tenseurs directement """