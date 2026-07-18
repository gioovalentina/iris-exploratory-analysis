# 🌸 Iris Exploratory Data Analysis

Análise exploratória do dataset Iris utilizando Python, Pandas,
Seaborn, Plotly e Streamlit.

## Objetivo

Identificar diferenças entre as espécies Setosa, Versicolor e
Virginica por meio de estatísticas descritivas e visualizações.

## Aplicação

Acesse o dashboard:

[🔗 Iris Exploratory Data Analysis](https://gioovalentina-iris-exploratory-analysis-app-maukyk.streamlit.app/)

## Dataset

O dataset contém 150 observações e quatro medidas:

- Comprimento da sépala
- Largura da sépala
- Comprimento da pétala
- Largura da pétala

A variável alvo possui três espécies:

- Setosa
- Versicolor
- Virginica

## Tecnologias

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Scikit-learn
- Streamlit

## Etapas da análise

1. Carregamento dos dados
2. Verificação da estrutura
3. Análise de valores ausentes
4. Estatísticas descritivas
5. Análise das distribuições
6. Comparação entre espécies
7. Análise de correlação
8. Visualizações multivariadas
9. PCA
10. Desenvolvimento do dashboard

## Principais resultados

- A espécie Setosa é facilmente separada das demais.
- Versicolor e Virginica apresentam alguma sobreposição.
- As medidas das pétalas são mais informativas.
- Comprimento e largura da pétala possuem forte correlação.

## Como executar

Clone o repositório:

```bash
git clone https://github.com/gioovalentina/iris-exploratory-analysis.git
```

Entre na pasta:
```bash
cd iris-exploratory-analysis
```

Crie o ambiente virtual:
```bash
python -m venv .venv
```

Ative no Windows:
```bash
.venv\Scripts\activate
```

Instale as dependências:
```bash
pip install -r requirements.txt
```

Execute:
```bash
streamlit run app.py
```

## Autor
Giovanna Valentina Esteves
