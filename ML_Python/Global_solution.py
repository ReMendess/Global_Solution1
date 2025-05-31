import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import joblib

st.set_page_config(page_title="Preditor de Deslizamento", layout="centered")
st.title("🌧️ Preditor de Risco de Deslizamento de Terra")
st.markdown("Insira as informações ambientais para estimar o risco com base em um modelo real treinado.")

# ---------------------
# Carregar modelo
# ---------------------

modelo = joblib.load("ML_Python/modelo_risco_deslizamento.pkl")

# ---------------------
# Inputs do usuário
# ---------------------
chuva = st.slider("Chuva (mm)", 0.0, 500.0, 150.0)
inclinacao = st.slider("Inclinação da encosta (graus)", 0.0, 90.0, 30.0)
saturacao = st.slider("Nível de saturação do solo (%)", 0.0, 1.0, 0.5)
vegetacao = st.slider("Cobertura vegetal (%)", 0.0, 1.0, 0.5)
agua = st.slider("Proximidade de corpos d'água (0 a 1)", 0.0, 1.0, 0.5)

st.markdown("### Tipo de Solo")
cascalho = st.slider("Solo cascalho (%)", 0.0, 1.0, 0.33)
arenoso = st.slider("Solo arenoso (%)", 0.0, 1.0 - cascalho, 0.33)
siltoso = 1.0 - cascalho - arenoso

if siltoso < 0:
    st.error("A soma dos tipos de solo não pode ultrapassar 100%.")
    st.stop()

# ---------------------
# Criar DataFrame de entrada
# ---------------------
X_input = pd.DataFrame([{
    "Chuva_mm": chuva,
    "Inclinacao_encosta": inclinacao,
    "Nivel_saturacao": saturacao,
    "Vegetacao": vegetacao,
    "Proximidade_agua": agua,
    "Solo_cascalho": cascalho,
    "Solo_arenoso": arenoso,
    "Solo_siltoso": siltoso
}])

# ---------------------
# Previsão
# ---------------------
risco = modelo.predict(X_input)[0]
risco = np.clip(risco, 0, 1)

# ---------------------
# Saída
# ---------------------
st.markdown("## Resultado da Predição")
if risco < 0.3:
    nivel = "🟢 Baixo"
    cor = "green"
elif risco < 0.6:
    nivel = "Moderado"
    cor = "yellow"
elif risco < 0.8:
    nivel = "Alto"
    cor = "orange"
else:
    nivel = "Crítico"
    cor = "red"

st.metric(label="Risco Estimado", value=f"{risco:.2%}")
st.markdown(f"### **Nível de Alerta**: <span style='color:{cor}; font-size: 28px'>{nivel}</span>", unsafe_allow_html=True)

# ---------------------
# Gráfico de comparação
# ---------------------
st.markdown("## Comparação com Média Histórica")

media_ficticia = {
    'Chuva_mm': 120,
    'Inclinacao_encosta': 25,
    'Nivel_saturacao': 0.4,
    'Vegetacao': 0.6,
    'Proximidade_agua': 0.5
}

features = ['Chuva_mm', 'Inclinacao_encosta', 'Nivel_saturacao', 'Vegetacao', 'Proximidade_agua']
valores_usuario = [chuva, inclinacao, saturacao, vegetacao, agua]
valores_historico = [media_ficticia[f] for f in features]

fig, ax = plt.subplots(figsize=(6, 3))
x = np.arange(len(features))
bar_width = 0.35
ax.bar(x - bar_width/2, valores_usuario, bar_width, label='Entrada Atual', color='skyblue')
ax.bar(x + bar_width/2, valores_historico, bar_width, label='Média Histórica', color='gray')
ax.set_xticks(x)
ax.set_xticklabels(features, rotation=30)
ax.set_ylabel('Valor')
ax.legend()
st.pyplot(fig)
