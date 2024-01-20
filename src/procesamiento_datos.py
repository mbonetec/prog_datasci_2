import pandas as pd


def crear_variable(dataframe, nombre_variable, opcion):
    """
    Segun la opcion recibida, realiza una accion con el dataframe y variable recibida.

    Args:
        dataframe (pd.DataFrame): El DataFrame a tratar.
        nombre_variable (str): El nombre de la variable.
        opcion (int): La opción par ala accion a realizar.
            Opciones: 1 - Calcula los dias de emision y agrega una nueva columna.

    Returns:
        pd.DataFrame: El DataFrame modificado con la nueva variable.
    """
    if opcion == 1:
        # nos aseguramos que las fechas están en formato datetime
        dataframe['first_air_date'] = pd.to_datetime(dataframe['first_air_date'])
        dataframe['last_air_date'] = pd.to_datetime(dataframe['last_air_date'])

        # Calculo de la diferencia en días y agrega la nueva columna al DataFrame
        dataframe[nombre_variable] = (dataframe['last_air_date'] - dataframe['first_air_date']).dt.days

    return dataframe


def crear_diccionario(dataframe):
    """
    Crea un diccionario con el nombre de la serie como clave y la dirección web completa de su poster como valor.

    Args:
        dataframe (pd.DataFrame): El DataFrame que contiene las columnas 'name', 'homepage', y 'poster_path'.

    Returns:
        dict: Un diccionario con el nombre de la serie y direccion completa del poster.
    """
    diccionario_series = {}

    for index, fila in dataframe.iterrows():
        nombre_serie = fila['name']
        homepage = fila['homepage']
        poster_path = fila['poster_path']

        # Concateno homepage y poster_path, y controla casos de NaN o ""
        if pd.notna(homepage) and pd.notna(poster_path) and homepage != "" and poster_path != "":
            direccion_web_poster = f"{homepage}{poster_path}"
        else:
            direccion_web_poster = "NOT AVAILABLE"

        diccionario_series[nombre_serie] = direccion_web_poster

    return diccionario_series
