import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title='Probabilidad de padecer enfermedades del corazón',
    page_icon=":bar_chart:",
    layout="wide"
)

@st.cache_data
def load_data(path: str):
    data = pd.read_csv(path)
    return data

df = load_data("Dataset/df_limpio.csv")
with st.expander("Muestra de los datos"):
    st.dataframe(df)

# ------- Sidebar
st.sidebar.header("Selección de filtros:")

General_Health = st.sidebar.multiselect(
    "Salud en general:",
    options=df['General_Health'].unique(),
    default=df['General_Health'].unique()
)

Checkup = st.sidebar.multiselect(
    "Último chequeo médico:",
    options=df['Checkup'].unique(),
    default=df['Checkup'].unique()
)

Exercise = st.sidebar.multiselect(
    "Hace ejercicio:",
    options=df['Exercise'].unique(),
    default=df['Exercise'].unique()
)

Heart_Disease = st.sidebar.multiselect(
    "Tiene enfermedades del corazón:",
    options=df['Heart_Disease'].unique(),
    default=df['Heart_Disease'].unique()
)

Skin_Cancer = st.sidebar.multiselect(
    "Tiene cáncer de piel:",
    options=df['Skin_Cancer'].unique(),
    default=df['Skin_Cancer'].unique()
)

Other_Cancer = st.sidebar.multiselect(
    "Tiene otro tipo de cáncer:",
    options=df['Other_Cancer'].unique(),
    default=df['Other_Cancer'].unique()
)

Depression = st.sidebar.multiselect(
    "Tiene depresión:",
    options=df['Depression'].unique(),
    default=df['Depression'].unique()
)

Diabetes = st.sidebar.multiselect(
    "Tiene diabetes:",
    options=df['Diabetes'].unique(),
    default=df['Diabetes'].unique()
)

Arthritis = st.sidebar.multiselect(
    "Tiene artritis:",
    options=df['Arthritis'].unique(),
    default=df['Arthritis'].unique()
)

Sex = st.sidebar.multiselect(
    "Sexo:",
    options=df['Sex'].unique(),
    default=df['Sex'].unique()
)

Age_Category = st.sidebar.multiselect(
    "Rango etario:",
    options=df['Age_Category'].unique(),
    default=df['Age_Category'].unique()
)

# Cambiar a st.slider para la altura en centímetros
min_height = int(df['Height_(cm)'].min())
max_height = int(df['Height_(cm)'].max())
Height_cm = st.sidebar.slider(
    "Altura en centímetros:",
    min_value=min_height,
    max_value=max_height,
    value=(min_height, max_height)
)

# Cambiar a st.slider para el peso en kilogramos
min_weight = int(df['Weight_(kg)'].min())
max_weight = int(df['Weight_(kg)'].max())
Weight_kg = st.sidebar.slider(
    "Peso en kilogramos:",
    min_value=min_weight,
    max_value=max_weight,
    value=(min_weight, max_weight)
)

# Cambiar a st.slider para el índice de masa corporal
min_bmi = int(df['BMI'].min())
max_bmi = int(df['BMI'].max())
BMI = st.sidebar.slider(
    "Índice de Masa Corporal:",
    min_value=min_bmi,
    max_value=max_bmi,
    value=(min_bmi, max_bmi)
)

# Usar DataFrame.eval para ejecutar la consulta de manera correcta
query_str = (
    f"General_Health == @General_Health and Checkup == @Checkup and Exercise == @Exercise and "
    f"Heart_Disease == @Heart_Disease and Skin_Cancer == @Skin_Cancer and Other_Cancer == @Other_Cancer and "
    f"Depression == @Depression and Diabetes == @Diabetes and Arthritis == @Arthritis and Sex == @Sex and "
    f"Age_Category == @Age_Category and `Height_(cm)` >= {Height_cm[0]} and `Height_(cm)` <= {Height_cm[1]} and "
    f"`Weight_(kg)` >= {Weight_kg[0]} and `Weight_(kg)` <= {Weight_kg[1]} and `BMI` >= {BMI[0]} and `BMI` <= {BMI[1]}"
)

df_selection = df[df.eval(query_str)]



# ------- PÁGINA PRINCIPAL
st.title(':bar_chart: Gráficos')
st.markdown('##')

# TOP KPI'S
total_heart_disease = df['Heart_Disease'].sum()
average_fried_potato = round(df_selection['FriedPotato_Consumption'].mean(), 1)

PWHD = (df['Heart_Disease'] == 1).sum()
WWHD = ((df['Heart_Disease'] == 1) & (df['Sex'] == 0)).sum()
MWHD = ((df['Heart_Disease'] == 1) & (df['Sex'] == 1)).sum()
left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader('Personas con enfermedades del corazón:')
    st.subheader(PWHD)

with middle_column:
    st.subheader('Mujeres con enfermedades del corazón:')
    st.subheader(WWHD)

with right_column:
    st.subheader('Hombres con enfermedades del corazón:')
    st.subheader(MWHD)

st.markdown("---")

# ------- GRÁFICOS
## ------- BAR CHART
## ------- ENFERMEDADES DEL CORAZON POR RANGO ETARIO
heart_disease_per_age_category = (
    df_selection.groupby(by=['Age_Category']).sum(numeric_only=True)[['Heart_Disease']].sort_values(by='Heart_Disease')
)

fig_heart_disease_group = px.bar(
    heart_disease_per_age_category,
    x="Heart_Disease",
    y=heart_disease_per_age_category.index,
    orientation='h',
    title='<b>Heart Disease per Age Group</b>',
    color_discrete_sequence=['#0083B8'] * len(heart_disease_per_age_category),
    template='plotly_white',
)

fig_heart_disease_group.update_layout(
    plot_bgcolor="rgba(0, 0, 0, 0)",
    xaxis=(dict(showgrid=False))
)

st.plotly_chart(fig_heart_disease_group)

# ------- PIE CHART

# Contar la cantidad de personas en cada categoría de edad después de aplicar los filtros
age_category_counts_filtered = df_selection['Age_Category'].value_counts()

# Crear el gráfico de pastel
fig_pie_chart_age_filtered = px.pie(
    values=age_category_counts_filtered.values,
    names=age_category_counts_filtered.index,
    title='Distribución por categoría de edad (Filtrada)',
)

# Mostrar el gráfico de pastel
st.plotly_chart(fig_pie_chart_age_filtered)
