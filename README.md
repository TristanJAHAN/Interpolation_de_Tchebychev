# Interpolation de Tchebychev en Python

Ce projet implémente l'interpolation polynomiale par les polynômes de Tchebychev.  
La méthode est utilisée pour approximer des fonctions analytiques sur un intervalle donné, avec une précision et une stabilité supérieures à l'interpolation classique de Lagrange.
Ce code est basé sur le cours M.Tordeux, Maîtres de conférences HDR à l'Unviversité de Pau et des Pays de l'Adour (UPPA).

# Construction

- Construction des nœuds de Tchebychev sur un intervalle \([a, b]\)
- Résolution du système d’interpolation par projection (formule exacte)
- Évaluation de l’interpolant sur une grille de points
- Visualisation de la fonction réelle et de l’interpolant
- Calcul et affichage de l’erreur maximale

# Exemple

-Fonction exponnetielle : \( f(x) = e^x \)

# Utilisation

```python
from tchebychev_interpolation import interpolation_tchebychev

erreur, x_eval, f_exact, approx = interpolation_tchebychev(-10, 10)
