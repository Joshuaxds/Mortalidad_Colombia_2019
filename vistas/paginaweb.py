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
            " Datos"
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
        st.write("El gráfico de líneas muestra el comportamiento mensual de las muertes y permite observar cómo cambia la mortalidad a lo largo del año. En este caso, se aprecia una caída marcada al inicio del año, cuando el registro baja a cerca de 18 mil muertes, seguida de una recuperación progresiva en los meses posteriores. Hacia la mitad del año se observa un aumento sostenido que supera los 21 mil casos y al final vuelve a presentarse un ascenso importante, alcanzando el valor más alto del gráfico.")
        fig = grafico_lineas(df_filtrado)
        st.plotly_chart(fig, use_container_width=True)
        st.write("En términos interpretativos, esto demuestra que las defunciones no mantienen un comportamiento uniforme, sino que presentan variaciones mensuales. El principal hallazgo es que existen meses con menor carga de mortalidad y otros en los que el número de muertes aumenta de forma notable, lo que permite identificar momentos críticos dentro del año.")
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
        st.write("El mapa coroplético representa la distribución territorial de las muertes por departamento y permite comparar visualmente la intensidad de la mortalidad en todo el país. En esta escala, los departamentos en blanco reflejan la mayor concentración de muertes, mientras que los tonos azul oscuro corresponden a menor intensidad. La lectura del mapa muestra que la mortalidad no se distribuye de forma homogénea, sino que se concentra con mayor fuerza en algunos departamentos, especialmente en zonas con alta densidad poblacional y mayor actividad urbana. ")
        fig = mapa_departamentos(df_filtrado, divipola)
        st.plotly_chart(fig, use_container_width=True)
        st.write("El hallazgo principal de este gráfico es la desigual distribución territorial de la mortalidad, ya que algunos departamentos concentran una carga mucho mayor que otros, lo cual puede relacionarse con tamaño poblacional, condiciones socioeconómicas y acceso a servicios de salud")
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
        st.write("El gráfico de barras presenta las cinco ciudades con mayor número de homicidios asociados a arma de fuego, por lo que permite identificar con claridad los territorios con mayores problemas de violencia letal. En primer lugar, aparece Santiago de Cali, con cerca de 970 muertes, seguida de Bogotá D.C. con alrededor de 600, Medellín con un poco más de 400, Barranquilla con aproximadamente 250 y San José de Cúcuta con cerca de 200 casos. La diferencia entre la primera ciudad y las demás es bastante visible, lo que muestra una concentración importante de la violencia homicida en Cali.")
        fig = ciudades_mas_violentas(df_filtrado, divipola)
        st.plotly_chart(fig, use_container_width=True)
        st.write("Este gráfico permite concluir que la violencia no afecta por igual a todas las ciudades, sino que se concentra en ciertos centros urbanos donde conviven problemáticas de seguridad, criminalidad y conflictividad social. El hallazgo más relevante es que Santiago de Cali encabeza ampliamente el listado, convirtiéndose en la ciudad más problemática dentro de este indicador.") 
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
        st.write("La tabla de causas de muerte permite identificar cuáles enfermedades y condiciones tienen mayor impacto dentro de la mortalidad general. Uno de los hallazgos más importantes es el claro predominio de las enfermedades crónicas y cardiovasculares, ya que varias de las principales causas están relacionadas con problemas respiratorios, hipertensión y afectaciones cardíacas o renales. Esto evidencia que una gran parte de las defunciones se originan en enfermedades de larga duración que afectan progresivamente la salud de la población")
        fig = top_causas(df_filtrado, causas)
        st.plotly_chart(fig, use_container_width=True)
        st.write("Se  evidencia que la mortalidad está fuertemente marcada por enfermedades no transmisibles y crónicas, mostrando un patrón donde predominan afecciones respiratorias, cardiovasculares y renales. Esto permite concluir que gran parte de las defunciones se concentra en enfermedades de larga evolución, asociadas al envejecimiento, estilos de vida y condiciones de salud pública.") 
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
        st.write("El gráfico de barras apiladas compara el total de muertes entre hombres y mujeres en cada departamento y permite observar diferencias importantes según el sexo. Se aprecia que en la mayoría de los territorios la mortalidad masculina es mayor que la femenina, aunque la magnitud varía bastante entre departamentos. Los valores más altos se observan en Antioquia, Bogotá D.C. y Valle del Cauca, que concentran una gran cantidad de defunciones en ambos sexos, mientras que departamentos como Vaupés, Vichada, Guainía y Amazonas presentan niveles mucho más bajos. ")
        fig = muertes_sexo_departamento(df_filtrado, divipola)
        st.plotly_chart(fig, use_container_width=True)
        st.write("Esta distribución deja ver que la mortalidad no solo depende del sexo, sino también del peso poblacional de cada departamento. El principal hallazgo es la presencia de una sobremortalidad masculina, acompañada de grandes diferencias territoriales que hacen que algunos departamentos concentren mucho más volumen de muertes que otros.") 
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
        st.write("El histograma de distribución por grupo de edad muestra claramente en qué etapas de la vida se concentra la mayor cantidad de muertes. El grupo con el valor más alto es Vejez, con una diferencia muy amplia frente a los demás, superando las 115 mil muertes aproximadamente. Esta distribución confirma que la mortalidad aumenta de manera considerable con la edad y que la vejez es, por mucho, el grupo más vulnerable.")
        fig = muertes_por_edad(df_filtrado)
        st.plotly_chart(fig, use_container_width=True)
        st.write("El hallazgo más importante es la fuerte concentración de muertes en edades avanzadas, lo que evidencia el efecto del envejecimiento poblacional y de las enfermedades crónicas sobre la mortalidad.")
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
        st.write("El gráfico circular presenta las diez ciudades con menor número de muertes y muestra que todas tienen una participación igual del 10%, por lo que ninguna sobresale por encima de las demás dentro de este grupo. Las ciudades que aparecen son Pacoa, Caldas, Cútiva, Motavita, Aguada, Santa Bárbara, Sativasur, Tópaga, Lourdes y Rector. La igualdad de las porciones indica que, dentro del conjunto seleccionado, todas comparten el mismo peso  y que el gráfico está enfocado más en identificar las ciudades con menor mortalidad que en comparar diferencias entre ellas.")
        fig = ciudades_menor_mortalidad(df_filtrado, divipola)
        st.plotly_chart(fig, use_container_width=True)
        st.write("En términos interpretativos, este resultado sugiere que estas ciudades tienen una participación reducida en el total de defunciones y que probablemente corresponden a territorios de menor población o con características demográficas particulares.") 
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
        logo_path = Path(__file__).resolve().parents[1] / "Imagenes" / "datos_qr.png"
        if logo_path.exists():
            st.image(str(logo_path), width=800)
        else:
            st.write("Logo DANE no disponible")