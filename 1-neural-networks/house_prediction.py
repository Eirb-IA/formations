import pandas as pd
import numpy as np
import keras
from keras.layers import Dense
from keras.models import Sequential
from sklearn.model_selection import train_test_split
from plot_keras_history import plot_history
import matplotlib.pyplot as plt

df = pd.read_csv("kc_house_data.csv")

# La colonne que l'on cherche à prédire
target = "price"

# x stocke les entrées (bathrooms,sqft_living,floors,grade,sqft_above,sqft_living15)
x = np.array(df.loc[:, df.columns != target])
# y stocke les sorties (price)
y = np.array(df[target]) 

# On divise en un set d'entraînement et un set de test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=True)

# Création du modèle : 2 couches cachéesde 8 et 16 neurones, 1 valeur de sortie
activation="relu"
model = Sequential([
    Dense(8, activation=activation),
    Dense(16, activation=activation),
    Dense(1),
])

# On indique au réseau de neurones quel algorithme d'optimisation et quelle fonction de coût utiliser
model.compile(optimizer="adam", loss="mean_absolute_error")

# Et on lance l'entraînement sur le set d'entraînement
history = model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))
plot_history(history)
plt.show()

# On vérifie que le modèle fonctionne sur des valeurs qu'il ne connaît pas avec le set de test
# La valeur affichée est la Mean Absolute Error : c'est donc une moyenne des erreurs commises
# Remarque : le modèle a plus de mal sur les valeurs extrêmes. Sur une valeur "normale", l'erreur sera probablement plus petite que ça
model.evaluate(x_test, y_test)

# On peut aussi afficher, pour chaque colonne d'entrée, les prix estimés et les vrais prix
figure = plt.figure(num="Features")
for i in range(6):
    ax = figure.add_subplot(2, 3, i + 1)
    ax.scatter(x_test[:, i], y_test, label="real")
    ax.scatter(x_test[:, i], model(x_test), label="predicted")  
    ax.set_title(df.columns[i + 1])
    ax.legend()
plt.show()