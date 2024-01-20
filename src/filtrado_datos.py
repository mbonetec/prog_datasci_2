import pandas as pd


def filtra_ingles(dataframe):
    """
    Filtra y muestra las series cuyo idioma original es inglés y que contienen "mystery" o "crime" en el resumen.

    Args:
        dataframe (pd.DataFrame): El DataFrame a tratar.

    Returns:
        dataframe (pd.DataFrame): El DataFrame con los registros que coinciden.
    """
    # Filtra las series en inglés
    df_ingles = dataframe[dataframe['original_language'] == 'en']

    # Filtra las series que contienen las palabras "mystery" o "crime" en el resumen (overview)
    df_filtrado_en = df_ingles[df_ingles['overview'].str.lower().str.contains('mystery|crime', na=False)]

    return df_filtrado_en


def filtra_canceladas(dataframe):
    """
    Filtra y muestra las series que han comenzado en 2023 y han sido canceladas.

    Args:
        dataframe (pd.DataFrame): El DataFrame a tratar.

    Returns:
        list: Una lista de nombres de series que cumplen con los criterios.
    """
    try:
        # Filtra las series que han comenzado en 2023 y han sido canceladas
        df_filtrado = dataframe[(dataframe['first_air_date'].dt.year == 2023) & (dataframe['status'] == 'Canceled')]
    except AttributeError:
        # Si hay un error de atributo, intenta nuevamente convirtiendo la columna a tipo datetime
        dataframe['first_air_date'] = pd.to_datetime(dataframe['first_air_date'], errors='coerce')
        df_filtrado = dataframe[(dataframe['first_air_date'].dt.year == 2023) & (dataframe['status'] == 'Canceled')]

    # Obtiene la lista de nombres de series
    series_canceladas = list(df_filtrado['name'])

    return series_canceladas



def filtra_japones(dataframe):
    """
    Filtra y obtiene un nuevo DataFrame con información de series cuyo idioma incluye el japonés.

    Args:
        dataframe (pd.DataFrame): El DataFrame a tratar.

    Returns:
        pd.DataFrame: Un nuevo DataFrame con las columnas mencionadas de las series que cumplen con los criterios.
    """
    # Filtra las series cuyo idioma incluye el japonés
    df_filtrado = dataframe[dataframe['languages'].str.contains('ja', na=False)]

    # Obtiene un nuevo DataFrame con las columnas solicitadas
    df_resultado = df_filtrado[['name', 'original_name', 'networks', 'production_companies']]

    return df_resultado
