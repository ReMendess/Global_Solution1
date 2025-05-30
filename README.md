# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Global Solution - 1º Semestre

## Nome do Grupo

- Arthur Luiz Rosado Alves -> RM562061
- Renan de Oliveira Mendes -> RM563145



## Sumário

[1. Justificativa do Problema](#c1)

[2. Descrição da Solução Proposta](#c2)

[3. Tecnologias Propostas](#c3)

[4. Pipeline de Dados](#c4)

[5. Diagrama](#c6)

<br>

# <a name="c1"></a>1. Justificativa do Problema

*Os deslizamentos de terra são uma ameaça a sociedade em geral, ao patrimônio e à infraestrutura, especialmente no Brasil onde estima-se que 8 milhões de brasileiros vivem em áreas de risco geológico, havendo muitas favelas, ocupação desordenada e alta incidência de chuvas. Esses eventos ocorrem, de forma súbita e sem aviso, resultando em tragédias como perdas humanas, perdas de moradias e elevados custos socioeconômicos. A situação é agravada pela ausência de sistemas preditivos , que dificultam a detecção precoce de riscos geotécnicos. Diante desse cenário, propomos uma solução tecnológica capaz de monitorar continuamente variáveis críticas — como umidade, temperatura e vibrações do solo, inclinação do terreno, e intensidade das chuvas —, identificar padrões de risco e emitir alertas preventivos. Essa abordagem permite uma resposta rápida e controlada principalmente pela análise de dados, facilitando tomadas de decisões em tempo real, assim minimizando os impactos do desastre e promovendo maior segurança para as comunidades afetadas.*

# <a name="c2"></a>2. Descrição da Solução Proposta

A solução proposta consiste em uma plataforma inteligente de monitoramento industrial, baseada na integração de tecnologias como sensores IoT, armazenamento em nuvem, inteligência artificial e visualização de dados. O objetivo é detectar antecipadamente possíveis falhas em equipamentos, reduzindo paradas inesperadas, otimizando manutenções e promovendo segurança operacional.

- **Coletar dados em tempo real via sensores IoT**;

- **Armazenar os dados em um banco de dados na nuvem;**
  
- **Processamento e Tratamento dos dados;**

- **Aplicar algoritmos de machine learning para identificar padrões de instabilidade e prever possiveis deslizamentos**

- **Visualização em dashboards interativos e simplificados;**

- **Emitir alertas automaticos por aplicativo, sms ou rádio, orientando possiveis evacuações ou ações**


# <a name="c3"></a>3. Tecnologias Propostas/Planejadas


## Definição das Tecnologias Utilizadas

| Camada                   | Tecnologias                                         |
|--------------------------|-----------------------------------------------------|
| **Sensoriamento**        | ESP32                                               |
| **Armazenamento**        | PostgreSQL                                          |
| **Backend e APIs**       | Python, tratamentos de dados e serviços.            |
| **IA / Machine Learning**| Streamlit, scikit-learn                             |
| **Infraestrutura**       | AWS                                                 |


# <a name="c4"></a>4. Pipeline de Dados

**Sensores IoT captam dados:**
- Umidade excessiva no solo;
- Vibrações sísmicas anormais;
- Inclinação do terreno (movimentações milimétricas);
- Volume de chuvas acumuladas;
- Temperatura e pressão atmosférica.



**Salvar dados brutos**
- Dados coletados pelos sensores são enviados ao servidor de ingestão.
- A API "Coletar Dados" armazena essas informações no banco de dados hospedado em nuvem.

**Limpeza e tratamento**
- Realiza pré-processamento e normalização;
- Remoção de dados nulos ou ausentes;
- Correção de dados inválidos;
- Prepara os dados para análise preditiva e visualização;

**Análise preditiva com Machine Learning**
- Modelos de machine learning são treinados com base em dados históricos de deslizamentos, padrões de chuva, inclinação e saturação do solo.
- Esses modelos analisam os sinais captados pelos sensores e identificam:
- Probabilidade de deslizamento em áreas monitoradas;
- Níveis de risco geotécnico;
- Anomalias ambientais fora do comportamento esperado.
- O objetivo é antecipar eventos críticos e permitir evacuação ou contenção antecipada.

**Visualização dos Dados em Dashboards**
- Os dados processados e as predições são apresentados em dashboards desenvolvidos com Python (Streamlit/Plotly) ou R (Shiny).
- Interface intuitiva para defesa civil, autoridades locais e população.

**Informações exibidas:**
- Status dos sensores em tempo real nas regiões monitoradas;
- Alertas de risco com níveis (verde, amarelo, vermelho);
- Mapas georreferenciados com zonas críticas;
- Histórico de condições climáticas e movimentação do terreno;
- Recomendações de ações preventivas (ex: evacuação, reforço de encostas).

**Notificações e Resposta Operacional**
- Notificações automáticas via chatbot, SMS, rádio comunitário ou aplicativo móvel;
- Registro de todas as decisões e ações realizadas por autoridades e equipes técnicas para rastreabilidade;
- Feedback das ocorrências para refinamento contínuo do modelo preditivo;
- Estimativa do impacto humano e material em caso de confirmação do evento;
- Geração automática de ordens de resposta (evacuação, isolamento de áreas, envio de equipes técnicas).




# <a name="c6"></a>6. Diagrama

<p align="center">
<img src="diagrama.drawio (1).png" alt="Driagrama da solução"></a>
</p>
