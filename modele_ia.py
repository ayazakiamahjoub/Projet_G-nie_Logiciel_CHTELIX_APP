import numpy as np
from sklearn.linear_model import LinearRegression

def predire_collecte(m1, m2, m3, mois_cible):
    
    X = np.array([[1], [2], [3]])
    y = np.array([m1, m2, m3])
    modele = LinearRegression()
    modele.fit(X, y)
    
    prediction_base = modele.predict([[4]])[0]
    
    # Haute saison : Juin(6) à Septembre(9) -> Pic en Juillet(7) et Août(8)
    coefficients_saison = {
        1: 0.8, 2: 0.8, 3: 0.9,  # Hiver : Basse saison
        4: 1.0, 5: 1.1,          # Printemps : Reprise
        6: 1.3, 7: 1.5, 8: 1.5, 9: 1.3, # Été : HAUTE SAISON (Pic)
        10: 1.1, 11: 0.9, 12: 0.8 # Automne/Hiver : Baisse
    }
    
    coef = coefficients_saison.get(mois_cible, 1.0)
    
    prediction_finale = prediction_base * coef
    
    if prediction_finale < 0:
        return 0.0
        
    return round(prediction_finale, 2)
