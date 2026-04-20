# -----------------------------------
# DAVID SANTIAGO PAEZ C
# 18/042026
# -----------------------------------

# ============================================
# FUNDAMENTOS DE INTELIGENCIA ARTIFICIAL (IA)
# ============================================

# IA vs Machine Learning
# IA: simula procesos cognitivos humanos
# ML: usa algoritmos para aprender de datos (requiere feature engineering)

# --------------------------------------------
# TIPOS DE MACHINE LEARNING
# --------------------------------------------

# 1. Supervisado:
# - Usa datos etiquetados
# - Ej: clasificación, regresión

# 2. No supervisado:
# - No hay etiquetas
# - Encuentra patrones
# - Ej: clustering

# 3. Semi-supervisado:
# - Pocos datos etiquetados + muchos sin etiquetar

# --------------------------------------------
# TIPOS DE PROBLEMAS EN ML
# --------------------------------------------

# Clasificación → categorías (spam / no spam)
# Regresión → valores continuos (precio casa)
# Clustering → agrupar datos similares
# Detección de anomalías → detectar casos raros (fraude)

# --------------------------------------------
# FACTORES PARA ELEGIR MODELO
# --------------------------------------------

# - Tipo de problema
# - Cantidad y tipo de datos
# - Recursos disponibles
# - Resultado esperado

# --------------------------------------------
# PIPELINE DE MACHINE LEARNING
# --------------------------------------------

# 1. Preprocesamiento de datos
# 2. Entrenamiento del modelo
# 3. Evaluación
# 4. Optimización
# 5. Despliegue

# --------------------------------------------
# LENGUAJES USADOS EN ML
# --------------------------------------------

# Python → principal (IA, ML, Deep Learning)
# R → estadística
# Otros: Julia, Scala, Java, JavaScript

# --------------------------------------------
# LIBRERÍAS IMPORTANTES EN PYTHON
# --------------------------------------------

# NumPy → operaciones numéricas
# Pandas → manejo de datos
# SciPy → computación científica
# Scikit-learn → modelos de ML

# --------------------------------------------
# VISUALIZACIÓN DE DATOS
# --------------------------------------------

# Matplotlib → gráficos básicos
# Seaborn → gráficos más avanzados
# ggplot2 → (R)
# Tableau → dashboards interactivos

# --------------------------------------------
# DEEP LEARNING
# --------------------------------------------

# Frameworks:
# TensorFlow
# Keras
# PyTorch

# Usos:
# - Visión por computador
# - Procesamiento de lenguaje natural (NLP)

# --------------------------------------------
# IA APLICADA
# --------------------------------------------

# Computer Vision:
# - detección de objetos
# - reconocimiento facial

# NLP:
# - análisis de texto
# - sentimientos

# --------------------------------------------
# IA GENERATIVA
# --------------------------------------------

# Genera contenido:
# - texto
# - imágenes
# - música

# --------------------------------------------
# EJEMPLO SIMPLE EN PYTHON
# --------------------------------------------

# Clasificación básica (simulación)

def clasificar_nota(nota):
    if nota >= 3:
        return "Aprobado"
    else:
        return "Reprobado"

notas = [2.5, 3.2, 4.0, 1.8]

resultados = [clasificar_nota(n) for n in notas]

print(resultados)

def clacificar_numeros(num):
    if num >= 10:
        return "Alto"
    else:
        return "bajo"

nums = [4,15,12,7,11,30,2]

results = [clacificar_numeros(n) for n in nums]

print (results)