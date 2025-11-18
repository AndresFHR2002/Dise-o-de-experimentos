import streamlit as st
import pandas as pd

def show_carga_datos_tab():
    st.title("📂 Carga de Datos")

    # --- SUBIR ARCHIVO ---
    archivo = st.file_uploader(
        "Seleccione el archivo Excel con la base de datos",
        type=["xlsx"]
    )

    # --- SI EL USUARIO CARGA EL ARCHIVO ---
    if archivo:
        df = pd.read_excel(archivo)

        # Guardar el DataFrame en la sesión para usarlo en otras pestañas
        st.session_state["df"] = df

        st.success("Datos cargados correctamente.")

        # Vista previa
        st.subheader("Vista previa de la base")
        st.dataframe(df.head())

        # Diccionario de datos
        st.subheader("📘 Diccionario de Variables")

        diccionario = {
            "hours_sleep": "Horas de sueño por día",
            "hours_study": "Horas de estudio por día",
            "exercise_per_week": "Número de veces que hace ejercicio a la semana",
            "stress_level": "Nivel de estrés reportado (1-10)",
            "screen_time": "Horas frente a la pantalla",
            "academic_performance": "Rendimiento académico (1-5)",
            "bmi": "Índice de masa corporal del estudiante",
            "id": "Identificador del estudiante en la base",
            "sleep_cat": "Categoría de horas de sueño (Alta / Media / Baja)",
            "study_cat": "Categoría de horas de estudio (Alta / Baja)",
            "exercise_label": "Etiqueta categórica del ejercicio"
        }

        st.table(pd.DataFrame(diccionario.items(), columns=["Variable", "Descripción"]))

    else:
        st.info("Suba un archivo Excel para continuar.")
