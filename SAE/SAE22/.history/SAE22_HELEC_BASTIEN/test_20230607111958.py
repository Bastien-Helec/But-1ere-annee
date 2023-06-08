import numpy as np
import matplotlib.pyplot as plt

# Définition du signal continu X1
temps_continu = np.linspace(0, 1, 1000)  # Plage de temps pour le signal continu
X1 = np.sin(2 * np.pi * temps_continu)  # Exemple de signal continu (sinusoïdal ici)

# Période d'échantillonnage
Te = 0.02  # 20 ms

# Échantillonnage du signal X1
temps_échantillonnage = np.arange(0, 1, Te)  # Plage de temps pour l'échantillonnage
X1ech = np.sin(2 * np.pi * temps_échantillonnage)  # Signal échantillonné

# Représentation graphique
plt.plot(temps_continu, X1, label='X1 (continu)')
plt.plot(temps_échantillonnage, X1ech, marker='o', label='X1ech (échantillonné)')
plt.xlabel('Temps')
plt.ylabel('Amplitude')
plt.title('Signal continu X1 et signal échantillonné X1ech')
plt.legend()
plt.grid(True)
plt.show()