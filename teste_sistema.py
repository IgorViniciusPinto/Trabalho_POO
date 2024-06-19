import unittest
from sistema import Sistema
from admin import Admin
from aluno import Aluno
from bibliotecario import Bibliotecario
from exemplar import ExemplarConcreto

class TesteSistema(unittest.TestCase):

    def setUp(self):
        # Configuração inicial para os testes
        self.sistema = Sistema()
        self.carregar_dados_teste()

    def carregar_dados_teste(self):
        # Dados de exemplo para testes
        self.sistema.biblioteca = {
            1001: [ExemplarConcreto(1001, "Autor 1", "Livro 1", 2020, "Aventura")],
            1002: [ExemplarConcreto(1002, "Autor 2", "Livro 2", 2021, "Ficção Científica")],
            1003: [ExemplarConcreto(1003, "Autor 3", "Livro 3", 2019, "Romance")]
        }

        self.sistema.usuarios = {
            "aluno@teste.com": Aluno("aluno@teste.com", "senha123"),
            "bibliotecario@teste.com": Bibliotecario("bibliotecario@teste.com", "senha456"),
            "admin@teste.com": Admin("admin@teste.com", "senha789")
        }

    def tearDown(self):
        # Limpeza após cada teste (opcional)
        pass

    def test_carregar_acervos(self):
        # Verifica se o carregamento inicial dos acervos ocorre corretamente
        self.assertIsNotNone(self.sistema.biblioteca)
        self.assertTrue(len(self.sistema.biblioteca) > 0)
        print("Teste de carregamento de acervos executado com sucesso.")

    def test_carregar_usuarios(self):
        # Verifica se o carregamento inicial dos usuários ocorre corretamente
        self.assertIsNotNone(self.sistema.usuarios)
        self.assertTrue(len(self.sistema.usuarios) > 0)
        print("Teste de carregamento de usuários executado com sucesso.")

    def test_login_aluno(self):
        # Testa o login e a interação do sistema como aluno
        aluno = self.sistema.usuarios["aluno@teste.com"]

        # Executa a interação como aluno
        self.sistema.tela_aluno(aluno)

        print(f"Teste de login e interação como aluno {aluno.get_email_perfil_usuario()} executado com sucesso.")

    def test_login_bibliotecario(self):
        # Testa o login e a interação do sistema como bibliotecário
        bibliotecario = self.sistema.usuarios["bibliotecario@teste.com"]

        # Executa a interação como bibliotecário
        with self.assertRaises(SystemExit):
            self.sistema.tela_bibliotecario(bibliotecario)

        print(f"Teste de login e interação como bibliotecário {bibliotecario.get_email_perfil_usuario()} executado com sucesso.")

    def test_criar_exemplar(self):
        # Testa a criação de um exemplar e a adição ao acervo
        exemplar = self.sistema.criar_exemplar(1004, "Autor 4", "Livro 4", 2022, "Suspense")

        # Verifica se o exemplar foi criado corretamente
        self.assertIsInstance(exemplar, ExemplarConcreto)
        self.assertIn(1004, self.sistema.biblioteca)
        self.assertIn(exemplar, self.sistema.biblioteca[1004])

        print("Teste de criação de exemplar e adição ao acervo executado com sucesso.")
        
    def test_login_admin(self):
        # Testa o login e a interação do sistema como admin
        admin = self.sistema.usuarios["admin@teste.com"]

        # Executa a interação como admin
        self.sistema.tela_admin(admin)

        print(f"Teste de login e interação como admin {admin.get_email_perfil_usuario()} executado com sucesso.")

if __name__ == "__main__":
    unittest.main()
