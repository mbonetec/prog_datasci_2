from analisis_grafico import grafico_barras, grafico_lineas, grafico_circular
from filtrado_datos import filtra_ingles, filtra_canceladas, filtra_japones
from lectura import descomprimir_archivo, leer_csv_pandas, leer_con_csv, medir_tiempo_ejecucion
from procesamiento_datos import crear_variable, crear_diccionario

# EJERCICIO 1: DESCOMPRESION Y LECTURA DE FICHEROS.
print(" # # EJERCICIO 1  # # ")

# Ejercicio 1.1
archivo_a_descomprimir = 'data/TMDB.zip'
descomprimir_archivo(archivo_a_descomprimir)

# Ejercicio 1.2
archivos_csv_a_combinar = ['data/TMDB_info.csv', 'data/TMDB_overview.csv', 'data/TMDB_distribution.csv']
resultado, tiempo1 = medir_tiempo_ejecucion(leer_csv_pandas, archivos_csv_a_combinar)
df1 = resultado

# Ejercicio 1.3
resultado, tiempo2 = medir_tiempo_ejecucion(leer_con_csv, archivos_csv_a_combinar)
df2 = resultado

# Ejercicio 1.4
print("## DIFERENCIAS OBSERVADAS  ## ")
print("El tiempo empleando en ambas funciones es bastante similar.")
print("Para conjuntos de datos pequeños, conviene hacer uso de pandas")
print("Sin embargo, para archivos grandes, la libreria de csv es más eficiente")
print("ya que no carga todo el conjunto de datos en memoria a la vez.")

# EJERCICIO 2: PROCESAMIENTO DE DATOS.
print(" # # EJERCICIO 2  # # ")
# Ejercicio 2.1
dataframe = df1
nombre_variable = 'air_days'
opcion = 1
# llamo a la funcion de crear variable
data = crear_variable(dataframe, nombre_variable, opcion)
# Ordena el DataFrame por la columna "air_days" de forma descendente
data_ordenado = data.sort_values(by='air_days', ascending=False)

# Muestra los primeros 10 registros
primeros_10_registros = data_ordenado.head(10)

# Imprime los 10 primeros registros
print("Los 10 registros con más días de emisión:")
print(primeros_10_registros)

# Ejercicio 2.2
# Llama a la función para crear el diccionario
diccionario_resultante = crear_diccionario(df1)
diccionario_resultante_ordenado = dict(sorted(diccionario_resultante.items()))

# Muestra los primeros 5 registros del diccionario
print("Primeros 5 registros del diccionario ordenado:")
for nombre_serie, direccion_web_poster in list(diccionario_resultante_ordenado.items())[:5]:
    print(f"{nombre_serie}: {direccion_web_poster}")

# EJERCICIO 3: FILTRADO DE DATOS.
print(" # # EJERCICIO 3  # # ")
# Ejercicio 3.1
# Llama a la función para filtrar y mostrar los nombres de las series
df_ingles = filtra_ingles(data_ordenado)
print("Series cuyo idioma original es ingles y en cuyo resumen aparecen las palabras mystery o crime:")
print(df_ingles['name'])

# Ejercicio 3.2
# Llama a la función para filtrar y mostrar los nombres de las series canceladas
lista_canceladas = filtra_canceladas(data_ordenado)
# Muestra los primeros 20 elementos de la lista recuperada
print("Primeros 20 elementos de la lista de series de 2023 que han sido canceladas:")
print(lista_canceladas[:20])

# Ejercicio 3.3
# Llama a la función para filtrar y obtener el nuevo DataFrame
df_japones = filtra_japones(df1)
# Muestra los 20 primeros registros.
print("Primeros 20 registros del nuevo dataFrame de japones:")
print(df_japones.head(20))

# EJERCICIO 4: ANÁLISIS GRÁFICO
print(" # # EJERCICIO 4  # # ")
# Ejercicio 4.1
# Llama a la función para generar el gráfico de barras
barras = grafico_barras(df1)

# Ejercicio 4.2
# Llama a la función para generar el gráfico de lineas
lineas = grafico_lineas(df1)
print("Observaciones:")
print("A partir de la decada de los 80, se incrementa considerabelente el numero de series del tipo scripted")
print("Además a partir de los 2000 hay un pequeño aumento de las miniseries, los realitys y los documentales.")

# Ejercicio 4.3
# Llama a la función para generar el gráfico circular
circular = grafico_circular(df1)

