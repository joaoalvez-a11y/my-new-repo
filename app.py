import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("vehicles.csv")

df["is_4wd"] = df["is_4wd"].fillna(0)

st.header("Dashboard de Análise de Veículos Usados")

st.write("""
Esta aplicação foi desenvolvida para funcionários de uma empresa fictícia  do mercado automotivo.

O objetivo é permitir a consulta e comparação de anúncios de veículos usados,
ajudando na análise de preços, quilometragem, ano do modelo, condição e características dos veículos.
""")

st.subheader("Filtros")

show_4wd = st.checkbox("Mostrar apenas veículos 4x4")

if show_4wd:
    df_filtered = df[df["is_4wd"] == 1]
else:
    df_filtered = df

st.subheader("Distribuição dos preços dos veículos")

df_price = df_filtered[df_filtered["price"] <= 16839] # Filtrando preços até US$ 16.839, que é o valor até 75% dos preços, para evitar distorção causada por outliers

fig_price = px.histogram(
    df_price,
    x="price",
    nbins=50,
    title="Distribuição dos preços até US$ 20.000",
    labels={"price": "Preço"}
)

st.plotly_chart(fig_price)

st.subheader("Relação entre preço e quilometragem")

df_scatter = df_filtered[
    (df_filtered["price"] <= 16839) &
    (df_filtered["odometer"] <= 100000)
]

fig_scatter = px.scatter(
    df_scatter,
    x="odometer",
    y="price",
    color="condition",
    title="Preço x Quilometragem por condição do veículo",
    labels={
        "odometer": "Quilometragem",
        "price": "Preço",
        "condition": "Condição"
    }
)

st.plotly_chart(fig_scatter)