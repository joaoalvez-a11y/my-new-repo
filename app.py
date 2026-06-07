import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles.csv')

st.header('Dashboard de anúncios de veículos')

st.write('Este aplicativo permite visualizar dados de anúncios de veículos usados.')

hist_button = st.button('Criar histograma de quilometragem')

if hist_button:
    st.write('Distribuição da quilometragem dos veículos')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Criar gráfico de dispersão: preço x quilometragem')

if scatter_button:
    st.write('Relação entre preço e quilometragem dos veículos')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)