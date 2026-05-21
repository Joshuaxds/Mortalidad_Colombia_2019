import streamlit as st
from vistas.Graficolineas import grafico_lineas
from vistas.Mapa import mapa_departamentos
from vistas.Graficobarras import ciudades_mas_violentas
from vistas.Causasmuertes import top_causas
from vistas.Graficobaapiladas import muertes_sexo_departamento
from vistas.Edades import muertes_por_edad
from vistas.Graficocircular import ciudades_menor_mortalidad

def mostrar_app(df, divipola, causas):
    st.markdown("""
    <style>
    body {
        background-color: #F5F5F5;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h1 style='text-align: center; color: #003366;'>
    📊 Análisis de Mortalidad en Colombia - 2019
    </h1>
    """, unsafe_allow_html=True)

    st.sidebar.markdown("## 📌 Navegación")

    opcion = st.sidebar.radio(
        "Secciones:",
        [
            "🏠 Inicio",
            "📈 Total de muertes por mes",
            "🗺️ Total de muertes por departamento",
            "🔫 Ciudades más violentas",
            "☠️ Causas",
            "⚖️ Sexo por departamento",
            "👶 Edad",
            "🥧 Ciudades menor mortalidad"
        ]
    )

    sexo = st.sidebar.selectbox(
        "Selecciona el sexo",
        ["Todos", "Masculino", "Femenino"]
    )

    if sexo == "Masculino":
        df_filtrado = df[df["SEXO"] == 1]
    elif sexo == "Femenino":
        df_filtrado = df[df["SEXO"] == 2]
    else:
        df_filtrado = df

    if opcion == "🏠 Inicio":
        st.subheader("📌 Descripción")
        st.write("Este aplicativo presenta un análisis de la mortalidad en Colombia en 2019, utilizando datos oficiales.")
        col1, col2, col3 = st.columns(3)
        col1.metric("📊 Registros", len(df))
        col2.metric("📅 Año", 2019)
        col3.metric("📍 Cobertura", "Nacional")
        st.info("Fuente: DANE")

    elif opcion == "📈 Total de muertes por mes":
        fig = grafico_lineas(df_filtrado)
        st.plotly_chart(fig, use_container_width=True)

    elif opcion == "🗺️ Total de muertes por departamento":
        fig = mapa_departamentos(df_filtrado, divipola)
        st.plotly_chart(fig, use_container_width=True)

    elif opcion == "🔫 Ciudades más violentas":
        fig = ciudades_mas_violentas(df_filtrado, divipola)
        st.plotly_chart(fig, use_container_width=True)

    elif opcion == "☠️ Causas":
        fig = top_causas(df_filtrado, causas)
        st.plotly_chart(fig, use_container_width=True)

    elif opcion == "⚖️ Sexo por departamento":
        fig = muertes_sexo_departamento(df_filtrado, divipola)
        st.plotly_chart(fig, use_container_width=True)

    elif opcion == "👶 Edad":
        fig = muertes_por_edad(df_filtrado)
        st.plotly_chart(fig, use_container_width=True)

    elif opcion == "🥧 Ciudades menor mortalidad":
        fig = ciudades_menor_mortalidad(df_filtrado, divipola)
        st.plotly_chart(fig, use_container_width=True)