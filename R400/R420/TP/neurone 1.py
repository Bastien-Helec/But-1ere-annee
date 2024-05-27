import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
from sklearn.model_selection import train_test_split


# Chargement des données
data = pd.read_csv('class1.txt', header = 0)
X=np.array(data["x"])
Y=np.array(data["y"])
c=data["class"]


plt.figure()


# Donnée d'entrainement et de test
X_train, X_test, Y_train, Y_test, c_train, c_test=train_test_split(X,Y,c,test_size=0.5)
#plt.scatter(X_train,Y_train, marker="x",c=c_train)
plt.scatter(X_test,Y_test, marker="o",c=c_test)


# Définition du modèle
model = tf.keras.Sequential([
    tf.keras.layers.Dense(4, activation='relu', input_shape=(2,)),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compilation du modèle
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Entraînement du modèle
train_data=np.transpose(np.array([X_train, Y_train]))
train_labels=c_train
model.fit(train_data, train_labels, epochs=300)


# Évaluation du modèle
test_data=np.transpose(np.array([X_test, Y_test]))
test_labels=c_test
test_loss, test_acc = model.evaluate(test_data, test_labels)
print(f'Test accuracy: {test_acc}')

# Prédiction des données de test pour la visu
predictions = model.predict(test_data)
plt.scatter(X_test,Y_test, marker=".",c=np.round(predictions))

plt.show()