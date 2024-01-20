import unittest
import os
from src.lectura import descomprimir_archivo, leer_csv_pandas, leer_con_csv, medir_tiempo_ejecucion


class TestLectura(unittest.TestCase):
    def test_descomprimir_zip(self):
        zip_file = "../data/TMDB.zip"
        descomprimir_archivo(zip_file)

        self.assertTrue(os.path.isfile("../data/TMDB_info.csv"))
        self.assertTrue(os.path.isfile("../data/TMDB_distribution.csv"))
        self.assertTrue(os.path.isfile("../data/TMDB_overview.csv"))

    def test_descomprimir_tar_gz(self):
        tar_gz_file = "../data/TMDB.tar.gz"
        descomprimir_archivo(tar_gz_file)

        self.assertTrue(os.path.isfile("../data/TMDB_info.csv"))
        self.assertTrue(os.path.isfile("../data/TMDB_distribution.csv"))
        self.assertTrue(os.path.isfile("../data/TMDB_overview.csv"))

    def test_tiempos(self):
        archivos_csv_a_combinar = \
            ['../data/TMDB_info.csv', '../data/TMDB_overview.csv', '../data/TMDB_distribution.csv']

        # tiempo de ejecución
        tiempo_csv = medir_tiempo_ejecucion(leer_con_csv, archivos_csv_a_combinar)

        # Verificar que la función devuelve un número
        self.assertIsInstance(tiempo_csv, (int, float), "leer_con_csv no devuelve un número.")


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLectura)
    unittest.TextTestRunner(verbosity=2).run(suite)
