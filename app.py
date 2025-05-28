import pandas as pd
import streamlit as st
import plotly.express as px

vehiculos = pd.read_csv('vehicles_us.csv')

st.header('Venta de vehiculos')

# Mostrar el DataFrame como una tabla interactiva
st.subheader('Tabla de datos generales')
st.dataframe(vehiculos)

# Separador visual
st.markdown("---")

hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer click en el boton
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(vehiculos, x="model_year")

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
