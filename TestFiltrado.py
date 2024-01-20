import unittest
import pandas as pd
from src.filtrado_datos import filtra_ingles, filtra_canceladas, filtra_japones
from src.lectura import leer_csv_pandas


class TestFiltrado(unittest.TestCase):
    def setUp(self):
        archivos_csv_a_combinar = \
            ['../data/TMDB_info.csv', '../data/TMDB_overview.csv', '../data/TMDB_distribution.csv']
        self.df = leer_csv_pandas(archivos_csv_a_combinar)

    def test_filtro_ingles(self):
        df_filtrado = filtra_ingles(self.df)

        # Verifica que df_filtrado es un dataframe
        self.assertIsInstance(df_filtrado, pd.DataFrame)

        # Verifica que al menos una fila en el DataFrame tiene el nombre 'The Act'
        nombre_serie = 'The Act'
        self.assertTrue(any(df_filtrado['name'] == nombre_serie),
                        f"No se encontró ninguna serie con el nombre '{nombre_serie}' en el resultado.")

    def test_filtro_canceladas(self):
        lista_canceladas = filtra_canceladas(self.df)

        # Verifica que lista_canceladas es una lista
        self.assertIsInstance(lista_canceladas, list)

        # Verifica que 'The Idol' está en la lista
        nombre_serie = 'The Idol'
        self.assertTrue(any(isinstance(serie, str) and serie == nombre_serie for serie in lista_canceladas),
                        f"No se encontró ninguna serie con el nombre '{nombre_serie}' en el resultado.")

    def test_filtro_japones(self):
        df_filtrado = filtra_japones(self.df)

        # Verifica que df_filtrado es un dataframe
        self.assertIsInstance(df_filtrado, pd.DataFrame)

        # Verifica que al menos una fila en el DataFrame tiene el nombre 'Naruto'
        nombre_serie = 'Naruto'
        self.assertTrue(any(df_filtrado['name'] == nombre_serie),
                        f"No se encontró ninguna serie con el nombre '{nombre_serie}' en el resultado.")


if __name__ == "__main__":
    unittest.main()
