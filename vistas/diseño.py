import streamlit as st
from modulos.cargar import cargar_datos

df, divipola, causas = cargar_datos()
def configurar_diseño(df):

 st.markdown("""
<style>
/* Fondo general */
.stApp {
    background: linear-gradient(180deg, #F5F7FA 0%, #EEF2F7 100%);
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #8E0038;
}

/* Texto del sidebar */
[data-testid="stSidebar"] * {
    color: white;
}

/* Título principal */
.hero-box {
    background: linear-gradient(90deg, #B6004C 0%, #8E0038 100%);
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.12);
    margin-bottom: 20px;
}

.hero-title {
    color: white;
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    margin: 0;
}

.hero-subtitle {
    color: white;
    text-align: center;
    font-size: 16px;
    margin-top: 8px;
    margin-bottom: 0;
}

/* Tarjetas visuales */
.card {
    background: white;
    padding: 18px;
    border-radius: 16px;
    box-shadow: 0 4px 18px rgba(0,0,0,0.08);
    border: 1px solid #E8ECF2;
}

/* Métricas */
[data-testid="stMetric"] {
    background: white;
    border-radius: 16px;
    padding: 14px;
    box-shadow: 0 4px 18px rgba(0,0,0,0.06);
    border: 1px solid #E8ECF2;
}

/* Texto general */
h1, h2, h3, h4 {
    color: #1F2D3D;
}

p, span, div {
    color: #2E3A4A;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-box">
    <h1 class="hero-title">📊 Mortalidad en Colombia 2019</h1>
    <p class="hero-subtitle">Análisis estadístico basado en datos oficiales del DANE</p>
</div>
""", unsafe_allow_html=True)

