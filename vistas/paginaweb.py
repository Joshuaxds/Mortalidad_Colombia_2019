import streamlit as st
from pathlib import Path
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

    st.sidebar.markdown("##  Navegación")

    opcion = st.sidebar.radio(
        "Secciones:",
        [
            " Inicio",
            " Muertes por mes",
            " Muertes por departamento",
            " Ciudades más violentas",
            " Causas",
            " Sexo por departamento",
            " Edad",
            " Ciudades menor mortalidad"
            " datos"
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

    if opcion == " Inicio":
        st.markdown(
            """
            <div style="display: flex; justify-content: center; margin-bottom: 20px;">
                <div style="background-color: #ffe6e6; border: 2px solid #ff4d4d; border-radius: 14px; padding: 18px 28px; max-width: 900px; width: 100%;">
                    <h1 style="text-align: center; color: #b30000; margin: 0;">Mortalidad en Colombia</h1>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.subheader(" Descripción")
        st.write("Esta aplicación web presenta un análisis estadístico de la mortalidad en Colombia utilizando datos oficiales del DANE correspondientes al año 2019. La plataforma permite explorar información sobre muertes por mes, departamento, ciudades con mayor y menor mortalidad, causas de fallecimiento, sexo y edad. Además, incluye una interfaz interactiva con navegación lateral y filtros para facilitar la visualización y comprensión de los datos a nivel naciona")
        st.write("")
        st.subheader("Fundamento del estudio")
        st.write("El fundamento de este estudio se basa en el análisis de datos oficiales de mortalidad en Colombia obtenidos a partir de las bases de datos del DANE, incluyendo registros de defunciones no fetales, códigos de causas de muerte y la división político-administrativa del país (DIVIPOLA). A través de estos archivos en formato Excel, se realizó un proceso de organización, limpieza y visualización de la información para identificar patrones de mortalidad según variables como sexo, edad, departamento, ciudad y causas de fallecimiento durante el año 2019. El objetivo principal es facilitar la interpretación de los datos estadísticos mediante gráficos e indicadores interactivos que permitan comprender mejor el comportamiento de la mortalidad a nivel nacional.")
        st.write("")
        st.write("---------------------------------------------------------------------------------------------------------------------------------------------------")
        
        col1, col2, col3 = st.columns(3)
        col1.metric(" Registros", len(df))
        col2.metric(" Año", 2019)
        col3.metric(" Cobertura", "Nacional")

        logo_path = Path(__file__).resolve().parents[1] / "Imagenes" / "dane.png"
        if logo_path.exists():
            st.image(str(logo_path), width=1700)
        else:
            st.write("Logo DANE no disponible")

    elif opcion == " Muertes por mes":
        st.markdown(
            """
            <div style="display: flex; justify-content: center; margin-bottom: 20px;">
                <div style="background-color: #ffe6e6; border: 2px solid #ff4d4d; border-radius: 14px; padding: 18px 28px; max-width: 900px; width: 100%;">
                    <h1 style="text-align: center; color: #b30000; margin: 0;">Muertes por mes</h1>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("Este gráfico muestra la evolución de las muertes a lo largo de los meses del año 2019. Visualiza las tendencias mensuales y permite identificar períodos con mayor o menor mortalidad.")
        fig = grafico_lineas(df_filtrado)
        st.plotly_chart(fig, use_container_width=True)
        st.write("El fundamento de este estudio se basa en el análisis de datos oficiales de mortalidad en Colombia obtenidos a partir de las bases de datos del DANE, incluyendo registros de defunciones no fetales, códigos de causas de muerte y la división político-administrativa del país (DIVIPOLA). A través de estos archivos en formato Excel, se realizó un proceso de organización, limpieza y visualización de la información para identificar patrones de mortalidad según variables como sexo, edad, departamento, ciudad y causas de fallecimiento durante el año 2019. El objetivo principal es facilitar la interpretación de los datos estadísticos mediante gráficos e indicadores interactivos que permitan comprender mejor el comportamiento de la mortalidad a nivel nacional.")
        st.write("El fundamento de este estudio se basa en el análisis de datos oficiales de mortalidad en Colombia obtenidos a partir de las bases de datos del DANE, incluyendo registros de defunciones no fetales, códigos de causas de muerte y la división político-administrativa del país (DIVIPOLA). A través de estos archivos en formato Excel, se realizó un proceso de organización, limpieza y visualización de la información para identificar patrones de mortalidad según variables como sexo, edad, departamento, ciudad y causas de fallecimiento durante el año 2019. El objetivo principal es facilitar la interpretación de los datos estadísticos mediante gráficos e indicadores interactivos que permitan comprender mejor el comportamiento de la mortalidad a nivel nacional.")
        st.write("")
        st.write("---------------------------------------------------------------------------------------------------------------------------------------------------")
        logo_path = Path(__file__).resolve().parents[1] / "Imagenes" / "dane.png"
        if logo_path.exists():
            st.image(str(logo_path), width=1700)
        else:
            st.write("Logo DANE no disponible")
    elif opcion == " Muertes por departamento":
        st.markdown(
            """
            <div style="display: flex; justify-content: center; margin-bottom: 20px;">
                <div style="background-color: #ffe6e6; border: 2px solid #ff4d4d; border-radius: 14px; padding: 18px 28px; max-width: 900px; width: 100%;">
                    <h1 style="text-align: center; color: #b30000; margin: 0;">Muertes por departamento</h1>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("Este mapa interactivo muestra la distribución geográfica de la mortalidad en cada departamento de Colombia. Los colores indican la intensidad de las muertes por región.")
        fig = mapa_departamentos(df_filtrado, divipola)
        st.plotly_chart(fig, use_container_width=True)
        st.write("El fundamento de este estudio se basa en el análisis de datos oficiales de mortalidad en Colombia obtenidos a partir de las bases de datos del DANE, incluyendo registros de defunciones no fetales, códigos de causas de muerte y la división político-administrativa del país (DIVIPOLA). A través de estos archivos en formato Excel, se realizó un proceso de organización, limpieza y visualización de la información para identificar patrones de mortalidad según variables como sexo, edad, departamento, ciudad y causas de fallecimiento durante el año 2019. El objetivo principal es facilitar la interpretación de los datos estadísticos mediante gráficos e indicadores interactivos que permitan comprender mejor el comportamiento de la mortalidad a nivel nacional.")
        st.write("El fundamento de este estudio se basa en el análisis de datos oficiales de mortalidad en Colombia obtenidos a partir de las bases de datos del DANE, incluyendo registros de defunciones no fetales, códigos de causas de muerte y la división político-administrativa del país (DIVIPOLA). A través de estos archivos en formato Excel, se realizó un proceso de organización, limpieza y visualización de la información para identificar patrones de mortalidad según variables como sexo, edad, departamento, ciudad y causas de fallecimiento durante el año 2019. El objetivo principal es facilitar la interpretación de los datos estadísticos mediante gráficos e indicadores interactivos que permitan comprender mejor el comportamiento de la mortalidad a nivel nacional.")
        st.write("")
        st.write("---------------------------------------------------------------------------------------------------------------------------------------------------")
        logo_path = Path(__file__).resolve().parents[1] / "Imagenes" / "dane.png"
        if logo_path.exists():
            st.image(str(logo_path), width=1700)
        else:
            st.write("Logo DANE no disponible")
    elif opcion == " Ciudades más violentas":
        st.markdown(
            """
            <div style="display: flex; justify-content: center; margin-bottom: 20px;">
                <div style="background-color: #ffe6e6; border: 2px solid #ff4d4d; border-radius: 14px; padding: 18px 28px; max-width: 900px; width: 100%;">
                    <h1 style="text-align: center; color: #b30000; margin: 0;">Ciudades mas violentas</h1>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("Este gráfico de barras ordena las ciudades con mayor número de fallecidos. Permite identificar qué ciudades tienen los índices de mortalidad más altos.")
        fig = ciudades_mas_violentas(df_filtrado, divipola)
        st.plotly_chart(fig, use_container_width=True)
        st.write("El fundamento de este estudio se basa en el análisis de datos oficiales de mortalidad en Colombia obtenidos a partir de las bases de datos del DANE, incluyendo registros de defunciones no fetales, códigos de causas de muerte y la división político-administrativa del país (DIVIPOLA). A través de estos archivos en formato Excel, se realizó un proceso de organización, limpieza y visualización de la información para identificar patrones de mortalidad según variables como sexo, edad, departamento, ciudad y causas de fallecimiento durante el año 2019. El objetivo principal es facilitar la interpretación de los datos estadísticos mediante gráficos e indicadores interactivos que permitan comprender mejor el comportamiento de la mortalidad a nivel nacional.") 
        st.write("El fundamento de este estudio se basa en el análisis de datos oficiales de mortalidad en Colombia obtenidos a partir de las bases de datos del DANE, incluyendo registros de defunciones no fetales, códigos de causas de muerte y la división político-administrativa del país (DIVIPOLA). A través de estos archivos en formato Excel, se realizó un proceso de organización, limpieza y visualización de la información para identificar patrones de mortalidad según variables como sexo, edad, departamento, ciudad y causas de fallecimiento durante el año 2019. El objetivo principal es facilitar la interpretación de los datos estadísticos mediante gráficos e indicadores interactivos que permitan comprender mejor el comportamiento de la mortalidad a nivel nacional.")
        st.write("")
        st.write("---------------------------------------------------------------------------------------------------------------------------------------------------")
        logo_path = Path(__file__).resolve().parents[1] / "Imagenes" / "dane.png"
        if logo_path.exists():
            st.image(str(logo_path), width=1700)
        else:
            st.write("Logo DANE no disponible")
    elif opcion == " Causas":
        st.markdown(
            """
            <div style="display: flex; justify-content: center; margin-bottom: 20px;">
                <div style="background-color: #ffe6e6; border: 2px solid #ff4d4d; border-radius: 14px; padding: 18px 28px; max-width: 900px; width: 100%;">
                    <h1 style="text-align: center; color: #b30000; margin: 0;">Causas</h1>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("Este gráfico presenta las principales causas de mortalidad en Colombia. Muestra qué enfermedades o factores son responsables de la mayoría de fallecidos.")
        fig = top_causas(df_filtrado, causas)
        st.plotly_chart(fig, use_container_width=True)
        st.write("El fundamento de este estudio se basa en el análisis de datos oficiales de mortalidad en Colombia obtenidos a partir de las bases de datos del DANE, incluyendo registros de defunciones no fetales, códigos de causas de muerte y la división político-administrativa del país (DIVIPOLA). A través de estos archivos en formato Excel, se realizó un proceso de organización, limpieza y visualización de la información para identificar patrones de mortalidad según variables como sexo, edad, departamento, ciudad y causas de fallecimiento durante el año 2019. El objetivo principal es facilitar la interpretación de los datos estadísticos mediante gráficos e indicadores interactivos que permitan comprender mejor el comportamiento de la mortalidad a nivel nacional.") 
        st.write("El fundamento de este estudio se basa en el análisis de datos oficiales de mortalidad en Colombia obtenidos a partir de las bases de datos del DANE, incluyendo registros de defunciones no fetales, códigos de causas de muerte y la división político-administrativa del país (DIVIPOLA). A través de estos archivos en formato Excel, se realizó un proceso de organización, limpieza y visualización de la información para identificar patrones de mortalidad según variables como sexo, edad, departamento, ciudad y causas de fallecimiento durante el año 2019. El objetivo principal es facilitar la interpretación de los datos estadísticos mediante gráficos e indicadores interactivos que permitan comprender mejor el comportamiento de la mortalidad a nivel nacional.")
        st.write("")
        st.write("---------------------------------------------------------------------------------------------------------------------------------------------------")
        logo_path = Path(__file__).resolve().parents[1] / "Imagenes" / "dane.png"
        if logo_path.exists():
            st.image(str(logo_path), width=1700)
        else:
            st.write("Logo DANE no disponible")
    elif opcion == " Sexo por departamento":
        st.markdown(
            """
            <div style="display: flex; justify-content: center; margin-bottom: 20px;">
                <div style="background-color: #ffe6e6; border: 2px solid #ff4d4d; border-radius: 14px; padding: 18px 28px; max-width: 900px; width: 100%;">
                    <h1 style="text-align: center; color: #b30000; margin: 0;">Sexo por departamento</h1>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("Este gráfico de barras apiladas muestra la distribución de muertes por sexo (masculino y femenino) en cada departamento, permitiendo comparar patrones de mortalidad entre géneros por región.")
        fig = muertes_sexo_departamento(df_filtrado, divipola)
        st.plotly_chart(fig, use_container_width=True)
        st.write("El fundamento de este estudio se basa en el análisis de datos oficiales de mortalidad en Colombia obtenidos a partir de las bases de datos del DANE, incluyendo registros de defunciones no fetales, códigos de causas de muerte y la división político-administrativa del país (DIVIPOLA). A través de estos archivos en formato Excel, se realizó un proceso de organización, limpieza y visualización de la información para identificar patrones de mortalidad según variables como sexo, edad, departamento, ciudad y causas de fallecimiento durante el año 2019. El objetivo principal es facilitar la interpretación de los datos estadísticos mediante gráficos e indicadores interactivos que permitan comprender mejor el comportamiento de la mortalidad a nivel nacional.") 
        st.write("El fundamento de este estudio se basa en el análisis de datos oficiales de mortalidad en Colombia obtenidos a partir de las bases de datos del DANE, incluyendo registros de defunciones no fetales, códigos de causas de muerte y la división político-administrativa del país (DIVIPOLA). A través de estos archivos en formato Excel, se realizó un proceso de organización, limpieza y visualización de la información para identificar patrones de mortalidad según variables como sexo, edad, departamento, ciudad y causas de fallecimiento durante el año 2019. El objetivo principal es facilitar la interpretación de los datos estadísticos mediante gráficos e indicadores interactivos que permitan comprender mejor el comportamiento de la mortalidad a nivel nacional.")
        st.write("")
        st.write("---------------------------------------------------------------------------------------------------------------------------------------------------")
        logo_path = Path(__file__).resolve().parents[1] / "Imagenes" / "dane.png"
        if logo_path.exists():
            st.image(str(logo_path), width=1700)
        else:
            st.write("Logo DANE no disponible")
    elif opcion == " Edad":
        st.markdown(
            """
            <div style="display: flex; justify-content: center; margin-bottom: 20px;">
                <div style="background-color: #ffe6e6; border: 2px solid #ff4d4d; border-radius: 14px; padding: 18px 28px; max-width: 900px; width: 100%;">
                    <h1 style="text-align: center; color: #b30000; margin: 0;">Edad</h1>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("Este gráfico muestra la distribución de muertes por grupos de edad. Permite visualizar qué rangos de edad tienen mayor mortalidad y cómo se distribuye en la población.")
        fig = muertes_por_edad(df_filtrado)
        st.plotly_chart(fig, use_container_width=True)
        st.write("El fundamento de este estudio se basa en el análisis de datos oficiales de mortalidad en Colombia obtenidos a partir de las bases de datos del DANE, incluyendo registros de defunciones no fetales, códigos de causas de muerte y la división político-administrativa del país (DIVIPOLA). A través de estos archivos en formato Excel, se realizó un proceso de organización, limpieza y visualización de la información para identificar patrones de mortalidad según variables como sexo, edad, departamento, ciudad y causas de fallecimiento durante el año 2019. El objetivo principal es facilitar la interpretación de los datos estadísticos mediante gráficos e indicadores interactivos que permitan comprender mejor el comportamiento de la mortalidad a nivel nacional.")
        st.write("El fundamento de este estudio se basa en el análisis de datos oficiales de mortalidad en Colombia obtenidos a partir de las bases de datos del DANE, incluyendo registros de defunciones no fetales, códigos de causas de muerte y la división político-administrativa del país (DIVIPOLA). A través de estos archivos en formato Excel, se realizó un proceso de organización, limpieza y visualización de la información para identificar patrones de mortalidad según variables como sexo, edad, departamento, ciudad y causas de fallecimiento durante el año 2019. El objetivo principal es facilitar la interpretación de los datos estadísticos mediante gráficos e indicadores interactivos que permitan comprender mejor el comportamiento de la mortalidad a nivel nacional.")
        st.write("")
        st.write("---------------------------------------------------------------------------------------------------------------------------------------------------")
        logo_path = Path(__file__).resolve().parents[1] / "Imagenes" / "dane.png"
        if logo_path.exists():
            st.image(str(logo_path), width=1700)
        else:
            st.write("Logo DANE no disponible")
    elif opcion == " Ciudades menor mortalidad":
        st.markdown(
            """
            <div style="display: flex; justify-content: center; margin-bottom: 20px;">
                <div style="background-color: #ffe6e6; border: 2px solid #ff4d4d; border-radius: 14px; padding: 18px 28px; max-width: 900px; width: 100%;">
                    <h1 style="text-align: center; color: #b30000; margin: 0;">Ciudades menor mortalidad</h1>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("Este gráfico circular muestra las ciudades con los menores índices de mortalidad. Permite identificar qué ciudades tienen mejores indicadores de salud y menor número de fallecidos.")
        fig = ciudades_menor_mortalidad(df_filtrado, divipola)
        st.plotly_chart(fig, use_container_width=True)
        st.write("El fundamento de este estudio se basa en el análisis de datos oficiales de mortalidad en Colombia obtenidos a partir de las bases de datos del DANE, incluyendo registros de defunciones no fetales, códigos de causas de muerte y la división político-administrativa del país (DIVIPOLA). A través de estos archivos en formato Excel, se realizó un proceso de organización, limpieza y visualización de la información para identificar patrones de mortalidad según variables como sexo, edad, departamento, ciudad y causas de fallecimiento durante el año 2019. El objetivo principal es facilitar la interpretación de los datos estadísticos mediante gráficos e indicadores interactivos que permitan comprender mejor el comportamiento de la mortalidad a nivel nacional.") 
        st.write("El fundamento de este estudio se basa en el análisis de datos oficiales de mortalidad en Colombia obtenidos a partir de las bases de datos del DANE, incluyendo registros de defunciones no fetales, códigos de causas de muerte y la división político-administrativa del país (DIVIPOLA). A través de estos archivos en formato Excel, se realizó un proceso de organización, limpieza y visualización de la información para identificar patrones de mortalidad según variables como sexo, edad, departamento, ciudad y causas de fallecimiento durante el año 2019. El objetivo principal es facilitar la interpretación de los datos estadísticos mediante gráficos e indicadores interactivos que permitan comprender mejor el comportamiento de la mortalidad a nivel nacional.")
        st.write("")
        st.write("---------------------------------------------------------------------------------------------------------------------------------------------------")
        logo_path = Path(__file__).resolve().parents[1] / "Imagenes" / "dane.png"
        if logo_path.exists():
            st.image(str(logo_path), width=1700)
        else:
            st.write("Logo DANE no disponible")
    elif opcion == " datos":
        st.markdown(
            """
            <div style="display: flex; justify-content: center; margin-bottom: 20px;">
                <div style="background-color: #ffe6e6; border: 2px solid #ff4d4d; border-radius: 14px; padding: 18px 28px; max-width: 900px; width: 100%;">
                    <h1 style="text-align: center; color: #b30000; margin: 0;">datos</h1>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        logo_path = Path(__file__).resolve().parents[1] / "Imagenes" / "dane.png"
        if logo_path.exists():
            st.image(str(logo_path), width=1700)
        else:
            st.write("Logo DANE no disponible")
       