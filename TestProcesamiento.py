import unittest
from src.procesamiento_datos import crear_variable, crear_diccionario
from src.lectura import leer_csv_pandas


class TestProcesamientoDatos(unittest.TestCase):
    def setUp(self):
        archivos_csv_a_combinar = \
            ['../data/TMDB_info.csv', '../data/TMDB_overview.csv', '../data/TMDB_distribution.csv']
        self.df = leer_csv_pandas(archivos_csv_a_combinar)

    def test_crear_variable_dias_emision(self):
        # Prueba para la función crear_variable con opción 1 (días de emisión)
        nombre_variable = 'air_days'
        opcion = 1

        # Llama a la función
        df_resultado = crear_variable(self.df.copy(), nombre_variable, opcion)

        # Verifica que la nueva columna se ha creado
        self.assertTrue(nombre_variable in df_resultado.columns)
        # Verifica que la serie 'Loki' tiene air_days de 35.0
        serie_loki = df_resultado[df_resultado['name'] == 'Loki']
        self.assertEqual(serie_loki['air_days'].iloc[0], 35.0)

    def test_crear_diccionario_posters(self):
        # Prueba para la función crear_diccionario
        diccionario_resultado = crear_diccionario(self.df.copy())

        # Verifica que el diccionario contiene las claves y valores esperados
        self.assertEqual(diccionario_resultado['Game of Thrones'],
                         'http://www.hbo.com/game-of-thrones/1XS1oqL89opfnbLl8WnZY1O1uJx.jpg')


if __name__ == "__main__":
    unittest.main()
