import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title = 'Probabilidad de padecer enfermedades del corazon',
    page_icon = ":bar_chart:",
    layout="wide"
)




@st.cache_data
def load_data(path: str):
    data = pd.read_csv(path)    
    return data

#uploaded_file = st.file_uploader("Sube un archivo")
#if uploaded_file is None:
#    st.info("Upload a file through a config", icon="ℹ️")
#    st.stop()


df = load_data("Dataset/CVD_cleaned.csv")
with st.expander("Muestra de los datos"):
    st.dataframe(df)



# ------- Sidebar
st.sidebar.header("Seleccióne los filtros:")

General_Health = st.sidebar.multiselect(
    "Salud en general:",
    options=df['General_Health'].unique(),
    default=df['General_Health'].unique()
)

Checkup = st.sidebar.multiselect(
    "Ultimo chequeo médico:",
    options=df['Checkup'].unique(),
    default=df['Checkup'].unique()
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


df_selection = df.query(
    "General_Health == @General_Health & Checkup == @Checkup & Sex == @Sex & Age_Category == @Age_Category"
)




# ------- PAGINA PRINCIPAL
st.title(':bar_chart: Graficos')
st.markdown('##')

# TOP KPI'S
total_heart_disease = df['Heart_Disease'].sum()
average_fried_potato = round(df_selection['FriedPotato_Consumption'], 1)

average_friedpotato_consumption = df['FriedPotato_Consumption'].apply(lambda x: ':🥔:' * int(round(x, 0)))


left_column, middle_column, right_column = st.columns(3)










