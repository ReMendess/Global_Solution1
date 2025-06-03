# RenanMendes
# ArthurRosado


# Instalando os pacotes.
install.packages("readr")
install.packages("dplyr")
install.packages("ggplot2")
install.packages("readxl")
install.packages("writexl")
install.packages("psych")
install.packages("corrplot")
install.packages("ggpubr")

# Carregar bibliotecas necessárias
library(ggplot2)
library(dplyr)
library(tidyr)
library(corrplot)
library(ggpubr)
library(readr)

dados <- read_delim("C:/Users/renan.a.mendes/Downloads/dados.csv", delim = ",", locale = locale(decimal_mark = "."))


# Ver os dados
print(dados)


# Verificar nomes das colunas
print(colnames(dados))

# Renomear as colunas 
colnames(dados) <- c("Regiao", "Temperatura", "Umidade", "Tipo_Solo", 
                     "Inclinacao", "Chuva", "Vibracao", "Risco", "Nivel_Risco")

# Verificação
glimpse(dados)

# Estatísticas descritivas
summary(dados)

# Converter variáveis categóricas para fator
dados$Regiao <- as.factor(dados$Regiao)
dados$Tipo_Solo <- as.factor(dados$Tipo_Solo)
dados$Inclinacao <- as.factor(dados$Inclinacao)
dados$Chuva <- as.factor(dados$Chuva)
dados$Nivel_Risco <- as.factor(dados$Nivel_Risco)

# Correlação entre variáveis numéricas
num_vars <- dados %>%
  select(Temperatura, Umidade, Vibracao, Risco)

cor_matrix <- cor(num_vars)
print(cor_matrix)
corrplot(cor_matrix, method = "circle", tl.col = "black", tl.cex = 0.8)

# Boxplot da temperatura por nível de risco
ggplot(dados, aes(x = Nivel_Risco, y = Temperatura, fill = Nivel_Risco)) +
  geom_boxplot() +
  labs(title = "Temperatura por Nível de Risco", y = "Temperatura (°C)", x = "Nível de Risco") +
  theme_minimal()

# Gráfico de barras da frequência por tipo de solo
ggplot(dados, aes(x = Tipo_Solo, fill = Tipo_Solo)) +
  geom_bar() +
  labs(title = "Distribuição por Tipo de Solo", x = "Tipo de Solo", y = "Frequência") +
  theme_minimal()

# Gráfico de dispersão: Umidade vs Risco
ggplot(dados, aes(x = Umidade, y = Risco, color = Nivel_Risco)) +
  geom_point(size = 3) +
  labs(title = "Umidade vs Risco", x = "Umidade (%)", y = "Nível de Risco") +
  theme_minimal()

# Facet: risco por região e chuva
ggplot(dados, aes(x = Regiao, y = Risco, fill = Chuva)) +
  geom_bar(stat = "identity", position = "dodge") +
  labs(title = "Risco por Região e Condição de Chuva", y = "Risco") +
  theme_minimal()

