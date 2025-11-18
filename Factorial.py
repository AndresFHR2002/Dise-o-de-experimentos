import streamlit as st
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.anova import anova_lm
import matplotlib.pyplot as plt
from scipy.stats import boxcox
import numpy as np

def show_factorial_tab():
    st.title("🧪 Diseño Factorial – ANOVA")

    # ─────────────────────────────────────────────
    # VERIFICAR SI HAY DATOS CARGADOS
    # ─────────────────────────────────────────────
    if "df" not in st.session_state:
        st.warning("Primero carga los datos en la pestaña **Carga de Datos**.")
        return

    df = st.session_state["df"]

    # ─────────────────────────────────────────────
    # CONVERTIR VARIABLES A FACTORES
    # ─────────────────────────────────────────────
    st.subheader("🎚 Conversión de variables a factores")
    st.write("Se convierten los tres factores del diseño factorial:")

    df["hours_sleep_cat"] = pd.qcut(df["hours_sleep"], 3, labels=["Baja", "Media", "Alta"])
    df["hours_study_cat"] = pd.qcut(df["hours_study"], 3, labels=["Bajo", "Medio", "Alto"])
    df["exercise_cat"] = pd.qcut(df["exercise_per_week"], 3, labels=["Poco", "Moderado", "Alto"])

    st.write(df[["hours_sleep_cat", "hours_study_cat", "exercise_cat"]].head())

    # ─────────────────────────────────────────────
    # MODELO FACTORIAL
    # ─────────────────────────────────────────────
    st.subheader("📘 Modelo factorial")

    formula = "academic_performance ~ hours_sleep_cat * hours_study_cat * exercise_cat"
    st.code(formula)

    modelo = smf.ols(formula, data=df).fit()

    # ─────────────────────────────────────────────
    # ANOVA
    # ─────────────────────────────────────────────
    st.subheader("📊 Tabla ANOVA del modelo factorial")

    tabla_anova = anova_lm(modelo, typ=2)
    st.dataframe(tabla_anova)

    # Interpretación automática
    st.markdown("### 📝 Interpretación rápida")
    if (tabla_anova["PR(>F)"] < 0.05).any():
        st.success("Existen efectos significativos en al menos un factor o interacción.")
    else:
        st.warning("Ningún factor muestra efecto significativo al 5%. El modelo no explica bien el rendimiento.")

    # ─────────────────────────────────────────────
    # PRUEBA DE NORMALIDAD (SHAPIRO)
    # ─────────────────────────────────────────────
    st.subheader("📉 Prueba de Normalidad – Shapiro-Wilk")

    residuos = modelo.resid
    shapiro_test = stats.shapiro(residuos)

    st.write(f"**Statistic:** {shapiro_test.statistic:.4f}")
    st.write(f"**p-value:** {shapiro_test.pvalue:.4f}")

    if shapiro_test.pvalue < 0.05:
        st.error("Los residuos NO siguen una distribución normal.")
    else:
        st.success("Los residuos siguen normalidad.")

    # QQplot
    fig, ax = plt.subplots()
    sm.qqplot(residuos, line="45", ax=ax)
    st.pyplot(fig)

    # ─────────────────────────────────────────────
    # PRUEBA DE HOMOGENEIDAD – LEVENE
    # ─────────────────────────────────────────────
    st.subheader("⚖ Prueba de Homogeneidad – Levene")

    lev = stats.levene(
        df["academic_performance"],
        df["hours_sleep"],
        df["hours_study"],
        df["screen_time"]
    )

    st.write("**Statistic:**", lev.statistic)
    st.write("**p-value:**", lev.pvalue)

    if lev.pvalue < 0.05:
        st.error("Las varianzas NO son homogéneas según Levene.")
    else:
        st.success("Las varianzas son homogéneas.")

    # ─────────────────────────────────────────────
    # TRANSFORMACIÓN BOX–COX (OPCIONAL)
    # ─────────────────────────────────────────────
    st.subheader("🔧 Transformación Box–Cox (Opcional)")

    if st.checkbox("Aplicar transformación Box–Cox a la variable respuesta"):
        y = df["academic_performance"]
        y_shift = y + 0.01  # prevenir ceros
        y_boxcox, lambda_bc = boxcox(y_shift)
        st.write("Lambda óptimo:", lambda_bc)

        fig2, ax2 = plt.subplots()
        sm.qqplot(y_boxcox, line="45", ax=ax2)
        st.pyplot(fig2)

    # ─────────────────────────────────────────────
    # POST-HOC – TUKEY
    # ─────────────────────────────────────────────
    st.subheader("📌 Comparaciones Post-Hoc – Tukey")

    variable_posthoc = st.selectbox(
        "Seleccione el factor para aplicar Tukey:",
        ["hours_sleep_cat", "hours_study_cat", "exercise_cat"]
    )

    tukey = pairwise_tukeyhsd(
        endog=df["academic_performance"],
        groups=df[variable_posthoc],
        alpha=0.05
    )

    st.write(tukey.summary())

    fig3 = tukey.plot_simultaneous()
    st.pyplot(fig3.figure)

    st.info("Si no hay diferencias significativas, los grupos no difieren realmente en rendimiento académico.")
