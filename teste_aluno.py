from exemplar import ExemplarConcreto
from aluno import Aluno
import unittest

class TestAluno(unittest.TestCase):
    def setUp(self):
        print("\nConfigurando os testes para Aluno...")
        self.aluno = Aluno("aluno@teste.com", 123456)

        # Exemplares para teste
        self.exemplar1 = ExemplarConcreto(1, "João da Silva", "Python Avançado", 2020, "Tecnologia")
        self.exemplar2 = ExemplarConcreto(2, "Maria Oliveira", "Matemática Básica", 2019, "Educação")
        self.exemplar3 = ExemplarConcreto(3, "Carlos Drummond de Andrade", "Sentimento do Mundo", 1940, "Poesia")

        # Acervo de exemplares para consulta
        self.acervo = {
            1: [self.exemplar1],
            2: [self.exemplar2],
            3: [self.exemplar3]
        }

    def tearDown(self):
        print("Finalizando os testes para Aluno...")

    def test_adicionar_remover_livro(self):
        print("\nTeste de adição e remoção de livro:")

        # Adicionando livro
        print("Adicionando livro:")
        self.assertTrue(self.aluno.adicionar_livro({
            'titulo': self.exemplar1.get_titulo(),
            'autor': self.exemplar1.get_autor(),
            'codigo': self.exemplar1.get_codigo(),
            'dados_exemplar': self.exemplar1.to_string()
        }))

        # Listando livros em posse do aluno
        print("Listando livros em posse do aluno:")
        self.aluno.get_livros_com_aluno()

        # Removendo livro
        print("Removendo livro:")
        self.assertTrue(self.aluno.remover_livro(self.exemplar1.get_codigo()))

    def test_calculo_multa_devolucao_atrasada(self):
        print("\nTeste de cálculo de multa para devolução com atraso:")

        # Empréstimo do exemplar
        self.assertTrue(self.aluno.adicionar_livro({
            'titulo': self.exemplar1.get_titulo(),
            'autor': self.exemplar1.get_autor(),
            'codigo': self.exemplar1.get_codigo(),
            'dados_exemplar': self.exemplar1.to_string()
        }))

        # Simulando devolução com atraso
        print(f"Simulando devolução com atraso para o exemplar '{self.exemplar1.get_titulo()}':")
        self.aluno.remover_livro(self.exemplar1.get_codigo())  # Devolve o livro

        # Validar se houve multa
        # Re-implementar esta parte conforme a lógica de multa do seu sistema

    def test_consulta_acervo(self):
        print("\nTeste de consulta de acervo:")

        # Consulta acervo completo
        print("Consulta acervo completo:")
        self.aluno.consultar_acervo(self.acervo)

        # Consulta acervo por título contendo 'Python'
        print("Consulta acervo por título contendo 'Python':")
        self.aluno.consultar_acervo(self.acervo, titulo="Python")

    def test_salvar_usuario(self):
        print("\nTeste de salvamento de usuário:")
        
        # Salvar usuário
        self.aluno.salvar_usuario()
        print("Usuário salvo com sucesso.")

if __name__ == "__main__":
    unittest.main()
