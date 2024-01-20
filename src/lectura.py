import os
import zipfile
import tarfile
import time
import pandas as pd



def descomprimir_archivo(ruta_archivo):
    """
    Descomprime un archivo en formato ZIP o tar.gz.

    Args:
        ruta_archivo (str): La ruta al archivo comprimido (ZIP o tar.gz).

    Raises:
        ValueError: Se genera si el formato del archivo no es ZIP ni tar.gz.
        FileNotFoundError: Se genera si el archivo no existe.
    """
    try:
        # Obtengo la extensión del archivo
        nombre_base, extension = os.path.splitext(ruta_archivo)

        # Descomprimo según la extensión
        if extension == '.zip':
            with zipfile.ZipFile(ruta_archivo, 'r') as zip_ref:
                zip_ref.extractall(os.path.dirname(ruta_archivo))
            print(f'Archivo {ruta_archivo} descomprimido correctamente.')

        elif extension == '.gz' and nombre_base.endswith('.tar'):
            with tarfile.open(ruta_archivo, 'r:gz') as tar_ref:
                tar_ref.extractall(os.path.dirname(ruta_archivo))
            print(f'Archivo {ruta_archivo} descomprimido correctamente.')

        else:
            raise ValueError(f'Error: El formato del archivo {ruta_archivo} no es compatible. '
                             'Solo se admiten archivos en formato ZIP o tar.gz.')
    except FileNotFoundError:
        print(f'Error: No se encontró el archivo {ruta_archivo}.')


def leer_csv_pandas(lista_rutas_csv):
    """
   Lee múltiples archivos CSV y los integra en un único DataFrame utilizando la columna "id" como clave.


   Args:
       lista_rutas_csv (list): Lista de rutas a los archivos CSV a leer y combinar.


   Returns:
       pd.DataFrame: Un DataFrame que integra los datos de todos los archivos CSV.
   """
    if not lista_rutas_csv:
        raise ValueError("La lista de rutas a archivos CSV está vacía.")

    # Leer el primer archivo CSV para obtener las columnas iniciales
    primer_df = pd.read_csv(lista_rutas_csv[0], encoding="latin-1")

    # Leer los DataFrames individuales y combinarlos por la columna "id"
    dfs = [pd.read_csv(archivo, encoding="latin-1") for archivo in lista_rutas_csv]

    # Verificar y manejar duplicados
    for df in dfs:
        if df['id'].duplicated().any():
            raise ValueError("Hay duplicados en la columna 'id' en al menos uno de los DataFrames.")

    # Verificar y manejar valores nulos en la columna 'id'
    for df in dfs:
        if df['id'].isnull().any():
            raise ValueError("Hay valores nulos en la columna 'id' en al menos uno de los DataFrames.")

    # Utilizar merge con how='inner' para combinar los DataFrames por la columna "id"
    df_combinado = primer_df
    for df in dfs[1:]:
        df_combinado = pd.merge(df_combinado, df, on='id', how='inner')

    return df_combinado


def leer_con_csv(lista_rutas_csv):
    """
   Lee múltiples archivos CSV y los integra en un único DataFrame utilizando la columna "id" como clave.


   Args:
       lista_rutas_csv (list): Lista de rutas a los archivos CSV a leer y combinar.


   Returns:
       pd.DataFrame: Un DataFrame que integra los datos de todos los archivos CSV.
   """
    if not lista_rutas_csv:
        raise ValueError("La lista de rutas a archivos CSV está vacía.")

    # Leer el primer archivo CSV para obtener las columnas iniciales
    primer_df = pd.read_csv(lista_rutas_csv[0], encoding="latin-1")

    # Leer los DataFrames individuales y combinarlos por la columna "id"
    dfs = [pd.read_csv(archivo, encoding="latin-1") for archivo in lista_rutas_csv]

    # Verificar y manejar duplicados
    for df in dfs:
        if df['id'].duplicated().any():
            raise ValueError("Hay duplicados en la columna 'id' en al menos uno de los DataFrames.")

    # Verificar y manejar valores nulos en la columna 'id'
    for df in dfs:
        if df['id'].isnull().any():
            raise ValueError("Hay valores nulos en la columna 'id' en al menos uno de los DataFrames.")

    # Utilizar merge con how='inner' para combinar los DataFrames por la columna "id"
    df_combinado = primer_df
    for df in dfs[1:]:
        df_combinado = pd.merge(df_combinado, df, on='id', how='inner')

    return df_combinado


def medir_tiempo_ejecucion(funcion, lista_rutas_csv):
    """
   Mide el tiempo de ejecución de una función.


   Args:
       funcion (function): La función a medir.
       lista_rutas_csv (list): Lista de rutas a los archivos CSV a pasar a la función.


   Returns:
       float: Tiempo de ejecución en segundos.
   """
    tiempo_inicial = time.time()

    # Llama a la función con los parámetros proporcionados
    resultado = funcion(lista_rutas_csv)

    tiempo_final = time.time()
    tiempo_ejecucion = tiempo_final - tiempo_inicial

    print(f"Tiempo de ejecución de {funcion.__name__}: {tiempo_ejecucion} segundos")

    return resultado, tiempo_ejecucion
