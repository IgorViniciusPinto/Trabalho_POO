import unittest
import os
from acervo import Acervo, GestorAcervo

class TestAcervo(unittest.TestCase):
    def test_emprestar_devolver_exemplar(self):
        exemplar = Acervo(1, "Autor Exemplo", "Título Exemplo", 2023, "Ficção")
        
        # Teste de empréstimo
        exemplar.set_emprestado(True)
        self.assertTrue(exemplar.is_emprestado())

        # Teste de devolução
        exemplar.set_emprestado(False)
        self.assertFalse(exemplar.is_emprestado())

    def test_serializacao_desserializacao(self):
        exemplar = Acervo(1, "Autor Exemplo", "Título Exemplo", 2023, "Ficção")
        exemplar_str = exemplar.to_string()
        
        exemplar_desserializado = Acervo.from_string(exemplar_str)
        self.assertEqual(exemplar_desserializado.get_codigo(), exemplar.get_codigo())
        self.assertEqual(exemplar_desserializado.get_autor(), exemplar.get_autor())
        self.assertEqual(exemplar_desserializado.get_titulo(), exemplar.get_titulo())
        self.assertEqual(exemplar_desserializado.get_ano_publicacao(), exemplar.get_ano_publicacao())
        self.assertEqual(exemplar_desserializado.get_genero(), exemplar.get_genero())

class TestGestorAcervo(unittest.TestCase):
    def setUp(self):
        # Cria um arquivo temporário com conteúdo CSV para o teste
        self.csv_content = """codigo,autor,titulo,ano_publicacao,genero,status
1,Autor A,Título A,2021,Ficção,Disponível
2,Autor B,Título B,2020,História,Emprestado
3,Autor C,Título C,2019,Biografia,Disponível"""
        self.csv_file = "temp_acervos.txt"
        with open(self.csv_file, "w", newline='', encoding='utf-8') as file:
            file.write(self.csv_content)

    def tearDown(self):
        # Remove o arquivo temporário após os testes
        if os.path.exists(self.csv_file):
            os.remove(self.csv_file)

    def test_adicionar_exemplar(self):
        gestor = GestorAcervo()
        exemplar1 = Acervo(1, "Autor A", "Título A", 2021, "Ficção")
        exemplar2 = Acervo(2, "Autor B", "Título B", 2020, "História")

        print("Teste de adição de exemplares ao acervo:")
        gestor.adicionar_exemplar(exemplar1)
        gestor.adicionar_exemplar(exemplar2)

        for codigo, exemplares in gestor.acervo.items():
            for exemplar in exemplares:
                print(f"  Código: {codigo}")
                print(f"    Autor: {exemplar.get_autor()}")
                print(f"    Título: {exemplar.get_titulo()}")
                print(f"    Ano de Publicação: {exemplar.get_ano_publicacao()}")
                print(f"    Gênero: {exemplar.get_genero()}")

        print()

        self.assertEqual(len(gestor.acervo), 2)

    def test_salvar_e_carregar_acervos(self):
        gestor = GestorAcervo()
        exemplar1 = Acervo(1, "Autor A", "Título A", 2021, "Ficção")
        exemplar2 = Acervo(2, "Autor B", "Título B", 2020, "História")

        gestor.adicionar_exemplar(exemplar1)
        gestor.adicionar_exemplar(exemplar2)

        print("Teste de salvar e carregar acervos:")
        # Salvando acervos
        gestor.salvar_acervos(self.csv_file)
        print(f"  Acervos salvos no arquivo: {self.csv_file}")

        # Criando um novo gestor para carregar os acervos do arquivo
        gestor2 = GestorAcervo()
        gestor2.carregar_acervos(self.csv_file)

        print("  Acervos carregados do arquivo:")
        for codigo, exemplares in gestor2.acervo.items():
            for exemplar in exemplares:
                print(f"  Código: {codigo}")
                print(f"    Autor: {exemplar.get_autor()}")
                print(f"    Título: {exemplar.get_titulo()}")
                print(f"    Ano de Publicação: {exemplar.get_ano_publicacao()}")
                print(f"    Gênero: {exemplar.get_genero()}")

        print()

        self.assertEqual(len(gestor2.acervo), 2)
        exemplar_carregado = gestor2.consultar_exemplar_por_codigo(1)
        self.assertIsNotNone(exemplar_carregado)
        self.assertEqual(exemplar_carregado.get_autor(), "Autor A")
        self.assertEqual(exemplar_carregado.get_titulo(), "Título A")
        self.assertEqual(exemplar_carregado.get_ano_publicacao(), 2021)
        self.assertEqual(exemplar_carregado.get_genero(), "Ficção")

if __name__ == '__main__':
    unittest.main()
