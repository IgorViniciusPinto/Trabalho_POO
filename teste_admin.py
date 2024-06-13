import unittest
from admin import Admin
from perfil_usuario import PerfilUsuario
from bibliotecario import Bibliotecario
from acervo import Acervo
from aluno import Aluno

class TestAdmin(unittest.TestCase):

    def setUp(self):
        # Configuração inicial para cada teste, se necessário
        self.admin = Admin("admin@biblioteca.com", "senha123")
        self.acervo = {
            1: Acervo(1, "Autor A", "Título A", 2021, "Ficção"),
            2: Acervo(2, "Autor B", "Título B", 2020, "História")
        }
        self.usuarios = {
            "aluno1@exemplo.com": Aluno("aluno1@exemplo.com", "senha456"),
            "bibliotecario1@exemplo.com": Bibliotecario("bibliotecario1@exemplo.com", "senha789")
        }

    def test_adicionar_acervo(self):
        print("\nTestando adição de exemplar ao acervo...")
        exemplar_c = Acervo(3, "Autor C", "Título C", 2022, "Aventura")
        resultado = self.admin.adicionar_acervo(self.acervo, exemplar_c)
        self.assertTrue(resultado)
        self.assertIn(3, self.acervo)
        print("Resultado esperado: True")
        print("Acervo após adição:", self.acervo)

    def test_adicionar_acervo_existente(self):
        print("\nTestando adição de exemplar já existente no acervo...")
        exemplar_b = Acervo(2, "Autor B", "Título B", 2020, "História")
        resultado = self.admin.adicionar_acervo(self.acervo, exemplar_b)
        self.assertFalse(resultado)
        print("Resultado esperado: False")

    def test_remover_acervo(self):
        print("\nTestando remoção de exemplar do acervo...")
        resultado = self.admin.remover_acervo(self.acervo, 2)
        self.assertTrue(resultado)
        self.assertNotIn(2, self.acervo)
        print("Resultado esperado: True")
        print("Acervo após remoção:", self.acervo)

    def test_listar_acervo(self):
        print("\nTestando listagem do acervo...")
        expected_output = "Código: 1, Título: Título A, Autor: Autor A, Ano: 2021, Gênero: Ficção, Status: Disponível"
        self.admin.listar_acervo(self.acervo)
        resultado = self.admin.listar_acervo(self.acervo)
        self.assertIn(expected_output, resultado)
        print("Resultado esperado encontrado na listagem:")
        print(expected_output)

    def test_consultar_acervo(self):
        print("\nTestando consulta ao acervo...")
        exemplares = list(self.acervo.values())
        self.admin.consultar_acervo(exemplares)

    def test_adicionar_usuario(self):
        print("\nTestando adição de usuário...")
        novo_aluno = Aluno("aluno2@exemplo.com", "senha789")
        resultado = self.admin.adicionar_usuario(self.usuarios, "aluno2@exemplo.com", "senha789", "Aluno")
        self.assertTrue(resultado)
        self.assertIn("aluno2@exemplo.com", self.usuarios)
        print("Resultado esperado: True")
        print("Usuários após adição:", self.usuarios)

    def test_adicionar_usuario_existente(self):
        print("\nTestando adição de usuário já existente...")
        resultado = self.admin.adicionar_usuario(self.usuarios, "aluno1@exemplo.com", "senha123", "Aluno")
        self.assertFalse(resultado)
        print("Resultado esperado: False")

    def test_remover_usuario(self):
        print("\nTestando remoção de usuário...")
        resultado = self.admin.remover_usuario(self.usuarios, "bibliotecario1@exemplo.com")
        self.assertTrue(resultado)
        self.assertNotIn("bibliotecario1@exemplo.com", self.usuarios)
        print("Resultado esperado: True")
        print("Usuários após remoção:", self.usuarios)

    def test_listar_usuarios(self):
        print("\nTestando listagem de usuários...")
        expected_output = "ID: {}, Email: aluno1@exemplo.com, Cargo: Aluno".format(self.usuarios["aluno1@exemplo.com"].get_ID_perfil_usuario())
        self.admin.listar_usuarios(self.usuarios)
        resultado = self.admin.listar_usuarios(self.usuarios)
        self.assertIn(expected_output, resultado)
        print("Resultado esperado encontrado na listagem:")
        print(expected_output)

    def test_consultar_usuario(self):
        print("\nTestando consulta de usuário...")
        resultado = self.admin.consultar_usuario(self.usuarios, "bibliotecario1@exemplo.com")
        print("Resultado da consulta:", resultado)

if __name__ == "__main__":
    unittest.main()
