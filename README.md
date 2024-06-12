# Prediccion de enfermedades del corazon

## Datos
Para este proyecto utilicé un dataset de kaggle.

## Feature Engineer
En el proceso de 'Feature Engineer' solo cambie las variables categoricas binarias(es decir las que solo aceptaban 2 valores) en numericas, es decir 0/1.

## Model definition
Probe los siguientes modelos de clasificación:
- Regresión logistica
- Arbol de Desición
- Random Forest
- Gradient Boosting Clasiffier
- K-Nearest Neighbors (KNN)

Al utilizar la metrica de **accuracy** y **mean_squared_error**, me decante por quedarme con el modelo de **logistinc regression** me dio una **accuracy** de 0.9192339447313465 y un **mean_squared_error** de 0.08076605526865357.

### Model Deployment
Para hacer deployable el modelo utilice las librias **streamlit**, **numpy** y **joblib**, esta ultima la utilice para cargar el modelo.


## Dashboard
Para el dashboard utilice las librerias **pandas**, **streamlit** y **plootly.express**.


## Conclusiones