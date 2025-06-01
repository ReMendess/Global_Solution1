# Modelo_Global_Solution.ipynb

Utilizando o notebook colab, pegamos os dados do Kaggle: https://www.kaggle.com/datasets/rajumavinmar/landslide-dataset
Nesse conjunto de dados, temos informações sobre fatores que influenciam deslizamentos, como precipitação, ângulo de declive, propriedades do solo, cobertura vegetal, atividade sísmica e proximidade de fontes de água. Cada linha representa uma observação única relacionada à ocorrência de deslizamentos, e as colunas descrevem atributos específicos associados às condições ambientais e geofísicas.

Realiamos a análise e tratamentos dos dados. Identificamos a correlação das variáveis e treinamenos um modelo de Machine Learning de predição.
Testamos diferentes modelos e optamos pelo RandomForestRegressor. Apesar de demonstrar uma certa tendência a overffiting no treinamento, ao analisar com os testes simulados, demonstrou uma boa acurácia e precisão.

<img src="/assets/9.png">

<img src="/assets/10.png">

# Programa_Monitoramento.py

Esta é uma aplicação Python que realiza o monitoramento dos últimos registros, por região, dentro da tabela.
Caso o último registro detectado seja de nivel de risco alto, é apresentado um alerta de deslizamento.
Criado utilizando Streamlit.

Link: https://globalsolution1-dzrtvby4c3n8krkph9ff9u.streamlit.app



## 📦 Requisitos

- Streamlit
- Oracledb
- Pandas
- Matplotlib


# Criando_Tabela.sql
Foi criado um banco de dados Oracle para a captação de registros de sensores.

<img src="/assets/4.png">

<img src="/assets/2.png">

<img src="/assets/1.png">

<img src="/assets/3.png">
