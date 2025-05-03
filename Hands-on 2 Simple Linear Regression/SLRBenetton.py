import numpy as np # Libreria para manejo matematico

# Valores dados para el caso de Benetton
X = np.array([23, 26, 30, 34, 43, 48, 52, 57, 58])  # Advertising
Y = np.array([651, 762, 856, 1063, 1190, 1298, 1421, 1440, 1518])  # Sales

n = len(X) # Guardamos la cantidad de registros de X

# Calculo de sumatorias para despues calcular B0 Y B1
sumX = np.sum(X)
sumY = np.sum(Y)
sumXY = np.sum(X * Y)
sumX2 = np.sum(X**2)

# Calculo de B1 y B0
B1 = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX**2)
B0 = (sumY - B1 * sumX) / n

# Mostramos la ecuacion de regresion
print(f"\nEcuacion de Regresion: Sales = {B0:.2f} + {B1:.2f} * Advertising")

# Damos valores desconocidos para realizar predicciones
advertising_pred = [21, 28, 55, 60, 68]

# Predicciones para valores desconocidos
print("\nPredicciones de Sales con valores desconocidos:")
for x in advertising_pred:
    x_pred = B0 + B1 * x
    print(f"Advertising = {x}: Sales ≈ {x_pred:.2f}")