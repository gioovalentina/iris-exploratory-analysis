import pandas as pd
import plotly.express as px
import streamlit as st
from sklearn.datasets import load_iris

st.set_page_config(
    page_title="Iris Data Explorer",
    page_icon="🌸",
    layout="wide"
)


@st.cache_data
def load_data():
    iris = load_iris(as_frame=True)
    df = iris.frame

    df.columns = [
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width",
        "target"
    ]

    df["species"] = df["target"].map({
        0: "setosa",
        1: "versicolor",
        2: "virginica"
    })

    return df.drop(columns="target")


df = load_data()

st.title("🌸 Iris Data Explorer")

st.markdown(
    """
    Aplicação interativa para explorar as diferenças entre as espécies
    **Setosa**, **Versicolor** e **Virginica**.
    """
)

st.sidebar.header("Filtros")

selected_species = st.sidebar.multiselect(
    "Selecione as espécies",
    options=df["species"].unique(),
    default=df["species"].unique()
)

filtered_df = df[df["species"].isin(selected_species)]

st.sidebar.header("Configuração do gráfico")

numeric_columns = [
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width"
]

column_labels = {
    "sepal_length": "Comprimento da sépala",
    "sepal_width": "Largura da sépala",
    "petal_length": "Comprimento da pétala",
    "petal_width": "Largura da pétala"
}

x_axis = st.sidebar.selectbox(
    "Variável do eixo X",
    options=numeric_columns,
    format_func=lambda column: column_labels[column],
    index=2
)

y_axis = st.sidebar.selectbox(
    "Variável do eixo Y",
    options=numeric_columns,
    format_func=lambda column: column_labels[column],
    index=3
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Número de flores",
    len(filtered_df)
)

col2.metric(
    "Espécies selecionadas",
    filtered_df["species"].nunique()
)

col3.metric(
    "Valores ausentes",
    int(filtered_df.isnull().sum().sum())
)

st.divider()

st.subheader("Visualização dos dados")

fig_scatter = px.scatter(
    filtered_df,
    x=x_axis,
    y=y_axis,
    color="species",
    hover_data=numeric_columns,
    labels=column_labels,
    title=(
        f"{column_labels[x_axis]} × "
        f"{column_labels[y_axis]}"
    )
)

st.plotly_chart(
    fig_scatter,
    use_container_width=True
)

left_column, right_column = st.columns(2)

with left_column:
    selected_measurement = st.selectbox(
        "Variável para o boxplot",
        options=numeric_columns,
        format_func=lambda column: column_labels[column]
    )

    fig_box = px.box(
        filtered_df,
        x="species",
        y=selected_measurement,
        color="species",
        labels={
            "species": "Espécie",
            selected_measurement: column_labels[selected_measurement]
        },
        title=f"{column_labels[selected_measurement]} por espécie"
    )

    st.plotly_chart(
        fig_box,
        use_container_width=True
    )

with right_column:
    fig_histogram = px.histogram(
        filtered_df,
        x=selected_measurement,
        color="species",
        marginal="box",
        labels={
            selected_measurement: column_labels[selected_measurement]
        },
        title=f"Distribuição de {column_labels[selected_measurement]}"
    )

    st.plotly_chart(
        fig_histogram,
        use_container_width=True
    )

st.subheader("Médias por espécie")

mean_table = (
    filtered_df
    .groupby("species")[numeric_columns]
    .mean()
    .round(2)
)

st.dataframe(
    mean_table,
    use_container_width=True
)

st.subheader("Matriz de correlação")

correlation = filtered_df[numeric_columns].corr()

fig_correlation = px.imshow(
    correlation,
    text_auto=".2f",
    aspect="auto",
    title="Correlação entre as medidas"
)

st.plotly_chart(
    fig_correlation,
    use_container_width=True
)

with st.expander("Visualizar dataset"):
    st.dataframe(
        filtered_df,
        use_container_width=True
    )

st.subheader("Principais conclusões")

st.markdown(
    """
    - A espécie **Setosa** apresenta pétalas menores e é facilmente separada.
    - A espécie **Virginica** possui, em média, as maiores pétalas.
    - **Versicolor** e **Virginica** apresentam alguma sobreposição.
    - As medidas das pétalas diferenciam melhor as espécies que as sépalas.
    - Comprimento e largura da pétala apresentam forte correlação.
    """
)