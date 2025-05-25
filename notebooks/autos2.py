import pandas as pd
import streamlit as st
import plotly.express as px

# Cargar los datos
vehiculos = pd.read_csv(
    'C:\\Users\\dell\\Downloads\\vehiculos\\vehiculos\\vehicles_us.csv')

st.title('Venta de vehiculos')
st.header('Anuncios de venta de coches')

# Mostrar el DataFrame con selección habilitada
edited_df = st.data_editor(vehiculos, num_rows="dynamic")

# Obtener las filas seleccionadas (devuelve una lista de índices)
selected_indices = st.session_state.get("edited_df_rows", [])

st.subheader('Visualizaciones basadas en la selección')

# Casilla de verificación para el histograma de selección
mostrar_hist_seleccion_checkbox = st.checkbox(
    'Mostrar histograma de precios para la selección')

if mostrar_hist_seleccion_checkbox:
    if selected_indices:
        vehiculos_seleccionados_hist = vehiculos.loc[selected_indices]
        st.write(
            f"Mostrando histograma para {len(vehiculos_seleccionados_hist)} vehículos seleccionados.")
        fig_hist_seleccion = px.histogram(
            vehiculos_seleccionados_hist, x="model_year")
        st.plotly_chart(fig_hist_seleccion, use_container_width=True)
    else:
        st.write(
            "Selecciona filas en la tabla para ver el histograma correspondiente.")
        fig_hist_total = px.histogram(vehiculos, x="model_year")
        st.plotly_chart(fig_hist_total, use_container_width=True)

# Separador visual
st.markdown("---")

# Casilla de verificación para el diagrama de dispersión de selección
mostrar_scatter_seleccion_checkbox = st.checkbox(
    'Mostrar diagrama de dispersión (model_year vs. price) para la selección')

if mostrar_scatter_seleccion_checkbox:
    if selected_indices:
        vehiculos_seleccionados_scatter = vehiculos.loc[selected_indices]
        st.write("Creando diagrama de dispersión para los vehículos seleccionados.")
        fig_scatter_seleccion = px.scatter(
            vehiculos_seleccionados_scatter, x="model_year", y="price")
        st.plotly_chart(fig_scatter_seleccion, use_container_width=True)
    else:
        st.write(
            "Selecciona filas en la tabla para ver el diagrama de dispersión correspondiente.")
        fig_scatter_total = px.scatter(vehiculos, x="model_year", y="price")
        st.plotly_chart(fig_scatter_total, use_container_width=True)
