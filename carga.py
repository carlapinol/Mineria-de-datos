import os
import pandas as pd
import csv

# Función para cargar y leer archivos CSV en DataFrames
def cargar_datos(path):
    # Verificar si la ruta es válida
    if not os.path.isdir(path):
        print("La ruta proporcionada no es válida.")
        return None
    
    archivos_csv = [archivo for archivo in os.listdir(path) if archivo.endswith('.csv')]
    
    if not archivos_csv:
        print("No se encontraron archivos CSV en el directorio proporcionado.")
        return None

    # Ordenar los archivos por nombre
    archivos_csv.sort()
    
    dataframes = {}  # Diccionario para almacenar los DataFrames
    for i, archivo in enumerate(archivos_csv):
        df_name = f'df{i + 1}'
        archivo_ruta = os.path.join(path, archivo)
        # Detectar automáticamente el delimitador del archivo CSV
        with open(archivo_ruta, 'rb') as file:
            dialect = csv.Sniffer().sniff(file.read(1024).decode('utf-8', errors='replace'))
            delimitador = dialect.delimiter
        # Leer el archivo CSV en un DataFrame
        df = pd.read_csv(archivo_ruta, delimiter=delimitador)
        # Almacenar el DataFrame en el diccionario
        dataframes[df_name] = df

    return dataframes  # Devolver el diccionario con los DataFrames
