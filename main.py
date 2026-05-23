import streamlit as st

from modulos.cargar import cargar_datos
from vistas.diseño import configurar_diseño
from vistas.principal import mostrar_app

st.set_page_config(
    page_title="Mortalidad en Colombia 2019",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

df, divipola, causas = cargar_datos()

configurar_diseño(df)

mostrar_app(df, divipola, causas)
