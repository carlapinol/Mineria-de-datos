import pandas as pd
from IPython.display import display
import numpy as np
import re

# Función para limpiar y analizar los datos
def limpiar_datos(dataframes):
    # Diccionario para mapear los valores de mes
    mapeo_mes = {
        "01": "Enero", "02": "Febrero", "03": "Marzo", "04": "Abril", "05": "Mayo", "06": "Junio",
        "07": "Julio", "08": "Agosto", "09": "Septiembre", "10": "Octubre", "11": "Noviembre", "12": "Diciembre"
    }

    # Diccionario para mapear los valores de trimestre
    mapeo_trimestre = {
        "1": "Trimestre 1", "2": "Trimestre 2", "3": "Trimestre 3", "4": "Trimestre 4"
    }

    # Solicitar al usuario que ingrese el año para el análisis
    while True:
        try:
            year = int(input("Por favor, introduce el año sobre el que deseas realizar el análisis: "))
            break
        except ValueError:
            print("Por favor, introduce un año válido.")

    # Realizar la limpieza de datos en todos los DataFrames
    for df_name, df in dataframes.items():
        # Si la columna de periodo existe y contiene datos relevantes, extraer año y mes/trimestre
        if "Periodo" in df.columns:
            # Convertir la columna "Periodo" a cadena primero
            df["Periodo"] = df["Periodo"].astype(str)

            # Extraer el año
            df["Año"] = df["Periodo"].str[:4]

            # Verificar la longitud de la columna "Periodo" y extraer mes o trimestre si corresponde
            if (df["Periodo"].str.len() == 7).any() & df["Periodo"].str.contains("M").any():
                df["Mes"] = df["Periodo"].str.extract(r'(M\d{1,2})', expand=False).str[1:].map(mapeo_mes)
                
            if (df["Periodo"].str.len() == 6).any() & df["Periodo"].str.contains("T").any():
                df["Trimestre"] = df["Periodo"].str.extract(r'(T\d{1})', expand=False).str[1:].map(mapeo_trimestre)

            # Eliminar la columna "Periodo"
            df.drop(columns=["Periodo"], inplace=True)

            # Filtrar los datos por año y mes/trimestre
            df_year = df[df["Año"].astype(int) == year]

            # Mostrar los datos filtrados
            print(f"\nDatos para el año {year} del DataFrame '{df_name}':")
            display(df_year)

            # Actualizar el DataFrame en el diccionario
            dataframes[df_name] = df_year

        else:
            print(f"No se encontró una columna 'Periodo' en el DataFrame '{df_name}'.")

    # Devolver el diccionario de DataFrames actualizado
    return dataframes

