# Modelo_Global_Solution.ipynb

Utilizando o notebook colab, pegamos os dados do Kaggle: https://www.kaggle.com/datasets/rajumavinmar/landslide-dataset
Nesse conjunto de dados, temos informações sobre fatores que influenciam deslizamentos, como precipitação, ângulo de declive, propriedades do solo, cobertura vegetal, atividade sísmica e proximidade de fontes de água. Cada linha representa uma observação única relacionada à ocorrência de deslizamentos, e as colunas descrevem atributos específicos associados às condições ambientais e geofísicas.

Realiamos a análise e tratamentos dos dados. Identificamos a correlação das variáveis e treinamenos um modelo de Machine Learning de predição.
Testamos diferentes modelos e optamos pelo RandomForestRegressor. Apesar de demonstrar uma certa tendência a overffiting no treinamento, ao analisar com os testes simulados, demonstrou uma boa acurácia e precisão.

<img src="/assets/9.png">

<img src="/assets/10.png">

# modelo_risco_deslizamento.pkl

Modelo treinado salvo.

# scaler_risco.pkl

Objeto que contém o StandardScaler do Scikit-Learn já ajustado (fitado) nos dados de treino.
Tem a média e o desvio padrão de cada feature usada no treino.

# Global_solution.py

Aplicação no Streamlit de predição de risco de deslizamento, utilizando o modelo treinado.
Permite o usuário selecionar as variáveis observadas ou simuladas e obter uma predição básica de risco de deslizamento da área.
Link da aplicação: https://globalsolution1-2nn8pxsmadkraeeuthm24b.streamlit.app


<img src="/assets/7.png">

<img src="/assets/8.png">


## 📦 Requisitos

- Streamlit
- Oracledb
- Scikit-learn
- Pandas
- Matplotlib
- Numpy
- Joblib
- Seaborn


