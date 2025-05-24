import streamlit as st
import pandas as pd
import plotly.express as px

vehiculos = pd.read_csv(
    'C:\\Users\\dell\\Downloads\\vehiculos\\vehiculos\\vehicles_us.csv')


hist_button = st.button('Histograma')  # crear un botón

color = st.color_picker("Pick a color")

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(vehiculos, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Separador visual
st.markdown("---")

# Botón para el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

# Lógica para el gráfico de dispersión
if scatter_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    # Crear el gráfico de dispersión
    # Elige dos columnas numéricas para el gráfico de dispersión. Aquí usamos 'odometer' y 'price' como ejemplo.
    fig_scatter = px.scatter(vehiculos, x="odometer", y="price")
    st.plotly_chart(fig_scatter, use_container_width=True)
