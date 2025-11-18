import streamlit as st

def show_introduccion_tab():
    st.title("Introducción al Estudio")


    st.header("🎯Introduccion")
    st.write("""
    El rendimiento académico universitario está influenciado por múltiples factores que van desde aspectos individuales hasta condiciones sociales e institucionales. Entre los determinantes más relevantes se encuentran los hábitos de vida, particularmente la actividad física y el sueño, ya que ambos impactan directamente procesos cognitivos como la memoria, la atención y la concentración. La literatura científica ha mostrado que una mayor frecuencia de ejercicio puede mejorar el bienestar físico y emocional, mientras que un adecuado descanso diario favorece la consolidación del aprendizaje y la regulación del estrés. Comprender la relación entre estos hábitos y el desempeño académico permite identificar patrones que orienten estrategias educativas y de bienestar estudiantil.
    En este proyecto se analiza cómo la frecuencia semanal de actividad física y las horas de sueño diaria se asocian con el promedio académico de un grupo de estudiantes universitarios. A través de un estudio descriptivo y exploratorio se busca caracterizar la base de datos, identificar posibles limitaciones y reconocer tendencias relevantes entre las variables. Este análisis constituye un primer paso fundamental para sustentar futuras etapas de modelación o toma de decisiones, aportando una visión clara sobre la influencia de los hábitos saludables en el desempeño académico.
    """)

    st.header("🎯 Comprensión del Problema")
    st.write("""
    El rendimiento académico es un indicador clave del desarrollo formativo de los estudiantes y depende de factores que no siempre están bajo control institucional. Entre ellos, los hábitos de vida juegan un papel central, especialmente la actividad física semanal y las horas de sueño, que influyen en la salud física, el estado emocional y la capacidad cognitiva. Sin embargo, no siempre está claro en qué medida estos hábitos se relacionan con el desempeño académico ni cuál de ellos ejerce un mayor efecto.
    El problema central radica en determinar si variaciones en la frecuencia de ejercicio y en el tiempo de descanso diario se reflejan en diferencias significativas en el promedio académico. Esto implica identificar patrones, posibles asociaciones y comportamientos atípicos dentro de la base de datos, así como evaluar si existen indicios que sugieran relaciones consistentes entre estas variables. Comprender este problema es esencial para orientar acciones que promuevan hábitos más saludables y, potencialmente, un mejor desempeño académico.
    """)

    st.header("⚠️ Sesgos y Limitaciones")
    st.write("""
    Aunque la base de datos utilizada ofrece información útil sobre hábitos de vida y rendimiento académico, es importante reconocer ciertos sesgos y limitaciones inherentes a su estructura. En primer lugar, varias variables dependen de autorreporte, como las horas de sueño o las horas dedicadas al estudio, lo que puede introducir sesgos de memoria o deseabilidad social. Los estudiantes tienden a sobreestimar o subestimar estos valores, lo que afecta la precisión de las mediciones.
    También se identifica una posible falta de control sobre factores externos no incluidos en el conjunto de datos, como el nivel socioeconómico, la carga académica específica, el estrés emocional, la alimentación o la calidad del entorno familiar. Estos elementos pueden influir en el rendimiento académico y no estar capturados, lo que limita la capacidad de atribuir relaciones causales.
    """)

    st.header("🎯 Objetivo General")
    st.write("""
    Analizar de manera exhaustiva la relación entre diversos hábitos de vida estudiantil principalmente la actividad física semanal, las horas de estudio y las horas de sueño y su impacto en el rendimiento académico, empleando técnicas estadísticas descriptivas y analíticas que permitan identificar tendencias, asociaciones y posibles interacciones entre estas variables. Este objetivo busca establecer si estos factores contribuyen de manera significativa al desempeño académico, así como comprender la magnitud y dirección de sus efectos, con el fin de aportar evidencia útil para la toma de decisiones orientadas a mejorar el bienestar y el desempeño académico de los estudiantes.
    """)

    st.header("📌 Objetivos Específicos")
    st.markdown("""
    - Identificar los patrones generales de distribución y comportamiento de la actividad física semanal, las horas de estudio y las horas de sueño en la población universitaria analizada.
    - Evaluar la relación individual entre cada uno de los hábitos de vida seleccionados y el rendimiento académico, determinando su influencia y la dirección de sus efectos.
    - Analizar la posible interacción entre la actividad física, las horas de estudio y las horas de sueño, con el fin de establecer si la combinación de estos factores genera cambios significativos en el desempeño académico.
    - Describir los hallazgos obtenidos mediante técnicas de análisis exploratorio de datos y modelación estadística, generando conclusiones que aporten evidencia para la comprensión del papel que desempeñan los hábitos estudiantiles en el rendimiento académico.
    """)
