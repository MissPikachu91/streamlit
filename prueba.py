import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

# Cargar los datos
data = pd.read_csv('MDAS-HVD_EVAL_1_Datos.csv')

# logo
logo ="https://assets.isu.pub/document-structure/230227151116-4673fcc5b4922b04cd2d36c66d5ace91/v1/b75dc761fb79305a7dce64a1673bf113.jpeg"

# Título de la aplicación
st.title('Análisis del conjunto de datos del Titanic')

# Descripción en el menú principal
st.markdown("""
Esta aplicación permite explorar el conjunto de datos del Titanic y visualizar diferentes análisis
interactivos según varios propósitos:

1. **Ver Relaciones**: Observa las relaciones entre diferentes variables.
2. **Ver Comparaciones**: Compara diferentes grupos de datos.
3. **Ver Composiciones**: Examina la composición de diferentes categorías.
4. **Ver Distribuciones**: Visualiza las distribuciones de las variables.

Utiliza las pestañas laterales para navegar por los diferentes tipos de análisis.
    """)

# Título de la aplicación con logo
st.sidebar.markdown("""
 <style>
    /* Estilo para el contenedor del logo */
    .logo-button {
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 10px;
        border: 2px solid #000; /* Puedes cambiar el color del borde */
        border-radius: 10px; /* Bordes redondeados */
        background-color: #f0f0f0; /* Color de fondo */
        text-decoration: none; /* Quitar subrayado de los enlaces */
        transition: background-color 0.3s, border-color 0.3s;
    }

    .logo-button:hover {
        background-color: #e0e0e0; /* Color de fondo al pasar el ratón */
        border-color: #666; /* Color del borde al pasar el ratón */
    }

    /* Estilo para la imagen del logo */
    .logo-img {
        max-width: 100%;
        height: auto;
    }
</style>
""", unsafe_allow_html=True)

# Título de la aplicación con logo
st.sidebar.markdown(f"""
<a class="logo-button" href="/">
<img src={logo} alt="Logo" class="logo-img">
</a>
""", unsafe_allow_html=True)

# Sidebar: Opciones de visualización
st.sidebar.title('Opciones de Visualización')
st.sidebar.write('Seleccione el gráfico que desea visualizar')
visualization = st.sidebar.selectbox('Tipo de gráfico:', ['Seleccione una opción', 'Relación', 'Comparación', 'Composición', 'Distribución'], index=0)

  


#### RELACIONES
def plot_heatmap(data):
    st.subheader('Mapa de Calor de Variables Numéricas')

    numeric_columns = data.select_dtypes(include=['int', 'float']).columns.tolist()

    # Calcular la matriz de correlación
    correlation_matrix = data[numeric_columns].corr()

    # Crear el mapa de calor interactivo con plotly
    fig = px.imshow(correlation_matrix, color_continuous_scale='Viridis',
                     labels=dict(x='Variables', y='Variables', color='Correlación'),
                     title='Mapa de Calor de Correlación')

    # Agregar los valores de correlación en cada celda del mapa de calor
    fig.update_traces(hovertemplate='Correlación: %{z:.2f}')

    st.plotly_chart(fig)

    
    

def plot_relationships_age_fare(data):
    st.subheader('Relación entre Edad y Tarifa pagada')

    # Ajustar el estilo del gráfico
    fig = px.scatter(data, x='Age', y='Fare',
                     title='Edad vs Tarifa pagada',
                     labels={'Age': 'Edad', 'Fare': 'Tarifa'})

    # Personalizar el eje y para mejorar la visibilidad de las etiquetas
    fig.update_yaxes(tickvals=[0, 50, 100, 150, 200, 250, 300], tickformat='$,.2f')

    # Personalizar los colores
    fig.update_traces(marker=dict(size=8, opacity=0.8),
                      marker_line=dict(width=1, color='DarkSlateGrey'))

    st.plotly_chart(fig)
    
    

def plot_gender_by_age(data):
    st.subheader('Cantidad de Mujeres y Hombres por Edad')

    # Calcular la cantidad de mujeres y hombres por edad
    gender_by_age = data.groupby(['Age', 'Sex']).size().unstack(fill_value=0).reset_index()

    # Crear el gráfico interactivo con Plotly
    fig = px.line(gender_by_age, x='Age', y=['female', 'male'],
                  labels={'value': 'Cantidad', 'variable': 'Género', 'Age': 'Edad'},
                  title='Cantidad de Mujeres y Hombres por Edad')

    st.plotly_chart(fig)




def plot_relationships(data):
    st.header('Visualización de Relaciones en el Titanic Dataset')
    
    plot_heatmap(data)

    plot_relationships_age_fare(data)
    
    plot_gender_by_age(data)






#opciones modulares
if visualization == 'Seleccione una opción':
#     display_data(data)
    pass
if visualization == 'Relación':
     plot_relationships(data)
if visualization == 'Comparación':
#]    plot_comparisons(data)
    pass
if visualization == 'Composición':
#     plot_composition(data)
    pass
if visualization == 'Distribución':
#     plot_distributions(data)
    pass