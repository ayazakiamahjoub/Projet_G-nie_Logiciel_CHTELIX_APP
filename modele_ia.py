import numpy as np
from sklearn.linear_model import LinearRegression

def predire_collecte(m1, m2, m3):
    # Les données historiques : Mois 1, 2 et 3
    X = np.array([[1], [2], [3]])
    y = np.array([m1, m2, m3])
    
    # Initialisation et entraînement du modèle
    modele = LinearRegression()
    modele.fit(X, y)
    
    # Prédiction pour le Mois 4
    prediction = modele.predict([[4]])
    
    # On s'assure que la prédiction n'est pas négative
    if prediction[0] < 0:
        return 0.0
        
    return round(prediction[0], 2)