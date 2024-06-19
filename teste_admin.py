import unittest
from admin import Admin
from acervo import Acervo
from aluno import Aluno
from bibliotecario import Bibliotecario

class TestAdmin(unittest.TestCase):
    
    def setUp(self):
        self.admin = Admin("admin@biblioteca.com", "senha_admin")
        self.acervo = {}
        self.usuarios = {}

    def test_adicionar_acervo(self):
        exemplar_a = Acervo(1, "George Orwell", "1984", 1949, "Ficção")
        resultado = self.admin.adicionar_acervo(self.acervo, exemplar_a)
        self.assertTrue(resultado)
        self.assertIn(1, self.acervo)

    def test_adicionar_acervo_existente(self):
        exemplar_a = Acervo(1, "George Orwell", "1984", 1949, "Ficção")
        self.admin.adicionar_acervo(self.acervo, exemplar_a)  # Adiciona o exemplar pela primeira vez
        resultado = self.admin.adicionar_acervo(self.acervo, exemplar_a)  # Tenta adicionar o mesmo exemplar novamente
        self.assertFalse(resultado)

    def test_remover_acervo(self):
        exemplar_a = Acervo(1, "George Orwell", "1984", 1949, "Ficção")
        self.admin.adicionar_acervo(self.acervo, exemplar_a)
        resultado = self.admin.remover_acervo(self.acervo, 1)
        self.assertTrue(resultado)
        self.assertNotIn(1, self.acervo)

    def test_listar_acervo(self):
        exemplar_a = Acervo(1, "George Orwell", "1984", 1949, "Ficção")
        exemplar_b = Acervo(2, "J.K. Rowling", "Harry Potter", 1997, "Fantasia")
        self.admin.adicionar_acervo(self.acervo, exemplar_a)
        self.admin.adicionar_acervo(self.acervo, exemplar_b)
        resultados = self.admin.listar_acervo(self.acervo)
        self.assertEqual(len(resultados), 2)

    def test_adicionar_usuario(self):
        resultado = self.admin.adicionar_usuario(self.usuarios, "aluno1@exemplo.com", "senha_aluno", "Aluno")
        self.assertTrue(resultado)
        self.assertIn("aluno1@exemplo.com", self.usuarios)

    def test_adicionar_usuario_existente(self):
        self.admin.adicionar_usuario(self.usuarios, "aluno1@exemplo.com", "senha_aluno", "Aluno")  # Adiciona o usuário pela primeira vez
        resultado = self.admin.adicionar_usuario(self.usuarios, "aluno1@exemplo.com", "senha_aluno", "Aluno")  # Tenta adicionar o mesmo usuário novamente
        self.assertFalse(resultado)

    def test_remover_usuario(self):
        self.admin.adicionar_usuario(self.usuarios, "aluno1@exemplo.com", "senha_aluno", "Aluno")
        resultado = self.admin.remover_usuario(self.usuarios, "aluno1@exemplo.com")
        self.assertTrue(resultado)
        self.assertNotIn("aluno1@exemplo.com", self.usuarios)

    def test_listar_usuarios(self):
        self.admin.adicionar_usuario(self.usuarios, "aluno1@exemplo.com", "senha_aluno", "Aluno")
        self.admin.adicionar_usuario(self.usuarios, "bibliotecario1@exemplo.com", "senha_bibliotecario", "Bibliotecario")
        resultados = self.admin.listar_usuarios(self.usuarios)
        self.assertEqual(len(resultados), 2)

    def test_consultar_acervo(self):
        exemplar_a = Acervo(1, "George Orwell", "1984", 1949, "Ficção")
        exemplar_b = Acervo(2, "J.K. Rowling", "Harry Potter", 1997, "Fantasia")
        self.admin.adicionar_acervo(self.acervo, exemplar_a)
        self.admin.adicionar_acervo(self.acervo, exemplar_b)
        resultados = self.admin.listar_acervo(self.acervo)
        self.assertEqual(len(resultados), 2)


if __name__ == '__main__':
    unittest.main()
