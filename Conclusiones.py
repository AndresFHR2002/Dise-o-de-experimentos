import streamlit as st

def show_final_tab():

    st.title("📝 Conclusiones, Estado del Arte y Referencias")

    st.header("1️⃣ Pensamiento Crítico Metodológico")
    st.write("""
    El análisis realizado permitió evaluar la relación entre horas de sueño, horas de estudio
    y actividad física con el rendimiento académico. No obstante, el proyecto presentó
    limitaciones metodológicas importantes, especialmente relacionadas con el cumplimiento
    de los supuestos del modelo factorial ANOVA.

    A pesar de aplicar transformaciones —incluyendo Box-Cox— la variable de rendimiento
    académico no alcanzó una distribución completamente normal y tampoco se logró la 
    homogeneidad de varianzas según la prueba de Levene. Esto sugiere que los datos originales 
    podrían contener ruido, escalas restrictivas (1-5) o poca variabilidad en algunos niveles 
    de los factores. Estas condiciones afectan la sensibilidad del ANOVA, lo cual requiere
    interpretar los resultados con cautela, reconociendo que el modelo puede no estimar
    adecuadamente los efectos reales.
    """)

    st.header("2️⃣ Estado del Arte")
    st.write("""
    Investigaciones previas han demostrado que el rendimiento académico está influenciado
    por múltiples factores, entre ellos el sueño, la carga académica, los hábitos de estudio,
    el estrés y los estilos de vida saludables. Estudios como los de Curcio et al. (2006)
    encuentran que la falta de sueño afecta directamente procesos cognitivos como memoria y 
    atención. De manera complementaria, investigaciones sobre actividad física (Taras, 2005)
    muestran que el ejercicio regular se asocia con mejoras en la concentración y el estado 
    emocional del estudiante.

    En cuanto a metodologías de análisis, el uso de diseños factoriales para explorar la
    interacción de variables relacionadas con hábitos de vida es común en estudios 
    educativos y psicológicos. Sin embargo, diversas publicaciones detallan que estas
    variables rara vez cumplen supuestos estrictos de normalidad debido a que suelen ser
    medidas autoinformadas, discretas o sesgadas. Por ello, muchas investigaciones recomiendan
    modelos alternativos como ANOVA robusto, modelos lineales generalizados o regresiones ordinales.
    """)

    st.header("3️⃣ Conclusiones Finales")
    st.write("""
    - **Conclusión 1:** No se encontraron efectos estadísticamente significativos de los 
      tres factores evaluados (sueño, estudio y ejercicio) sobre el rendimiento académico,
      lo cual puede deberse tanto a la estructura de los datos como a la falta de cumplimiento
      de los supuestos del ANOVA.

    - **Conclusión 2:** Aunque las transformaciones mejoraron ligeramente la normalidad,
      no corrigieron totalmente la heterogeneidad de varianzas, indicando que la variable
      respuesta podría requerir un modelo alternativo o un instrumento de medición con mayor
      sensibilidad.

    - **Conclusión 3:** Los resultados sugieren que, dentro de esta base de datos particular,
      los hábitos de sueño, estudio y ejercicio no presentan cambios suficientemente marcados
      como para generar diferencias detectables en el rendimiento. Se recomienda ampliar la
      muestra, mejorar la calidad del registro y considerar otras variables relevantes como
      motivación, hábitos de estudio y factores socioemocionales.
    """)

    st.header("4️⃣ Referencias")
    st.write("""
    - Curcio, G., Ferrara, M., & De Gennaro, L. (2006). Sleep loss, learning capacity and 
      academic performance. *Sleep Medicine Reviews.*
    - Taras, H. (2005). Physical activity and student performance. *Journal of School Health.*
    - Montgomery, D. C. (2017). *Design and Analysis of Experiments.* Wiley.
    - Howell, D. (2012). *Statistical Methods for Psychology.* Cengage.
    """)
