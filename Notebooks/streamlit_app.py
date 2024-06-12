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

df = load_data("Dataset\df_limpio.csv")
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

Height_cm = st.sidebar.multiselect(
    "Altura en centímetros:",
    options=df['Height_(cm)'].unique(),
    default=df['Height_(cm)'].unique()
)

Weight_kg = st.sidebar.multiselect(
    "Peso en kilogramos:",
    options=df['Weight_(kg)'].unique(),
    default=df['Weight_(kg)'].unique()
)

BMI = st.sidebar.multiselect(
    "Índice de Masa Corporal:",
    options=df['BMI'].unique(),
    default=df['BMI'].unique()
)

# Usar DataFrame.eval para ejecutar la consulta de manera correcta
query_str = (
    f"General_Health == @General_Health and Checkup == @Checkup and Exercise == @Exercise and "
    f"Heart_Disease == @Heart_Disease and Skin_Cancer == @Skin_Cancer and Other_Cancer == @Other_Cancer and "
    f"Depression == @Depression and Diabetes == @Diabetes and Arthritis == @Arthritis and Sex == @Sex and "
    f"Age_Category == @Age_Category and `Height_(cm)` == @Height_cm and `Weight_(kg)` == @Weight_kg and BMI == @BMI"
)

df_selection = df[df.eval(query_str)]
df_selection.reset_index(inplace=True)

# ------- PÁGINA PRINCIPAL
st.title(':bar_chart: Gráficos')
st.markdown('##')

# TOP KPI'S
total_heart_disease = df['Heart_Disease'].sum()
average_fried_potato = round(df_selection['FriedPotato_Consumption'].mean(), 1)

PWHD = (df['Heart_Disease'] == 'Yes').sum()
WWHD = ((df['Heart_Disease'] == 'Yes') & (df['Sex'] == 'Female')).sum()
MWHD = ((df['Heart_Disease'] == 'Yes') & (df['Sex'] == 'Male')).sum()
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
## ------- RANGO DE EDADES CON ENFERMEDADES DEL CORAZÓN
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

st.plotly_chart(fig_heart_disease_group)
