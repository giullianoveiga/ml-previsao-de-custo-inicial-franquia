import streamlit as st  # Importa a biblioteca Streamlit para criar apps web interativos
import pandas as pd
from sklearn.linear_model import LinearRegression  # Importa o modelo de regressão linear do scikit-learn
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error  # Importa métricas de avaliação
import plotly.graph_objs as go  # Importa Plotly para gráficos interativos

st.set_page_config(page_title="Previsão de Custos de Franquia", layout="wide", page_icon="💸")
st.sidebar.title("Menu")
st.sidebar.info("Preencha os campos para prever o custo inicial de uma franquia. Você pode inserir um valor anual.")

tabs = st.tabs(["Dashboard", "Sobre o Desenvolvedor"])
tab_dashboard = tabs[0]
tab_dev = tabs[1]

with tab_dashboard:
    st.title("Previsão Inicial de Custo para Franquia")  # Título do app na interface web
    st.markdown("""
    Esta aplicação utiliza regressão linear para prever o custo inicial de abertura de uma franquia com base no valor anual da franquia. Você pode visualizar os dados, analisar o gráfico interativo e conferir as métricas do modelo.
    """)

    dados = pd.read_csv("dataset.csv", sep=";")  # Lê os dados do arquivo CSV padrão

    X = dados[['FrqAnual']]  # Seleciona a coluna de valor anual da franquia como variável independente
    y = dados['CusInic']  # Seleciona a coluna de custo inicial como variável dependente

    modelo = LinearRegression().fit(X, y)  # Treina o modelo de regressão linear
    prev_treino = modelo.predict(X)

    col1, col2 = st.columns([1,2])  # Layout mais amplo para gráfico

    with col1:
        st.subheader("Amostra dos Dados")
        st.dataframe(dados.head(15))

    with col2:
        st.subheader("Gráfico Interativo")
        trace_dados = go.Scatter(x=X['FrqAnual'], y=y, mode='markers', name='Dados reais', marker=dict(color='blue'))
        trace_regressao = go.Scatter(x=X['FrqAnual'], y=prev_treino, mode='lines', name='Regressão Linear', line=dict(color='red'))
        layout = go.Layout(title='Dispersão e Regressão Linear', xaxis=dict(title='Valor Anual da Franquia'), yaxis=dict(title='Custo Inicial'))
        fig = go.Figure(data=[trace_dados, trace_regressao], layout=layout)
        st.plotly_chart(fig, use_container_width=True)
        
    # Exibe métricas do modelo
    st.header("Métricas do Modelo de Regressão Linear")
    col3, col4, col5 = st.columns(3)
    col3.metric("R²", f"{r2_score(y, prev_treino):.3f}", help="Coeficiente de determinação")
    col4.metric("Erro Médio Absoluto (MAE)", f"{mean_absolute_error(y, prev_treino):.2f}")
    col5.metric("Erro Quadrático Médio (MSE)", f"{mean_squared_error(y, prev_treino):.2f}")


st.sidebar.header("Faça uma Previsão")
novo_valor = st.sidebar.number_input("Insira Novo Valor Anual", min_value=1.0, max_value=999999.0, value=1500.0, step=0.01)
processar = st.sidebar.button("Processar Previsão")

if processar:
    dados_novo_valor = pd.DataFrame([[novo_valor]], columns=['FrqAnual'])
    prev = modelo.predict(dados_novo_valor)
    st.success(f"Para {novo_valor:.2f} Reais, a Previsão de Custo Inicial é de {prev[0]:.2f} Reais")


with tab_dev:
    st.subheader("Sobre o Desenvolvedor")
    st.markdown("""
    ## Giulliano Veiga

    - Cientista de Dados
    - WhatsApp: [+55 85 98170-8027](https://wa.me/5585981708027)
    - Instagram: [@giullianoveiga](https://instagram.com/giullianoveiga)
    - GitHub: [giullianoveiga](https://github.com/giullianoveiga)
    - LinkedIn: [Giulliano Veiga](https://www.linkedin.com/in/giulliano-veiga/)
    """)
