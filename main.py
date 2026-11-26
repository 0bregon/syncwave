
import streamlit as st
import pandas as pd

# configuracion de la pagina
st.set_page_config(
    page_title="MarketTech AI",
    page_icon="💻",
    layout="wide"
)

# encabezado
st.title("💻 MarketTech AI")
st.subheader("Análisis del mercado tecnológico")

st.write(
    "Plataforma de análisis de precios de componentes "
    "informáticos y su relación con indicadores económicos "
    "de Panamá y Estados Unidos."
)

st.divider()

# navegacion
seccion = st.sidebar.selectbox(
    "Navegación",
    [
        "Inicio",
        "Datos del mercado",
        "Análisis de precios",
        "Comparación de mercados",
        "Indicadores económicos",
        "Interpretación con IA"
    ]
)

# pagina de inicio
if seccion == "Inicio":
    st.header("Bienvenido a MarketTech AI")

    st.write(
        "Explora información sobre el comportamiento "
        "del mercado de componentes informáticos."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.info("🇵🇦 **Mercado de Panamá**")
        st.write("Consulta y analiza precios de tiendas panameñas.")

    with col2:
        st.info("🇺🇸 **Mercado de Estados Unidos**")
        st.write("Consulta y analiza precios del mercado estadounidense.")

    st.divider()

    st.subheader("Categorías de componentes")

    categorias = ["CPU", "GPU", "RAM", "SSD"]

    columnas = st.columns(4)

    for columna, categoria in zip(columnas, categorias):
        with columna:
            st.metric(label=categoria, value="Pendiente")

    st.caption(
        "Los indicadores se mostrarán cuando se conecten "
        "los conjuntos de datos."
    )

# datos del mercado
elif seccion == "Datos del mercado":
    st.header("Datos del mercado")
    st.write(
        "Aquí se consultarán los registros de precios "
        "de componentes informáticos."
    )

# analisis de precios
elif seccion == "Análisis de precios":
    st.header("Análisis de precios")
    st.write(
        "Aquí se presentarán estadísticas y visualizaciones "
        "del comportamiento de los precios."
    )

# comparacion de mercados
elif seccion == "Comparación de mercados":
    st.header("Comparación de mercados")
    st.write(
        "Aquí se compararán los precios de Panamá "
        "y Estados Unidos."
    )

# indicadores economicos
elif seccion == "Indicadores económicos":
    st.header("Indicadores económicos")
    st.write(
        "Aquí se analizarán indicadores económicos "
        "y su relación con los precios tecnológicos."
    )

# interpretacion con ia
elif seccion == "Interpretación con IA":
    st.header("Interpretación con inteligencia artificial")
    st.write(
        "Aquí se integrará Gemini para interpretar "
        "los resultados obtenidos mediante el análisis de datos."
    )
