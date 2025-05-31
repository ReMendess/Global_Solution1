import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Carregar o modelo e o scaler treinado
modelo = joblib.load("ML_Python/modelo_risco_deslizamento.pkl")
scaler = joblib.load("ML_Python/scaler_risco.pkl")

# Interface
st.title("Predição de Risco de Deslizamento")

# Entradas do usuário
chuva = st.slider("Chuva (mm)", 0, 500, 100)
inclinacao = st.slider("Inclinação da Encosta", 0, 90, 30)
saturacao = st.slider("Nível de Saturação", 0.0, 1.0, 0.5)
vegetacao = st.slider("Cobertura Vegetal", 0.0, 1.0, 0.5)
proximidade_agua = st.slider("Proximidade de Corpos d'Água", 0.0, 1.0, 0.5)

solo = st.selectbox("Tipo de Solo", ["Cascalho", "Arenoso", "Siltoso"])

# One-hot encoding manual para o tipo de solo
solo_cascalho = 1 if solo == "Cascalho" else 0
solo_arenoso = 1 if solo == "Arenoso" else 0
solo_siltoso = 1 if solo == "Siltoso" else 0

# Criar DataFrame com os dados de entrada
X_input = pd.DataFrame([[
    chuva, inclinacao, saturacao, vegetacao, proximidade_agua,
    solo_cascalho, solo_arenoso, solo_siltoso
]], columns=[
    'Chuva_mm', 'Inclinacao_encosta', 'Nivel_saturacao', 'Vegetacao',
    'Proximidade_agua', 'Solo_cascalho', 'Solo_arenoso', 'Solo_siltoso'
])

# Aplicar o mesmo scaler usado no treino
X_input_scaled = scaler.transform(X_input)

# Fazer a predição
risco = modelo.predict(X_input_scaled)[0]

# Exibir o resultado
st.subheader("Resultado da Predição")
st.write(f"Nível de risco de deslizamento: **{risco:.3f}**")

# Opcional: exibir uma faixa de risco
if risco < 0.3:
    st.success("Baixo risco")
elif risco < 0.6:
    st.warning("Risco moderado")
else:
    st.error("Alto risco!")
