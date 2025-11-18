import streamlit as st

# Importar cada sección (cada una será un archivo .py)
from Introduccion import show_introduccion_tab
from Carga_datos import show_carga_datos_tab
from Visualizacion import show_visualizaciones_tab
from Factorial import show_factorial_tab
from Conclusiones import show_final_tab

# Crear pestañas principales
tabs = st.tabs([
    "📘 Introducción",
    "📂 Carga de Datos",
    "📊 Visualización - EDA",
    "🧪 Diseño Factorial (ANOVA)",
    "📝 Conclusiones y Referencias"
])

# Mostrar contenido en cada pestaña
with tabs[0]:
    show_introduccion_tab()

with tabs[1]:
    show_carga_datos_tab()

with tabs[2]:
    show_visualizaciones_tab()

with tabs[3]:
    show_factorial_tab()

with tabs[4]:
    show_final_tab()
