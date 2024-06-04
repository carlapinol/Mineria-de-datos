import os
import pandas as pd
import csv
from IPython.display import display

# Función para cargar y leer archivos CSV en DataFrames
def cargar_archivos():
    # Solicitar al usuario que ingrese la ruta del directorio
    ruta_directorio = input("Por favor, ingresa la ruta del directorio donde se encuentran los archivos CSV: ")
    
    # Verificar si la ruta es válida
    if not os.path.isdir(ruta_directorio):
        print("La ruta proporcionada no es válida.")
        return None
    
    archivos_csv = [archivo for archivo in os.listdir(ruta_directorio) if archivo.endswith('.csv')]
    
    if not archivos_csv:
        print("No se encontraron archivos CSV en el directorio proporcionado.")
        return None
    
    dataframes = {}  # Diccionario para almacenar los DataFrames
    for i, archivo in enumerate(archivos_csv):
        df_name = f'df{i + 1}'
        # Construir la ruta completa al archivo
        archivo_ruta = os.path.join(ruta_directorio, archivo)
        # Detectar automáticamente el delimitador del archivo CSV
        with open(archivo_ruta, 'rb') as file:
            dialect = csv.Sniffer().sniff(file.read(1024).decode('utf-8', errors='replace'))
            delimitador = dialect.delimiter
        # Leer el archivo CSV en un DataFrame
        df = pd.read_csv(archivo_ruta, delimiter=delimitador)
        # Almacenar el DataFrame en el diccionario
        dataframes[df_name] = df
        # Mostrar los primeros registros del DataFrame
        print(f"\nArchivo '{archivo}' cargado como '{df_name}':\n")
        display(df.head())

    return dataframes  # Devolver el diccionario con los DataFrames
