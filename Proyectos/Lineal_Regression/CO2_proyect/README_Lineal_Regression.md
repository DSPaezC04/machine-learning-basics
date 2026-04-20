# 🚗 Predicción de Emisiones de CO2 con Regresión Lineal

## 📌 Descripción

Este proyecto implementa un modelo de **Machine Learning** utilizando **regresión lineal** para predecir las emisiones de CO2 de vehículos a partir de diferentes características como:

* Tamaño del motor (Engine Size)
* Número de cilindros (Cylinders)
* Consumo de combustible (Fuel Consumption)

El objetivo es entender cómo diferentes variables influyen en la contaminación generada por un vehículo.

---

## 🧠 Conceptos aplicados

* Regresión lineal
* División de datos (train/test)
* Evaluación de modelos
* Visualización de datos
* Selección de variables

---

## ⚙️ Tecnologías utilizadas

* Python
* NumPy
* Pandas
* Matplotlib
* Scikit-learn

---

## 📊 Dataset

Se utilizó un dataset público que contiene información sobre consumo de combustible y emisiones de CO2 de vehículos.

Fuente:
https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv

---

## 🔍 Flujo del proyecto

1. Carga de datos
2. Exploración del dataset
3. Selección de variables relevantes
4. Visualización de relaciones entre variables
5. Entrenamiento del modelo de regresión lineal
6. Evaluación del modelo
7. Comparación de diferentes variables predictoras

---

## 📈 Resultados

El modelo fue capaz de encontrar una relación entre las variables y las emisiones de CO2.

Se evaluó utilizando:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score

Estos indicadores permiten medir qué tan preciso es el modelo.

---

## 🧪 Experimentos

Se probaron diferentes variables independientes:

* Engine Size
* Fuel Consumption

Esto permite comparar cuál variable tiene mayor impacto en la predicción.

---

## 🚀 Cómo ejecutar el proyecto

1. Clonar el repositorio:

```bash
git clone https://github.com/tu-usuario/tu-repo.git
```

2. Instalar dependencias:

```bash
pip install numpy pandas matplotlib scikit-learn
```

3. Ejecutar el script:

```bash
python regresion_lineal.py
```

---

## 📌 Aprendizajes

* Cómo preparar datos para Machine Learning
* Cómo entrenar un modelo de regresión lineal
* Cómo evaluar el rendimiento de un modelo
* Importancia de la selección de variables

---

## 📎 Autor

**David Santiago Paez**

---

## ⭐ Próximos pasos

* Implementar regresión múltiple
* Probar modelos más avanzados
* Optimizar el modelo
* Crear visualizaciones más avanzadas
