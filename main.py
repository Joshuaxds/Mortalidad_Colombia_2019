import streamlit as st
from modulos.cargar import cargar_datos
from vistas.principal import mostrar_app

st.set_page_config(
    page_title="Mortalidad en Colombia 2019",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

df, divipola, causas = cargar_datos()
mostrar_app(df, divipola, causas)
