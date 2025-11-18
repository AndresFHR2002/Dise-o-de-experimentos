import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

def show_visualizaciones_tab():

    st.title("📊 Visualización y Análisis Exploratorio (EDA)")

    # Verificar si se cargaron datos en la pestaña 2
    if "df" not in st.session_state:
        st.warning("⚠️ Primero cargue la base de datos en la pestaña **Carga de Datos**.")
        return
    
    df = st.session_state["df"]

    # ============================
    # VISTA GENERAL
    # ============================
    st.subheader("📌 1. Vista General de los Datos")
    st.dataframe(df.head())

    st.subheader("📌 2. Estadísticos Descriptivos")
    st.write(df.describe())

    # ============================
    # HISTOGRAMAS
    # ============================
    st.subheader("📊 Histogramas")

    variables_numericas = df.select_dtypes(include=["int64", "float64"]).columns.tolist()

    if len(variables_numericas) == 0:
        st.warning("No hay variables numéricas disponibles para graficar.")
        return

    variable_hist = st.selectbox("Seleccione una variable para ver su histograma", variables_numericas)

    fig = px.histogram(df, x=variable_hist, nbins=20, title=f"Histograma de {variable_hist}")
    st.plotly_chart(fig)

    # ============================
    # BOXPLOTS
    # ============================
    st.subheader("📦 Boxplots Interactivos")

    variable_box = st.selectbox("Seleccione una variable numérica para boxplot", variables_numericas)

    fig2 = px.box(df, y=variable_box, title=f"Boxplot de {variable_box}")
    st.plotly_chart(fig2)

    # ============================
    # CORRELACIÓN 🔥 (CORREGIDO)
    # ============================
    st.subheader("🔥 Mapa de calor de correlaciones")

    # Seleccionamos SOLO variables numéricas para evitar errores
    df_numerico = df.select_dtypes(include=["int64", "float64"])

    if df_numerico.shape[1] >= 2:
        corr = df_numerico.corr()

        fig_corr = px.imshow(
            corr,
            text_auto=True,
            aspect="auto",
            color_continuous_scale="RdBu_r",
            title="Matriz de Correlaciones"
        )
        st.plotly_chart(fig_corr)
    else:
        st.info("No hay suficientes variables numéricas para calcular correlaciones.")

    # ============================
    # SCATTER CON RENDIMIENTO
    # ============================
    st.subheader("📈 Relación con el rendimiento académico")

    if "academic_performance" in df.columns:
        variable_scatter = st.selectbox(
            "Seleccione una variable para graficar contra rendimiento académico",
            variables_numericas
        )

        fig_sc = px.scatter(
            df,
            x=variable_scatter,
            y="academic_performance",
            trendline="ols",
            title=f"{variable_scatter} vs Rendimiento Académico"
        )
        st.plotly_chart(fig_sc)
    else:
        st.error("La variable 'academic_performance' no está en la base de datos.")

    
    
