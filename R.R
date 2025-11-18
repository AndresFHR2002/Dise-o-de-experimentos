###############################################################
########Andres Felipe Hernandez Rojas ########################



###############################################
#        ANÁLISIS EXPLORATORIO DE DATOS       #
###############################################

# Librerías necesarias
library(readxl)
library(dplyr)
library(ggplot2)
library(psych)
library(GGally)
library(reshape2)

# Cargar base
df <- read_excel("C:/Users/FEPROCOL/Desktop/Semestre 10/Trabajo final/Base de datos.xlsx")

# Ver estructura
str(df)

########################################################
# 1. TABLAS DESCRIPTIVAS GENERALES
########################################################

# Selección de variables numéricas
num_vars <- df %>% 
  select(hours_sleep, hours_study, exercise_per_week,
         stress_level, bmi, screen_time, academic_performance)

# Tabla descriptiva completa
describe(num_vars)

# También con summary()
summary(num_vars)

########################################################
# 2. HISTOGRAMAS
########################################################

par(mfrow=c(2,3))
hist(df$hours_sleep, main="Horas de sueño", col="skyblue", xlab="")
hist(df$hours_study, main="Horas de estudio", col="lightgreen", xlab="")
hist(df$exercise_per_week, main="Ejercicio por semana", col="orange", xlab="")
hist(df$stress_level, main="Nivel de estrés", col="pink", xlab="")
hist(df$bmi, main="IMC", col="yellow", xlab="")
hist(df$academic_performance, main="Rendimiento académico", col="lightblue", xlab="")
par(mfrow=c(1,1))

########################################################
# 3. BOXPLOTS
########################################################

par(mfrow=c(2,3))
boxplot(df$hours_sleep, main="Boxplot: Horas sueno", col="skyblue")
boxplot(df$hours_study, main="Boxplot: Horas estudio", col="lightgreen")
boxplot(datos$exercise_label, main="Boxplot: Ejercicio/semana", col="orange")
boxplot(df$stress_level, main="Boxplot: Estres", col="pink")
boxplot(df$bmi, main="Boxplot: IMC", col="yellow")
boxplot(df$academic_performance, main="Boxplot: Rendimiento", col="lightblue")
par(mfrow=c(1,1))


boxplot(df$screen_time, main="Boxplot: IMC", col="yellow")

########################################################
# 4. DENSIDADES SUAVIZADAS
########################################################

ggplot(num_vars, aes(x = hours_sleep)) + 
  geom_density(fill="skyblue") + ggtitle("Densidad: Horas de Sueño")

ggplot(num_vars, aes(x = hours_study)) + 
  geom_density(fill="lightgreen") + ggtitle("Densidad: Horas de Estudio")

ggplot(num_vars, aes(x = exercise_per_week)) + 
  geom_density(fill="orange") + ggtitle("Densidad: Ejercicio por Semana")

########################################################
# 5. QQ-PLOTS PARA NORMALIDAD
########################################################

par(mfrow=c(2,3))
qqnorm(df$hours_sleep); qqline(df$hours_sleep, col="red")
qqnorm(df$hours_study); qqline(df$hours_study, col="red")
qqnorm(df$exercise_per_week); qqline(df$exercise_per_week, col="red")
qqnorm(df$stress_level); qqline(df$stress_level, col="red")
qqnorm(df$bmi); qqline(df$bmi, col="red")
qqnorm(df$academic_performance); qqline(df$academic_performance, col="red")
par(mfrow=c(1,1))

########################################################
# 6. GRÁFICOS DE BARRAS PARA VARIABLES CATEGÓRICAS
########################################################

ggplot(df, aes(x = sleep_cat)) +
  geom_bar(fill="skyblue") +
  ggtitle("Categorias de sueño")

ggplot(datos, aes(x = study_cat)) +
  geom_bar(fill="lightgreen") +
  ggtitle("Categorías de estudio")

ggplot(df, aes(x = exercise_label)) +
  geom_bar(fill="orange") +
  ggtitle("Frecuencia de ejercicio por semana")

########################################################
# 7. PAIRPLOT / MATRIZ DE CORRELACIÓN
########################################################

# Pairplot con GGally
ggpairs(num_vars)

# Correlación numérica
cor(num_vars)

########################################################
# 8. GRÁFICOS PRINCIPALES DE TUS TRES VARIABLES CLAVE
#    – horas_sleep
#    – hours_study
#    – exercise_per_week
########################################################

## Histograma + densidad
ggplot(datos, aes(x=hours_sleep)) +
  geom_histogram(aes(y=..density..), bins=20, fill="skyblue") +
  geom_density(color="red", linewidth=1.2) +
  ggtitle("Distribución: Horas de sueño")

ggplot(df, aes(x=hours_study)) +
  geom_histogram(aes(y=..density..), bins=20, fill="lightgreen") +
  geom_density(color="red", linewidth=1.2) +
  ggtitle("Distribución: Horas de estudio")

ggplot(df, aes(x=exercise_per_week)) +
  geom_histogram(aes(y=..density..), bins=10, fill="orange") +
  geom_density(color="red", linewidth=1.2) +
  ggtitle("Distribución: Ejercicio por semana")

## Boxplots individuales
ggplot(df, aes(y = hours_sleep)) + geom_boxplot(fill="skyblue")
ggplot(df, aes(y = hours_study)) + geom_boxplot(fill="lightgreen")
ggplot(df, aes(y = exercise_per_week)) + geom_boxplot(fill="orange")

## Relación con rendimiento académico
ggplot(datos, aes(x=hours_sleep, y=academic_performance)) +
  geom_point(color="blue") +
  geom_smooth(method="lm") +
  ggtitle("Sueño vs Rendimiento Académico")

ggplot(df, aes(x=hours_study, y=academic_performance)) +
  geom_point(color="green") +
  geom_smooth(method="lm") +
  ggtitle("Estudio vs Rendimiento Académico")

ggplot(df, aes(x=exercise_per_week, y=academic_performance)) +
  geom_point(color="orange") +
  geom_smooth(method="lm") +
  ggtitle("Ejercicio vs Rendimiento Académico")


########################################################
# 9. GRÁFICOS EXTRA: ESTRÉS, IMC Y TIEMPO EN PANTALLA
########################################################

ggplot(datos, aes(x=datos$stress_level)) +
  geom_histogram(fill="pink", bins=20) +
  ggtitle("Distribución del nivel de estres")

ggplot(df, aes(x=bmi)) +
  geom_histogram(fill="yellow", bins=20) +
  ggtitle("Distribución del IMC")

ggplot(df, aes(x=screen_time)) +
  geom_histogram(fill="purple", bins=20) +
  ggtitle("Distribución del tiempo en pantalla")

########################################################
# FIN DEL ANÁLISIS EXPLORATORIO
########################################################



# Seleccionar solo las variables importantes
vars <- datos[, c("hours_sleep", "hours_study", "exercise_per_week")]

# Cambiar nombres para que se vean bonitos en el gráfico
colnames(vars) <- c("Horas de sueno", "Horas de estudio", "Ejercicio por semana")

# Crear el boxplot conjunto
boxplot(vars,
        col = c("skyblue", "lightgreen", "lightcoral"),
        main = "Comparacion de variables importantes",
        ylab = "Valores",
        las = 2)   # hace que las etiquetas se lean verticalmente





boxplot(df$screen_time, main="Boxplot: IMC", col="yellow")





# Boxplot bonito para screen_time
boxplot(df$screen_time,
        main = "Distribución del tiempo frente a pantalla",
        ylab = "Horas por día",
        notch = TRUE,             # Muesca para ver diferencia de medianas
        boxwex = 0.5,             # Grosor del box
        cex.axis = 1.1,           # Tamaño de eje
        cex.lab = 1.2,            # Tamaño de etiquetas
        cex.main = 1.4,           # Tamaño del título
        frame.plot = FALSE        # Quita los bordes del gráfico
)

# Agregar una linea de la mediana para destacar






plot(datos$screen_time, datos$academic_performance,
     main = "Relación entre horas de pantalla y rendimiento académico",
     xlab = "Horas de pantalla por día",
     ylab = "Rendimiento académico",
     pch = 19,
     col = "steelblue")

# Línea de tendencia
abline(lm(df$academic_performance ~ df$screen_time), col = "red", lwd = 2)








# Crear categorías de horas de pantalla
datos$screen_group <- cut(datos$screen_time,
                       breaks = c(0, 2, 4, 6, 10),
                       labels = c("Bajo", "Moderado", "Alto", "Muy alto"),
                       include.lowest = TRUE)

# Boxplot comparativo
boxplot(academic_performance ~ screen_group, data=datos,
        main = "Rendimiento académico según nivel de horas de pantalla",
        xlab = "Nivel de exposición a pantallas",
        ylab = "Rendimiento académico",
        col = c("lightgreen", "lightblue", "orange", "tomato"))












# Gráfico de dispersión entre horas de estudio y rendimiento académico
plot(datos$hours_study, datos$academic_performance,
     main = "Relación entre horas de estudio y rendimiento académico",
     xlab = "Horas de estudio por día",
     ylab = "Rendimiento académico",
     pch = 19,
     col = "darkgreen")

# Línea de tendencia lineal
abline(lm(datos$academic_performance ~ datos$hours_study), 
       col = "red", 
       lwd = 2)




# QQ-plot mejorado para academic_performance
qqnorm(datos$academic_performance,
       main = "QQ-Plot: Rendimiento Académico",
       pch = 19,
       col = "steelblue",
       cex = 1.1)

qqline(datos$academic_performance,
       col = "darkred",
       lwd = 2)

# Agregar cuadrícula suave
grid(col = "gray80", lty = 2)


modelo <- aov(academic_performance ~ hours_sleep * hours_study * exercise_per_week, data = datos)
modelo








modelo <- aov(academic_performance ~ sleep_cat * study_cat * exercise_label,
              data = datos)
summary(modelo)





res <- residuals(modelo)

# Normalidad (Shapiro sobre residuales)
shapiro.test(res)

# QQ-plot de residuales
qqnorm(res); qqline(res, col = "red")

# Homogeneidad de varianzas (Levene)
library(car)
leveneTest(academic_performance ~ sleep_cat * study_cat * exercise_label,
           data = datos)




datos$acad_trans <- log(datos$academic_performance)
model2 <- aov(acad_trans ~ sleep_cat * study_cat * exercise_label, data=datos)
shapiro.test(residuals(model2))




library(MASS)

bc <- boxcox(aov(academic_performance ~ sleep_cat * study_cat * exercise_label,
                 data = datos))

lambda <- bc$x[which.max(bc$y)]
lambda


if(lambda == o){
  datos$acad_trans <- log(datos$academic_performance)
} else {
  datos$acad_trans <- (datos$academic_performance^lambda - 1) / lambda
}

model_bc <- aov(acad_trans ~ sleep_cat * study_cat * exercise_label, data = datos)

shapiro.test(residuals(model_bc))





datos$acad_trans <- sqrt(datos$academic_performance)
model_sqrt <- aov(acad_trans ~ sleep_cat * study_cat * exercise_label, data = datos)
shapiro.test(residuals(model_sqrt))


datos$acad_trans <- 1 / datos$academic_performance
model_inv <- aov(acad_trans ~ sleep_cat * study_cat * exercise_label, data = datos)
shapiro.test(residuals(model_inv))






library(bestNormalize)

yj <- yeojohnson(datos$academic_performance)
datos$acad_trans <- predict(yj)

model_yj <- aov(acad_trans ~ sleep_cat * study_cat, data = datos)
shapiro.test(residuals(model_yj))

TukeyHSD(modelo)



resultado_tukey <- TukeyHSD(modelo)

print(resultado_tukey)

plot(resultado_tukey, las = 1, cex.axis = 0.7)


modelo <- aov(academic_performance ~ sleep_cat * study_cat,
              data = datos)

resultado_tukey <- TukeyHSD(modelo)

print(resultado_tukey)


TukeyHSD(modelo, "sleep_cat")
TukeyHSD(modelo, "study_cat")
TukeyHSD(modelo, "exercise_label")



