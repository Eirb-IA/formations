import pandas as pd
import numpy as np

classes_df = pd.read_csv("data/classes.csv")
data_df = pd.read_csv("data/zoo.csv")

# y contient le numéro de la classe de chaque ligne de données
y = data_df['class_type']

# On garde le nom à part
names = data_df['animal_name']

# x contient toutes les informations de chaque animal, sans sa classe
x = data_df.drop(columns=['class_type', 'animal_name']).to_numpy()


gorilla = [1,0,0,1,0,0,0,1,1,1,0,0,2,0,0,1] # expect 1
pony = [1,0,0,1,0,0,0,1,1,1,0,0,4,1,1,1] # expect 1
sole = [0,0,1,0,0,1,0,1,1,0,0,1,0,1,0,0] # expect 4
tortoise = [0,0,1,0,0,0,0,0,1,1,0,0,4,1,0,1] # expect 3

test_set = [gorilla, pony, sole, tortoise]
