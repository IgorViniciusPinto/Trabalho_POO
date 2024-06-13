import unittest
from bibliotecario import Bibliotecario
from acervo import Acervo  # Supondo que Acervo seja importado de um arquivo acervo.py

class TestBibliotecario(unittest.TestCase):

    def setUp(self):
        # Configuração inicial para cada teste, se necessário
        self.bibliotecario = Bibliotecario("bibliotecario@example.com", "senha123")

    def test_consultar_acervo_sem_filtro(self):
        # Testa a consulta de todo o acervo sem filtros
        biblioteca = {
            '001': [Acervo(1, "Autor A", "Livro A", 2020, "Ficção"), Acervo(2, "Autor B", "Livro B", 2019, "História")],
            '002': [Acervo(3, "Autor C", "Livro C", 2021, "Biografia")]
        }
        print("Teste de consulta de acervo sem filtro:")
        self.bibliotecario.consultar_acervo(biblioteca)
        print()

    def test_consultar_acervo_com_filtro_titulo(self):
        # Testa a consulta do acervo filtrando por título
        biblioteca = {
            '001': [Acervo(1, "Autor A", "Livro A", 2020, "Ficção"), Acervo(2, "Autor B", "Livro B", 2019, "História")],
            '002': [Acervo(3, "Autor C", "Livro C", 2021, "Biografia")]
        }
        print("Teste de consulta de acervo com filtro por título:")
        self.bibliotecario.consultar_acervo(biblioteca, "Livro A")
        print()

    def test_adicionar_acervo(self):
        # Testa a adição de exemplar ao acervo
        acervo = {}
        exemplar = Acervo(1, "Novo Autor", "Novo Livro", 2023, "Fantasia")

        print("Teste de adição de exemplar ao acervo:")
        self.bibliotecario.adicionar_acervo(acervo, exemplar)
        print(f"Acervo após adição do exemplar:")
        for codigo, exemplar in acervo.items():
            print(f"  Código: {codigo}")
            print(f"    Título: {exemplar.get_titulo()}")
            print(f"    Autor: {exemplar.get_autor()}")
            print(f"    Ano: {exemplar.get_ano_publicacao()}")
            print(f"    Gênero: {exemplar.get_genero()}")
        print()

        self.assertIn(1, acervo)  # Verifica se o exemplar foi adicionado ao acervo

    def test_remover_acervo(self):
        # Testa a remoção de exemplar do acervo
        acervo = {
            1: Acervo(1, "Autor A", "Livro A", 2020, "Ficção"),
            2: Acervo(2, "Autor B", "Livro B", 2019, "História")
        }
        print("Teste de remoção de exemplar do acervo:")
        self.bibliotecario.remover_acervo(acervo, 1)
        print(f"Acervo após remoção do exemplar:")
        for codigo, exemplar in acervo.items():
            print(f"  Código: {codigo}")
            print(f"    Título: {exemplar.get_titulo()}")
            print(f"    Autor: {exemplar.get_autor()}")
            print(f"    Ano: {exemplar.get_ano_publicacao()}")
            print(f"    Gênero: {exemplar.get_genero()}")
        print()

        self.assertNotIn(1, acervo)  # Verifica se o exemplar foi removido do acervo

if __name__ == '__main__':
    unittest.main()
