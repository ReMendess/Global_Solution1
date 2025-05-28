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

[5. Plano Inicial de Desenvolvimento](#c5)

[6. Diagrama](#c6)

<br>

# <a name="c1"></a>1. Justificativa do Problema

*As linhas de produção industrial sofrem frequentemente com paradas inesperadas, resultando em prejuízos financeiros, atrasos logísticos e riscos à segurança. Esse cenário é agravado pela ausência de sistemas preditivos em tempo real, que dificultam a antecipação de falhas. Diante disso, propomos uma solução que monitora continuamente os equipamentos, identifica padrões de falha e emite alertas para intervenções preventivas, tornando o ambiente mais eficiente, seguro e confiável.*

# <a name="c2"></a>2. Descrição da Solução Proposta

A solução proposta consiste em uma plataforma inteligente de monitoramento industrial, baseada na integração de tecnologias como sensores IoT, armazenamento em nuvem, inteligência artificial e visualização de dados. O objetivo é detectar antecipadamente possíveis falhas em equipamentos, reduzindo paradas inesperadas, otimizando manutenções e promovendo segurança operacional.

- **Coletar dados em tempo real via sensores IoT**;

- **Armazenar os dados em um banco de dados na nuvem;**
  
- **Processamento e Tratamento dos dados;**

- **Aplicar algoritmos de machine learning para predição de falhas;**

- **Visualização em dashboards interativos e simplificados;**

- **Notificar automaticamente os funcionários via aplicativo;**


# <a name="c3"></a>3. Tecnologias Propostas/Planejadas


## Definição das Tecnologias Utilizadas

| Camada                   | Tecnologias                                         |
|--------------------------|-----------------------------------------------------|
| **Sensoriamento**        | ESP32                                               |
| **Armazenamento**        | PostgreSQL                        |
| **Backend e APIs**       | Python, tratamentos de dados e serviços.            |
| **IA / Machine Learning**| TensorFlow                                          |
| **Infraestrutura**       | AWS                                                 |


# <a name="c4"></a>4. Pipeline de Dados

**Sensores IoT captam dados:**
- Vibração anormal;
- Temperatura excessiva;
- Umidade;
- Energia.

**Salvar dados brutos**
- Dados coletados pelos sensores são enviados ao servidor de ingestão.
- A API "Coletar Dados" armazena essas informações no banco de dados hospedado em nuvem.

**Limpeza e tratamento**
- Realiza pré-processamento e normalização;
- Remoção de dados nulos ou ausentes;
- Correção de dados inválidos;
- Prepara os dados para análise preditiva e visualização;

**Análise preditiva com Machine Learning**
- Utiliza modelos de aprendizado de máquina treinados com dados históricos dos sensores.
- Os modelos analisam padrões de comportamento das máquinas para prever:
  - Possíveis falhas;
  - Anomalias operacionais;
  - Níveis de risco e desgaste.
- Essa etapa tem o objetivo de antecipar manutenções e reduzir paradas não planejadas.
- Frameworks utilizados:  `TensorFlow`.

**Visualização dos Dados em Dashboards**
- Os dados preditivos gerados pelos modelos de machine learning são utilizados para construção de dashboards visuais.
- Os dashboards são desenvolvidos com as tecnologias **R** e **Python**, oferecendo uma interface intuitiva para equipe técnica.

**Informações exibidas:**
- Status dos sensores em tempo real;
- Alertas de risco preditivo;
- Histórico de desempenho das máquinas;
- Recomendações de manutenção preventiva.

**Notificações e Resposta Operacional**
- Notificação automática via chatbot e aplicativos;
- Registro das ações realizadas pelos operadores em log para rastreabilidade;
- Feedback operacional para validação e aprendizado das predições;
- Previsão do impacto operacional da falha identificada;
- Transformação automática dos alertas em ordens de serviço priorizadas.


# <a name="c5"></a>5. Plano Inicial de Desenvolvimento


| Etapa | Atividade                            |
|-------|--------------------------------------|
| 1     | Escolha e simulação de sensores      |
| 2     | Criação das APIs                     | 
| 3     | Pipeline de ingestão de dados        | 
| 4     | Treinamento do modelo de IA          |
| 5     | Desenvolvimento de dashboards        | 
| 6     | Mensagens com NLP e voz              | 


# <a name="c6"></a>6. Diagrama

<p align="center">
<img src="diagrama.drawio (1).png" alt="Driagrama da solução"></a>
</p>
