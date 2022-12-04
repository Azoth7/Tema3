import streamlit as st
import pandas as pd
import plotly.express as px


data = pd.read_csv('https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv')

st.title("TEMA 3: Gráficas en Streamlit")
st.subheader("José Luis Quevedo Orrantia")
st.write('Desarrollo de un código sobre la estructura de una aplicación web que contenga 3 controles para la predicción de ventas de productos de Walmart en el noroeste de los Estados Unidos')


st.subheader("Gráfica: Histograma")


fig5 = px.histogram(data,x='State')

st.plotly_chart(fig5, use_container_width=True)


st.subheader("Gráfica: Pastel")

fig1 = px.pie(data, values='Sales', names='Ship Mode')

st.plotly_chart(fig1, use_container_width=True)


st.subheader("Gráfica: Barras")

fig3 = px.bar(data, x='City', y='Sales', color="Region")
st.plotly_chart(fig3, use_container_width=True)