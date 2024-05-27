import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix



# Données. Couple H,T confortable et inconfortable
ht_data_i=np.array([[0,0],[10,10],[12,14],[90,20], [30,12], [40,8],[50,16],[60,7],[80,20],[90,17]])
ht_data_c=np.array([[0,15],[20, 16], [21,16.5],[50,18],[92,23],[100,24],[98,30],[70,24]])

# Fonction sigmoïde
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Fonction de coût (log loss)
def log_loss(y_true, y_pred):
    epsilon = 1e-15
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
    return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

# Descente de gradient pour la régression logistique
def gradient_descent(X, y, learning_rate=0.002, epochs=200000):
    m, n = X.shape
    theta = np.zeros(n)
    theta =[ 1, 0, 0]
    loss_history = []

    for i in range(epochs):
        # Calcul du gradient
        z = np.dot(X, theta)
        y_pred = sigmoid(z)
        gradient = np.dot(X.T, (y_pred - y)) / m
        theta -= learning_rate * gradient
        loss = log_loss(y, y_pred)
        loss_history.append(loss)

    return theta, loss_history

# Les données X contient les (H,T) et y les étiquettes
X=np.concatenate((ht_data_c,ht_data_i))
y=np.concatenate((np.ones(len(ht_data_c)),np.zeros(len(ht_data_i))))



# Ajout d'une colonne de 1 pour le biais
X = np.hstack((np.ones((X.shape[0], 1)), X))

# Entraînement du modèle de régression logistique
theta, loss_history = gradient_descent(X, y)

print("Coefficients estimés:", theta)
print("Log loss après l'entraînement:", loss_history[-1])

# Prédiction des étiquettes pour les données de test
y_pred = np.round(sigmoid(np.dot(X, theta)))

# Calcul de la matrice de confusion
confusion = confusion_matrix(y, y_pred)
print("Matrice de confusion :\n", confusion)


# Visualisation des données
plt.scatter(X[:, 1][y == 0], X[:, 2][y == 0], label="Ambiance inconfortable")
plt.scatter(X[:, 1][y == 1], X[:, 2][y == 1], label="Ambiance confortable")


# Calcul de la droite de séparation (séparatrice)
x_values = np.array([X[:, 1].min() - 1, X[:, 1].max() + 1])
y_values = -(theta[0] + theta[1] * x_values) / theta[2]

plt.plot(x_values, y_values, color='red', label="Séparatrice")
plt.xlabel("Humidité")
plt.ylabel("Température")
plt.legend()
plt.title("Visualisation des données et de la séparatrice")
#plt.title("Visualisation des données")
plt.show()

# Visualisation de la descente du gradient
plt.plot(loss_history)
plt.xlabel("Epochs")
plt.ylabel("Log Loss")
plt.title("Descente du gradient (Log Loss)")
plt.show()
