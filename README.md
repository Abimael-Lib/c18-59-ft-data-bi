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

## Model Deployment
Para hacer deployable el modelo utilice las librias **streamlit**, **numpy** y **joblib**, esta ultima la utilice para guardar y cargar posteriormente el modelo.

## Dashboard
Para el dashboard utilice las librerias **pandas**, **streamlit** y **plootly.express**. Utilice el una copia del dataset original, salvo que esta tiene los valores de la columna "Age_Category" en formato string, mostrando explicitamente el rango etario de la persona, esto lo hice para que fuera mas claro para el usuario de la aplicación el poder utilizar el filtro de rango etario, luego para los filtros booleanos utilice 0 y 1 para especificar si se cumplia o no con la condicion escrita encima de los respectivos numero, para los filtros que recibian una cantidad considerable de valores decidi utilizar un *slider* para que sea mas eficiente el uso de los respectivos filtros, luego grafique un bar chart que mostraba una comparación entre los distintos rangos etario con el fin de ver a cuales rangos pertenecia la mayor cantidad de enfermedades del corazon, luego grafique un Pie Chart para ver de forma mas precisa como variaba la cantidad de personas por rango etario segun los ajustes que se hagan usando los filtros.


## Conclusiones