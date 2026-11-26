
# imports
import pandas as pd
import streamlit as st
import os
import importlib.util

st.set_page_config(page_title="Home", layout="wide")

st.title("Statistics Project 1")

# bibliotecas requeridas
librerias_req = [
    "pandas",
    "streamlit",
    "plotly",
    "scipy",
    "numpy",
    "matplotlib"
]

st.subheader("Required libraries")

# comprobar instalacion de bibliotecas
for lib in librerias_req:
    if importlib.util.find_spec(lib) is not None:
        st.success(f"✅ **{lib}** is installed")
    else:
        st.error(f"❌ **{lib}** not found")
        st.caption(f"Run: `pip install {lib}`")

# boton para actualizar
if st.button("Check again"):
    st.rerun()

st.subheader("Data upload (required to run the project)")

# cargar archivo de temperaturas
archivo_cargado = st.file_uploader(
    "Upload the temperaturas.txt file",
    type=["txt"]
)

if archivo_cargado is not None:
    df = pd.read_csv(
        archivo_cargado,
        sep=r"\s+",
        encoding="utf-8"
    )
    st.session_state["datos_cargados"] = df
    st.success("File uploaded and stored in memory.")

st.subheader("Download technical report")

# ruta del informe PDF
ruta_pdf = "resources/document.pdf"

# comprobar si existe el informe
if os.path.exists(ruta_pdf):
    with open(ruta_pdf, "rb") as archivo_pdf:
        pdf_bytes = archivo_pdf.read()

    st.download_button(
        label="📄 Download Technical Report (PDF)",
        data=pdf_bytes,
        file_name="Technical_Report_Statistics.pdf",
        mime="application/pdf",
        help="Click to download the project's official document."
    )
else:
    st.error(
        f"⚠️ PDF file not found at the specified path: "
        f"`{ruta_pdf}`. Please verify the file is saved correctly."
    )
