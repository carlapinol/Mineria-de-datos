import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def create_plot(data, x, y, title, xlabel, ylabel, chart_type, width=1000, height=600):
    """
    Crea un gráfico usando Plotly.

    Parameters:
    - data (DataFrame): El DataFrame que contiene los datos.
    - x (str): La columna a usar en el eje X.
    - y (str): La columna a usar en el eje Y.
    - title (str): El título del gráfico.
    - xlabel (str): La etiqueta del eje X.
    - ylabel (str): La etiqueta del eje Y.
    - chart_type (str): El tipo de gráfico ('line', 'histogram', 'bar', 'pie', 'scatter').
    - width (int): El ancho de la figura.
    - height (int): La altura de la figura.

    Returns:
    - fig: La figura Plotly generada.
    """
    
    # Limpiar los valores de la columna y
    data[y] = data[y].str.replace('.', '', regex=False).str.replace(',', '.', regex=False).astype(float)

    fig = None
    
    if chart_type == 'line':
        fig = px.line(data, x=x, y=y, title=title)
    elif chart_type == 'histogram':
        fig = px.histogram(data, x=x, y=y, title=title)
    elif chart_type == 'bar':
        fig = px.bar(data, x=x, y=y, title=title)
    elif chart_type == 'pie':
        fig = px.pie(data, names=x, values=y, title=title)
    elif chart_type == 'scatter':
        fig = px.scatter(data, x=x, y=y, title=title)
    else:
        raise ValueError("Tipo de gráfico no soportado: use 'line', 'histogram', 'bar', 'pie', 'scatter'")

    fig.update_layout(
        xaxis_title=xlabel,
        yaxis_title=ylabel,
        title=title,
        width=width,
        height=height
    )
    
    fig.show()
