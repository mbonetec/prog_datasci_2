**Análisis de la base de datos The Movie Database (TMDB)**

**REPOSITORIO**

Este repositorio contiene código y recursos para realizar análisis del contenido de la base de datos The Movie Database (TMDB) para la compañia de medios de comunicación Open Broadcast Corporation, ya que se está planteando adquirir licencias de emisión de programas de televisión populares con las que espera aumentar significativamente el número de suscriptores.

Para comenzar con este proyecto, sigue los siguientes pasos: 
git clone https://github.com/mbonetec/prog_mbc.git

Navega al directorio del proyecto:
cd prog_mbc

Instala las dependencias necesarias:
pip install -r requirements.txt

Abre pycharm y ejecuta el análisis: 
El script principal para realizar el análisis es main.py

Los resultados del análisis se mostrarán en la consola.

**Estructura del Proyecto:**
El repositorio tiene la siguiente estructura:
README.md: Archivo que presenta el proyecto y explica como ejecutarlo.
SRC: Carpeta con los scripts del analisis.
  main.py: El script principal para el análisis. 
  lectura.py: Las funciones del ejercicio 1 para la descompresion y la lectura de datos.
  procesamiento_datos.py: Las funciones del ejercicio 2 para el procesado de datos.
  filtrado_datos.py: Las funciones del ejercicio 3 para el filtrado de datos.
  analisis_grafico.py: Las funciones del ejercicio 4 para el análisis gráfico.
requirements.txt: Un archivo de texto que especifica las dependencias de Python requeridas para el proyecto. 
Data: La carpeta con el zip de datos de TMDB
Test: La carpeta con las funciones para realizar los test del proyecto.
  TestLectura.py
      Se verifica que tras descomproimir el zip se encuentran los archivos TMDB_info.csv, TMDB_distribution.csv y TMDB_overview.csv
      
  TestFiltrado.py
      Para las funciones filtra_ingles y filtra_japones verifica que retorna un dataframe.
      Para filtro ingles debe encontrar la serie 'The Act' entre los resultados.
      Para el filtro japones verifica que contenga la serie 'Naruto'.
      Para el filtro de canceladas verifica que retorne una lista y que además contenga la serie 'The Idol'. 

  TestProcesamiento.py
      Se verifica que la nueva columna se ha creado. 
      Se verifica que la serie 'Loki' tiene la nueva variable air_days de 35.0
      Verifica que el diccionario contiene las claves y valores esperados para la serie 'Game of Thrones'.
      
Licencia:
El código en este repositorio está bajo la Licencia MIT. Siéntete libre de usar y modificar el código.
