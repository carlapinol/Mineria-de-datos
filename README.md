Este repositorio contiene scripts para la carga, limpieza y visualización de datos geoespaciales en España. Incluye datos de la carpeta `data` y un shapefile en la carpeta `spain` para generar mapas de calor.

## Cómo usar este proyecto

Para ver este proyecto ejecutado en Google Colab, simplemente haz clic en el siguiente enlace:

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Z6jszqkcaNDSDhDA-5np-itqsQf3V8Ps?usp=sharing)

## Uso del Chatbot MarIAno

Para facilitar el trabajo y la interacción con el proyecto, puedes usar el chatbot creado específicamente para este trabajo, llamado MarIAno. Puedes acceder a MarIAno a través del siguiente enlace:

[MarIAnito](https://chatgpt.com/g/g-W4KJ8mawg-mariano)

Este chatbot está diseñado para responder preguntas y proporcionar asistencia relacionada con los datos y scripts incluidos en este repositorio.

## Estructura del Proyecto

- `carga.py`: Script para cargar archivos CSV en DataFrames de pandas.
- `limpia.py`: Script para limpiar y analizar los datos cargados.
- `plotea.py`: Script para crear diferentes tipos de gráficos usando Plotly.
- `spain.py`: Script para generar mapas de calor de España utilizando datos geoespaciales.
- `data/`: Carpeta que contiene los archivos CSV con los datos.
- `spain/`: Carpeta que contiene el shapefile (`spain.shp`) y los archivos asociados.
- `Datos_turismo.ipynb`: Notebook que contine el codigo con la carga, limpieza y análisis de los datos.

## Requisitos

Asegúrate de tener instaladas las siguientes bibliotecas antes de ejecutar los scripts:

- pandas
- numpy
- geopandas
- matplotlib
- plotly

Puedes instalar las dependencias usando pip:

```bash
pip install pandas numpy geopandas matplotlib plotly
```

## Uso de los Scripts

### 1. Cargar Datos

El script `carga.py` carga archivos CSV en DataFrames de pandas. Independientemente de su separador.

```python
form carga import cargar_datos

dataframes_cargados = cargar_datos("ruta/al/directorio/data")
```

### 2. Limpiar y Analizar Datos

El script `limpia.py` limpia y analiza los datos cargados. Puedes especificar filtros por año, origen y destino.

```python
from limpia import limpiar_datos

# Ejemplo de uso
resultados = limpiar_datos(dataframes_cargados, year=2022, origin='Navarra', destiny='Alicante')
```

### 3. Crear Gráficos

El script `plotea.py` crea diferentes tipos de gráficos usando Plotly.

```python
from plotea import plotear_datos

# Ejemplo de uso
data = pd.DataFrame({
    'Comunidad': ['Andalucía', 'Aragón', 'Asturias', 'Balears', 'Canarias'],
    'Total': ['6,85', '2,88', '0,99', '1,15', '0,61']
})
plotear_datos(data, x='Comunidad', y='Total', title='Contribución de Comunidades', xlabel='Comunidad', ylabel='Total', chart_type='bar')
```

### 4. Generar Mapas de Calor

El script `spain.py` genera mapas de calor de España utilizando el shapefile proporcionado, en Matplotlib o Plotly.

```python
from spain import spain_heat_map

# Generar datos aleatorios
num_regions = 18  # Asegúrate de que este número coincida con el número de regiones en tu shapefile
data = np.random.randint(1, 100, num_regions)

# Ruta al directorio donde está la carpeta 'spain'
path = "ruta/al/directorio"

# Parámetros de la función
cmap = "autumn"
title = "Mapa de Calor de España"

# Llamar a la función con datos aleatorios
spain_heat_map(data, path, cmap, title, plot_type="matplotlib")
```

## Instrucciones Adicionales

1. **Clonar el Repositorio**:
   ```bash
   git clone https://github.com/carlapinol/Mineria-de-datos
   cd Mineria-de-datos
   ```

2. **Ejecutar los Scripts**:
   - Asegúrate de tener todos los archivos CSV en la carpeta `data` y el shapefile en la carpeta `spain`.
   - Modifica las rutas y parámetros según sea necesario en los ejemplos de uso.

3. **Notas Importantes**:
   - Los datos en los scripts de ejemplo deben coincidir con el número de regiones en el shapefile para que el gráfico se genere correctamente.
   - Ajusta las rutas y parámetros según tus necesidades.
