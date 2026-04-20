# ============================================
# PROYECTO: REGRESIÓN LINEAL - EMISIONES CO2
# AUTOR: David Santiago Paez
# FECHA: 18/04/2026
# ============================================

# --------------------------------------------
# 1. IMPORTACIÓN DE LIBRERÍAS
# --------------------------------------------
# Estas librerías nos permiten trabajar con datos, gráficos y modelos de Machine Learning

import numpy as np                    # Manejo de arrays y operaciones matemáticas
import pandas as pd                  # Manipulación de datos tipo tabla (DataFrame)
import matplotlib.pyplot as plt      # Visualización de datos (gráficas)

from sklearn.model_selection import train_test_split   # Para dividir datos en entrenamiento y prueba
from sklearn.linear_model import LinearRegression      # Modelo de regresión lineal
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score  # Métricas de evaluación


# --------------------------------------------
# 2. CARGA DEL DATASET
# --------------------------------------------
# Se carga un archivo CSV desde una URL externa (como si fuera un Excel online)

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv"
df = pd.read_csv(url)

# Visualizar algunas filas aleatorias para verificar que cargó correctamente
df.sample(5)

# Mostrar estadísticas generales del dataset (promedio, mínimo, máximo, etc.)
df.describe()


# --------------------------------------------
# 3. SELECCIÓN DE VARIABLES IMPORTANTES
# --------------------------------------------
# Se filtran solo las columnas relevantes para el análisis

cdf = df[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB', 'CO2EMISSIONS']]

# Mostrar algunas filas del nuevo DataFrame filtrado
cdf.sample(5)


# --------------------------------------------
# 4. VISUALIZACIÓN DE LOS DATOS
# --------------------------------------------

# Histogramas: permiten ver la distribución de los datos
cdf.hist()
plt.show()

# Gráfica 1: Consumo de combustible vs Emisiones
plt.scatter(cdf.FUELCONSUMPTION_COMB, cdf.CO2EMISSIONS)
plt.xlabel("Fuel Consumption Combined")
plt.ylabel("CO2 Emissions")
plt.title("Relación entre consumo y emisiones")
plt.show()

# Gráfica 2: Tamaño del motor vs Emisiones
plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS)
plt.xlabel("Engine Size")
plt.ylabel("CO2 Emissions")
plt.title("Relación entre tamaño del motor y emisiones")
plt.show()

# Gráfica 3: Número de cilindros vs Emisiones
plt.scatter(cdf.CYLINDERS, cdf.CO2EMISSIONS)
plt.xlabel("Cylinders")
plt.ylabel("CO2 Emissions")
plt.title("Relación entre cilindros y emisiones")
plt.show()


# --------------------------------------------
# 5. PREPARACIÓN DE LOS DATOS
# --------------------------------------------
# Definimos:
# X = variable independiente (entrada)
# y = variable dependiente (lo que queremos predecir)

X = cdf.ENGINESIZE.to_numpy()
y = cdf.CO2EMISSIONS.to_numpy()


# --------------------------------------------
# 6. DIVISIÓN DE DATOS (TRAIN / TEST)
# --------------------------------------------
# Se separan los datos en:
# - entrenamiento (80%) → el modelo aprende
# - prueba (20%) → se evalúa el modelo

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# --------------------------------------------
# 7. CREACIÓN Y ENTRENAMIENTO DEL MODELO
# --------------------------------------------

# Se crea el modelo de regresión lineal
modelo = LinearRegression()

# IMPORTANTE:
# sklearn espera datos en formato 2D → reshape(-1,1)
# (-1) significa "ajusta automáticamente el número de filas"

modelo.fit(X_train.reshape(-1, 1), y_train)


# --------------------------------------------
# 8. PARÁMETROS DEL MODELO
# --------------------------------------------
# El modelo aprende la ecuación:
# y = m*x + b

print("Pendiente (coeficiente m):", modelo.coef_[0])
print("Intercepto (b):", modelo.intercept_)


# --------------------------------------------
# 9. VISUALIZACIÓN DEL MODELO (TRAIN)
# --------------------------------------------
# Se grafican:
# - puntos reales (datos)
# - línea de regresión (modelo)

plt.scatter(X_train, y_train)
plt.plot(X_train, modelo.coef_ * X_train + modelo.intercept_)
plt.xlabel("Engine Size")
plt.ylabel("CO2 Emissions")
plt.title("Modelo entrenado (Train)")
plt.show()


# --------------------------------------------
# 10. PREDICCIÓN
# --------------------------------------------
# El modelo predice valores usando datos de prueba

y_pred = modelo.predict(X_test.reshape(-1, 1))


# --------------------------------------------
# 11. EVALUACIÓN DEL MODELO
# --------------------------------------------
# Métricas para medir qué tan bueno es el modelo

print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("Root Mean Squared Error:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("R2 Score:", r2_score(y_test, y_pred))

# Interpretación:
# - MAE: error promedio
# - MSE: error cuadrático (penaliza errores grandes)
# - RMSE: raíz del MSE (más interpretable)
# - R2: qué tan bien explica el modelo los datos (1 = perfecto)


# --------------------------------------------
# 12. VISUALIZACIÓN (TEST)
# --------------------------------------------

plt.scatter(X_test, y_test)
plt.plot(X_test, modelo.coef_ * X_test + modelo.intercept_)
plt.xlabel("Engine Size")
plt.ylabel("CO2 Emissions")
plt.title("Modelo evaluado (Test)")
plt.show()


# --------------------------------------------
# 13. SEGUNDO EXPERIMENTO
# --------------------------------------------
# Se prueba otra variable independiente:
# Consumo de combustible en lugar de tamaño del motor

X2 = cdf.FUELCONSUMPTION_COMB.to_numpy()

X_train, X_test, y_train, y_test = train_test_split(
    X2, y, test_size=0.2, random_state=42
)

modelo2 = LinearRegression()
modelo2.fit(X_train.reshape(-1, 1), y_train)

y_pred = modelo2.predict(X_test.reshape(-1, 1))

print("MSE usando consumo de combustible:", mean_squared_error(y_test, y_pred))


# --------------------------------------------
# CONCLUSIÓN
# --------------------------------------------
# Se comparan variables para ver cuál predice mejor las emisiones.
# Esto es clave en Machine Learning:
# elegir buenas variables mejora el modelo.