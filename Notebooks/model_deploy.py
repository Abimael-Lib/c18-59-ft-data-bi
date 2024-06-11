import streamlit as st
import joblib
import numpy as np

# Ruta al archivo del modelo
model_path = 'C:/Users/Abi/Desktop/c18-59-ft-data-bi/Notebooks/logistic_regression_model.pkl'

# Cargar el modelo preentrenado
try:
    model = joblib.load(model_path)
    st.success("Modelo cargado exitosamente.")
except FileNotFoundError:
    st.error(f"Archivo no encontrado: {model_path}")
    st.stop()

# Lista de características esperadas por el modelo (sin 'Heart_Disease')
model_features = [
    'General_Health', 'Checkup', 'Exercise', 'Skin_Cancer',
    'Other_Cancer', 'Depression', 'Diabetes', 'Arthritis', 'Sex',
    'Age_Category', 'Height_(cm)', 'Weight_(kg)', 'BMI', 'Smoking_History',
    'Alcohol_Consumption', 'Fruit_Consumption',
    'Green_Vegetables_Consumption', 'FriedPotato_Consumption'
]

# Características que solo deben aceptar 0 y 1
binary_features = [
    'Exercise', 'Skin_Cancer', 'Other_Cancer',
    'Depression', 'Arthritis', 'Sex', 'Smoking_History'
]

# Diccionario para almacenar los valores de las características
feature_values = {}

# Definir valores mínimos y máximos para cada característica
min_max_values = {
    'General_Health': (0, 4),
    'Checkup': (0, 4),
    'Exercise': (0, 1),
    'Skin_Cancer': (0, 1),
    'Other_Cancer': (0, 1),
    'Depression': (0, 1),
    'Diabetes': (0, 3),
    'Arthritis': (0, 1),
    'Sex': (0, 1),
    'Age_Category': (0, 12),
    'Height_(cm)': (91.0, 241.0),
    'Weight_(kg)': (24.95, 293.02),
    'BMI': (12.02, 99.33),
    'Smoking_History': (0, 1),
    'Alcohol_Consumption': (0.0, 30.0),
    'Fruit_Consumption': (0.0, 120.0),
    'Green_Vegetables_Consumption': (0.0, 128.0),
    'FriedPotato_Consumption': (0.0, 128.0)
}

# Crear una entrada para cada característica (sin 'Heart_Disease')
# Crear una entrada para cada característica (sin 'Heart_Disease')
for feature in model_features:  # Usar las características esperadas por el modelo
    if feature in binary_features:
        feature_values[feature] = st.selectbox(f'Característica: {feature}', options=[0, 1])
    else:
        min_val, max_val = min_max_values[feature]
        min_val = float(min_val)  # Convertir mínimo a flotante
        max_val = float(max_val)  # Convertir máximo a flotante
        feature_values[feature] = st.number_input(f'Característica: {feature}', min_value=min_val, max_value=max_val, value=(min_val + max_val) / 2)




# Botón para hacer predicciones
if st.button("Predecir"):
    # Convertir los valores de las características en una matriz de numpy
    input_values = np.array([feature_values[feature] for feature in model_features]).reshape(1, -1)  # Usar las características esperadas por el modelo

    # Hacer predicción
    prediction = model.predict(input_values)
    prediction_proba = model.predict_proba(input_values)

    # Mostrar el resultado de la predicción
    st.write(f"Predicción: {prediction[0]}")
    st.write(f"Probabilidades: {prediction_proba}")

# Para ejecutar la aplicación, usa el comando en la terminal:
# streamlit run model_deploy.py

