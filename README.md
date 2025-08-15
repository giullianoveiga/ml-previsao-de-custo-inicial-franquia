# Previsão de Custos para Abrir Franquia

Esta aplicação utiliza regressão linear para prever o custo inicial de abertura de uma franquia com base no valor anual da franquia. Desenvolvida com Streamlit, ela permite análise visual dos dados, geração de previsões e avaliação de métricas do modelo.

## Funcionalidades
- Visualização dos dados
- Gráfico interativo (Plotly)
- Previsão de custo inicial para novos valores
- Exibição de métricas do modelo (R², MAE, MSE)
- Layout moderno com sidebar e instruções

## Cenário Fictício

Imagine que você é um consultor de negócios e está ajudando uma rede de franquias a expandir para novas cidades. A rede quer saber quanto deve investir inicialmente para abrir uma unidade, considerando diferentes valores anuais de franquia. Com esta ferramenta, você pode:

1. Carregar os dados históricos de franquias já abertas.
2. Visualizar a relação entre o valor anual da franquia e o custo inicial.
3. Inserir o valor anual planejado para uma nova unidade e obter uma previsão do custo inicial.
4. Apresentar gráficos e métricas para embasar sua recomendação ao cliente.

## Como usar

1. Instale as dependências:
   ```bash
   pip install streamlit scikit-learn plotly pandas
   ```
2. Execute o app:
   ```bash
   streamlit run regressao-linear.py
   ```
3. Siga as instruções na interface para carregar dados, visualizar gráficos e gerar previsões.

## Exemplo de uso

- O cliente deseja abrir uma franquia com valor anual de R$ 2.000,00.
- Insira esse valor na sidebar e clique em "Processar Previsão".
- O app mostrará a estimativa do custo inicial, gráficos e métricas do modelo.

---

Desenvolvido por Giulliano Veiga - Cientista de Dados
Instagram: @giullianoveiga
Whatsapp: +5585981708027