import pandas as pd
import matplotlib.pyplot as plt


def grafico_barras(dataframe):
    """
    Genera un gráfico de barras con el número de series por año de inicio.

    Args:
        dataframe (pd.DataFrame): El DataFrame a tratar.

    Returns:
        None
    """
    # Extrae el año de inicio de 'first_air_date'
    dataframe['year'] = pd.to_datetime(dataframe['first_air_date']).dt.year

    # Cuenta el número de series por año
    series_por_anyo = dataframe['year'].value_counts().sort_index()

    # Genera el gráfico de barras
    plt.figure(figsize=(12, 8))
    series_por_anyo.plot(kind='bar', color='skyblue')
    plt.title('Número de Series por Año de Inicio')
    plt.xlabel('Año de Inicio')
    plt.ylabel('Número de Series')
    plt.show()
    plt.savefig('graficas/grafico_barras.png')
    plt.close()  # Cierro la figura


def grafico_lineas(dataframe):
    """
    Genera un gráfico de líneas que muestra el número de series de cada categoría de la variable 'type'
    producidas en cada década desde 1940.

    Args:
        dataframe (pd.DataFrame): El DataFrame a tratar.

    Returns:
        None
    """
    # Extrae el año de inicio de 'first_air_date'
    dataframe['decada'] = (pd.to_datetime(dataframe['first_air_date']).dt.year // 10) * 10

    # Filtra las series desde 1940
    dataframe_filtrado = dataframe[dataframe['decada'] >= 1940]

    # Cuenta el número de series de cada categoría de 'type' por década
    series_por_decada = dataframe_filtrado.groupby(['decada', 'type']).size().unstack().fillna(0)

    # Genera el gráfico de líneas
    plt.figure(figsize=(12, 8))
    series_por_decada.plot(kind='line', marker='o')
    plt.title('Número de Series de cada Categoría por Década desde 1940')
    plt.xlabel('Década')
    plt.ylabel('Número de Series')
    plt.show()
    plt.savefig('graficas/grafico_lineas.png')
    plt.close()  # Cierro la figura


def grafico_circular(dataframe):
    """
    Genera un gráfico circular con el número de series por género y muestra el porcentaje respecto al total.

    Args:
        dataframe (pd.DataFrame): El DataFrame a tratar.

    Returns:
        None
    """
    # Elimina las filas con 'genres' vacío
    dataframe = dataframe[dataframe['genres'].notna()]

    # Separa los géneros y cuenta el número de series por género
    generos_series = dataframe['genres'].str.split(',').explode().str.strip()
    cuenta_generos = generos_series.value_counts()

    # Crea un nuevo DataFrame con los resultados
    df_generos = pd.DataFrame({'Genero': cuenta_generos.index, 'Numero_de_Series': cuenta_generos.values})
    df_generos['Porcentaje'] = (df_generos['Numero_de_Series'] / df_generos['Numero_de_Series'].sum()) * 100
    df_generos['genres_2'] = df_generos.apply(lambda row: row['Genero'] if row['Porcentaje'] >= 1 else 'Other', axis=1)

    df_generos2 = df_generos.drop('Genero', axis=1)

    # Agrupar por genres_2 y sumar las columnas
    df_other = df_generos2[df_generos2['genres_2'] == 'Other']
    df_other_agrupado = df_other.groupby('genres_2').agg({'Numero_de_Series': 'sum', 'Porcentaje': 'sum'}).reset_index()

    # Filtrar los registros que no son 'Other'
    df_generos_sin_other = df_generos2[df_generos2['genres_2'] != 'Other']

    # Concatenar los dos dataframes
    df_generos2_actualizado = pd.concat([df_generos_sin_other, df_other_agrupado])

    # Genera el gráfico circular con la columna 'genres_2' y porcentajes en la leyenda
    plt.figure(figsize=(10, 10))
    percentages = df_generos2_actualizado['Porcentaje']
    labels_2 = [f'{genre} ({percent:.1f}%)' for genre, percent in zip(df_generos2_actualizado['genres_2'], percentages)]
    plt.pie(df_generos2_actualizado['Numero_de_Series'], labels=None, autopct='', startangle=90, pctdistance=0.85,
            textprops={'fontsize': 10})
    plt.title('Número de Series por Género', fontsize=14)
    plt.legend(labels_2, loc='center left', bbox_to_anchor=(1, 0.5))

    plt.show()
    plt.savefig('graficas/grafico_circular.png')
    plt.close()  # Cierro la figura
