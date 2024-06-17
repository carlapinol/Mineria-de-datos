import pandas as pd
import numpy as np
import re

def limpiar_dataframe(df, year=None, origin=None, destiny=None):
    # Hacer una copia del DataFrame para evitar modificar el original
    df = df.copy()
    
    # Diccionario para mapear los valores de mes
    mapeo_mes = {
        "01": "Enero", "02": "Febrero", "03": "Marzo", "04": "Abril", "05": "Mayo", "06": "Junio",
        "07": "Julio", "08": "Agosto", "09": "Septiembre", "10": "Octubre", "11": "Noviembre", "12": "Diciembre"
    }

    # Diccionario para mapear los valores de trimestre
    mapeo_trimestre = {
        "1": "Trimestre 1", "2": "Trimestre 2", "3": "Trimestre 3", "4": "Trimestre 4"
    }

    if "Periodo" in df.columns:
        # Convertir la columna "Periodo" a cadena primero
        df["Periodo"] = df["Periodo"].astype(str)

        # Extraer el año
        df["Año"] = df["Periodo"].str[:4]

        # Verificar la longitud de la columna "Periodo" y extraer mes o trimestre si corresponde
        if (df["Periodo"].str.len() == 7).any() and df["Periodo"].str.contains("M").any():
            df["Mes"] = df["Periodo"].str.extract(r'(M\d{1,2})', expand=False).str[1:].map(mapeo_mes)
                
        if (df["Periodo"].str.len() == 6).any() and df["Periodo"].str.contains("T").any():
            df["Trimestre"] = df["Periodo"].str.extract(r'(T\d{1})', expand=False).str[1:].map(mapeo_trimestre)

        # Eliminar la columna "Periodo"
        df.drop(columns=["Periodo"], inplace=True)

        # Filtrar los datos por año si se especifica
        if year is not None:
            if year > 2023:
                year = 2022  # Usamos 2022 como año predeterminado
            elif year < 1900 or year > 2023:
                raise ValueError("Por favor, introduce un año válido.")

            # Filtrar los datos por año
            df = df[df["Año"].astype(int) == year]

    # Encontrar todas las columnas que deben considerarse como "Origen"
    origen_cols = [col for col in df.columns if re.search(r'procedencia|residencia', col, re.IGNORECASE)]
    # Renombrar las columnas según el número de coincidencias
    if len(origen_cols) > 1:
        df.drop(columns=[origen_cols[0]], inplace=True)  # Eliminar la primera columna
        df.rename(columns={origen_cols[1]: 'Origen'}, inplace=True)
        df['Origen'] = df['Origen'].fillna('Total')  # Rellenar los valores nulos con 'Total'
    elif len(origen_cols) == 1:
        df.rename(columns={origen_cols[0]: 'Origen'}, inplace=True)
        df['Origen'] = df['Origen'].fillna('Total')  # Rellenar los valores nulos con 'Total'

    # Filtrar por el valor específico de origen si se proporciona
    if origin:
        if 'Origen' in df.columns:
            df = df[df['Origen'].str.contains(origin, case=False, na=False)]

    # Tratamiento de columnas de destino
    destino_cols = [col for col in df.columns if re.search(r'provincia|destino', col, re.IGNORECASE)]
    if destino_cols:
        if len(destino_cols) > 1:
            df.drop(columns=[destino_cols[0]], inplace=True)
        df.rename(columns={destino_cols[-1]: 'Destino'}, inplace=True)
        # Filtrar por destino específicos
        if destiny and 'Destino' in df.columns:
            df = df[df['Destino'].str.contains(destiny, case=False, na=False)]

    return df

def limpiar_datos(dataframes, year=None, origin=None, destiny=None):
    # Si se proporciona un solo DataFrame
    if isinstance(dataframes, pd.DataFrame):
        return limpiar_dataframe(dataframes, year, origin, destiny)

    # Si se proporciona un diccionario de DataFrames
    elif isinstance(dataframes, dict):
        dataframes_copiados = {df_name: limpiar_dataframe(df, year, origin, destiny) for df_name, df in dataframes.items() if isinstance(df, pd.DataFrame)}
        return dataframes_copiados

    else:
        raise ValueError("El argumento 'dataframes' debe ser un DataFrame o un diccionario de DataFrames.")


