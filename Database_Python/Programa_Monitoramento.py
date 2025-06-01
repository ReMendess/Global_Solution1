import streamlit as st
import oracledb
import pandas as pd
import matplotlib.pyplot as plt

# Configuração do banco Oracle
DSN = "oracle.fiap.com.br:1521/ORCL"
USER = "RM563145"
PASSWORD = "260399"

# Função de conexão
def obter_conexao():
    try:
        conn = oracledb.connect(user=USER, password=PASSWORD, dsn=DSN)
        return conn
    except Exception as exc:
        st.error(f"Erro na conexão com o banco: {exc}")
        return None

# Função para buscar o último registro por região
def obter_ultimos_registros():
    conn = obter_conexao()
    if conn is None:
        return pd.DataFrame()

    query = """
        SELECT * FROM (
            SELECT 
                REGIAO, TEMPERATURA, UMIDADE, TIPO_SOLO, INCLINACAO, 
                CHUVA, VIBRACAO, RISCO, NIVEL_RISCO,
                ROW_NUMBER() OVER (PARTITION BY REGIAO ORDER BY ROWID DESC) as rn
            FROM SENSORES_REGIAO
        ) WHERE rn = 1
    """

    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Função para contar alertas por região
def obter_frequencia_alertas():
    conn = obter_conexao()
    if conn is None:
        return pd.DataFrame()

    query = """
        SELECT REGIAO, COUNT(*) AS TOTAL_ALERTAS
        FROM SENSORES_REGIAO
        WHERE NIVEL_RISCO = 'Alto'
        GROUP BY REGIAO
        ORDER BY REGIAO
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Streamlit 
st.set_page_config(page_title="Monitoramento de Risco", layout="wide")
st.title("Monitoramento de Sensores por Região")

# Buscar dados
df_ultimos = obter_ultimos_registros()

if not df_ultimos.empty:
    st.subheader("🔍 Última leitura por região:")
    st.dataframe(df_ultimos, use_container_width=True)

    # Verificar se há risco alto
    regioes_em_alerta = df_ultimos[df_ultimos['NIVEL_RISCO'] == 'Alto']['REGIAO'].tolist()
    if regioes_em_alerta:
        for regiao in regioes_em_alerta:
            st.error(f"ALERTA: Nível de risco Alto detectado na região: {regiao}")
    else:
        st.success("Nenhum alerta de risco alto nas regiões monitoradas.")

    # Gráfico de frequência
    st.subheader("Frequência de alertas de risco ALTO por região")
    df_alertas = obter_frequencia_alertas()

    if not df_alertas.empty:
        fig, ax = plt.subplots()
        ax.bar(df_alertas['REGIAO'], df_alertas['TOTAL_ALERTAS'], color='red')
        ax.set_xlabel("Região")
        ax.set_ylabel("Quantidade de Alertas")
        ax.set_title("Alertas de Risco Alto por Região")
        st.pyplot(fig)
    else:
        st.info("Nenhum alerta de risco alto registrado no histórico.")

else:
    st.warning("Nenhum dado encontrado na tabela SENSORES_REGIAO.")
