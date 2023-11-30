import pandas as pd
import numpy as np
# import tensorflow as tf

#Le but de ces exercices est de manipuler une base de donnees des contrats futures de l'or
#Le but ici est de ne pas comprendre comment la dataset a ete genere en premier lieu

'''Exercie 01: Implementer la fonction read_data qui prend en parametre le chemin du fichier fourni
et qui retourne en uitlisant la methode de pandas read_csv la dataframe correspondante'''

filepath = "/home/msandi/AI/GC/GC_2022/GC_22.txt"
def read_data(filepath):
    return pd.read_csv(filepath)

'''Exercice 02: Implementer la fonction real_read_data qui prend en parametre le chemin du fichier fourni et
une liste des noms de chaque colonne  ["datetime", "open", "high", "low","close","volume"]
puis retourne le resultat'''

def real_read_data(filepath, names):
    return pd.read_csv(filepath, sep = ';', header = None, names = ["datetime", "open", "high", "low","close","volume"])

'''Exercice 03: On remarque que la forme de datetime n'est pas claire, pour regler ce probleme 
implementer la fonction prepare_data qui prend en parametre filepath, names et divise la colonne datetime en deux :
Date et Time avec Date de la forme annee-mois-jour et Time de la forme Heure:minute:seconde'''

def prepare_data(filepath, names):
    df = real_read_data(filepath,names=["datetime", "open", "high", "low","close","volume"])
    n = df.shape[0]
    for i in range(n):
        a = df.iloc[i]["datetime"] #it's a copy
        df.loc[i,"datetime"]= a[0:4]+"-"+a[4:6]+"-"+a[6:8]+" "+a[9:11]+":"+a[11:13]+":"+a[13:15] #DirectAccess
    df[["Date","Time"]] = df["datetime"].str.split(" ", n = 1, expand=True)
    df = df.drop("datetime", axis = 1)
    return df
    
    
'''Exercice 04: La dataset donnee est en heure UTC, implementer la fonction qui prend en parametre une chaine de caractere du type
heure:minute:seconde et la decale de n heures avec n entier relatif puis retourne la nouvelle chaine '''

def time_UTC_plus_i(time , i):
    var_time = int(time[0:2])
    if (var_time + i >= 24):
        a = 24 - var_time
        if i - a < 10:
            return "0"+f"{i-a}"+time[2:8]
        return f"{i-a}"+time[2:8]
    else :
        return f"{var_time+i}"+time[2:8]

'''Exericie 05: Implementer la fonction qui transfomre la data frame en array'''

def dataframe_to_values(filepath, names):
    return prepare_data(filepath, names).values

"Exercice 06: Implementer la fonction compare_date qui prend en parametre qui les compare et puis  renvoie 1 si la première date est antérieure à la deuxième date, 0 sinon"
def compare_date(date_1, date_2):
    if(int(date_1[0:4]) < int(date_2[0:4])):
        return 1
    elif (int(date_1[0:4])> int(date_2[0:4])):
        return 0
    if(int(date_1[5:7]) < int(date_2[5:7])):
        return 1
    elif (int(date_1[5:7])>int(date_2[5:7])):
        return 0
    if(int(date_1[8:10]) < int(date_2[8:10])):
        return 1
    elif(int(date_1[8:10])> int(date_2[8:10])):
        return 0
    else : return 0
    
'''Exercice 07: Implemnter la fonction final_data qui transforme la base de donnees en un tenseur de rang 3 (voir cours partie : Donnees temporelles
et Sequentielles)'''

def final_data(filepath, names):
    L = dataframe_to_values(filepath, names)
    M = []
    G = []
    last_date = L[0][5]
    for i in range(len(L)):
        date = L[i][5]
        if(not compare_date(last_date, date)):
            M.append(list(L[i]))
        else:
            last_date = date
            G.append(list(M))
            M = []
    return G

"""Question: pourquoi on a travaille avec des listes au lieu des tenseurs directement """