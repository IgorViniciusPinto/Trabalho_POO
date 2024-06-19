import unittest
import datetime
from exemplar import ExemplarConcreto

class TestExemplarConcreto(unittest.TestCase):

    def setUp(self):
        # Configuração inicial para cada teste, se necessário
        self.exemplar = ExemplarConcreto(1, "Autor Exemplo", "Título Exemplo", 2023, "Ficção")

    def test_emprestar_e_devolver(self):
        # Testa os métodos de empréstimo e devolução
        print("Teste de empréstimo e devolução:")
        print("Exemplar inicialmente disponível:", not self.exemplar.is_emprestado())
        
        self.exemplar.emprestar()
        print("Exemplar após empréstimo:", self.exemplar.is_emprestado())
        print("Data de empréstimo:", self.exemplar.get_data_emprestimo())

        self.exemplar.devolver()
        print("Exemplar após devolução:", not self.exemplar.is_emprestado())
        print("Data de empréstimo após devolução:", self.exemplar.get_data_emprestimo())
        print()

        self.assertFalse(self.exemplar.is_emprestado())  # Verifica se está disponível após devolução
        self.assertIsNone(self.exemplar.get_data_emprestimo())  # Verifica se data de empréstimo é None após devolução

    def test_calcula_multa_sem_atraso(self):
        # Testa o cálculo de multa sem atraso na devolução
        print("Teste de cálculo de multa sem atraso:")
        self.exemplar.emprestar()

        data_devolucao = datetime.date.today()  # Supondo que hoje é a data de devolução
        multa = self.exemplar.calcula_multa(data_devolucao)

        print(f"Multa calculada: R$ {multa:.2f}")
        print()

        self.assertEqual(multa, 0.0)  # Não deve haver multa sem atraso

    def test_calcula_multa_com_atraso(self):
        # Testa o cálculo de multa com atraso na devolução
        print("Teste de cálculo de multa com atraso:")
        self.exemplar.emprestar()

        data_devolucao = datetime.date.today() + datetime.timedelta(days=5)  # Devolução com 5 dias de atraso
        multa = self.exemplar.calcula_multa(data_devolucao)

        print(f"Multa calculada: R$ {multa:.2f}")
        print()

        self.assertEqual(multa, 10.0)  # Multa de R$ 2,00 por dia de atraso

    def test_calcula_data_devolucao(self):
        # Testa o cálculo da data de devolução
        print("Teste de cálculo da data de devolução:")
        self.exemplar.emprestar()

        data_devolucao = self.exemplar.calcula_data_devolucao()

        print(f"Data de devolução calculada: {data_devolucao}")
        print()

        self.assertEqual(data_devolucao, self.exemplar.get_data_emprestimo() + datetime.timedelta(days=7))  # Devolução em 7 dias

    def test_from_string(self):
        # Testa o método from_string para criar um exemplar a partir de uma string
        print("Teste do método from_string:")
        exemplar_str = "1,Autor Exemplo,Título Exemplo,2023,Ficção,True,2024-06-14"
        exemplar = ExemplarConcreto.from_string(exemplar_str)

        print("Exemplar criado a partir da string:")
        print(f"  Código: {exemplar.get_codigo()}")
        print(f"  Autor: {exemplar.get_autor()}")
        print(f"  Título: {exemplar.get_titulo()}")
        print(f"  Ano de Publicação: {exemplar.get_ano_publicacao()}")
        print(f"  Gênero: {exemplar.get_genero()}")
        print(f"  Emprestado: {exemplar.is_emprestado()}")
        print(f"  Data de Empréstimo: {exemplar.get_data_emprestimo()}")
        print()

        self.assertEqual(exemplar.get_codigo(), 1)
        self.assertEqual(exemplar.get_autor(), "Autor Exemplo")
        self.assertEqual(exemplar.get_titulo(), "Título Exemplo")
        self.assertEqual(exemplar.get_ano_publicacao(), 2023)
        self.assertEqual(exemplar.get_genero(), "Ficção")
        self.assertTrue(exemplar.is_emprestado())
        self.assertEqual(exemplar.get_data_emprestimo(), datetime.date(2024, 6, 14))

if __name__ == '__main__':
    unittest.main()
