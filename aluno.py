from perfil_usuario import PerfilUsuario
from exemplar import Exemplar
from typing import Dict, List, Optional
import datetime

class Aluno(PerfilUsuario):
    MAX_LIVROS:int = 5  # Limite máximo de livros que um aluno pode emprestar

    def __init__(self, email:str, senha:int) -> None:
        # Inicializa um objeto Aluno com email e senha.
        super().__init__(email, senha)
        self._papel:str = "Aluno"
        self._livros_com_aluno: List[Dict[str, str]] = [] # Lista de dicionários que armazenam detalhes dos livros emprestados

    def consultar_acervo(self, acervo:Dict[int, List[Exemplar]], titulo: Optional[str]=None) -> None:
        # Consulta o acervo para encontrar livros pelo título.
        if titulo:
            found:bool = False
            for exemplares in acervo.values():
                for exemplar in exemplares:
                    if titulo.lower() in exemplar.get_titulo().lower():
                        found = True
                        print(f"Código: {exemplar.get_codigo()}, Título: {exemplar.get_titulo()}, Autor: {exemplar.get_autor()}, Ano: {exemplar.get_ano_publicacao()}, Gênero: {exemplar.get_genero()}")
            if not found:
                print("Livro não encontrado no acervo.")
        else:
            for exemplares in acervo.values():
                for exemplar in exemplares:
                    print(f"Código: {exemplar.get_codigo()}, Título: {exemplar.get_titulo()}, Autor: {exemplar.get_autor()}, Ano: {exemplar.get_ano_publicacao()}, Gênero: {exemplar.get_genero()}")

    def get_livros_com_aluno(self) -> None:
        # Lista os livros que o aluno possui emprestados.
        if self._livros_com_aluno:
            for livro in self._livros_com_aluno:
                print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Código: {livro['codigo']}")
        else:
            print("Você não possui livros emprestados no momento.")

    def adicionar_livro(self, livro:Dict[str, str]) -> bool:
        # Adiciona um livro à lista de livros emprestados pelo aluno.
        #Returns: bool: True se o livro foi adicionado com sucesso, False se o limite de livros foi atingido.
        if len(self._livros_com_aluno) >= Aluno.MAX_LIVROS:
            print("Você atingiu o limite máximo de livros emprestados.")
            return False
        else:
            self._livros_com_aluno.append(livro)
            print("Livro adicionado com sucesso.")
            return True

    def remover_livro(self, codigo_livro:int) -> bool:
        # Remove um livro da lista de livros emprestados pelo aluno.
        # Returns: bool: True se o livro foi removido com sucesso, False se o livro não foi encontrado.
        for livro in self._livros_com_aluno:
            if livro['codigo'] == codigo_livro:
                exemplar = Exemplar.from_string(livro['dados_exemplar'])
                if exemplar.is_emprestado():
                    data_devolucao = exemplar.get_data_emprestimo() + datetime.timedelta(days=7)
                    self.calcular_multa(data_devolucao)
                self._livros_com_aluno.remove(livro)
                print("Livro devolvido com sucesso.")
                return True
        print("Livro não encontrado na lista de livros emprestados.")
        return False

    def calcular_multa(self, data_devolucao:datetime.date) -> None:
        # Calcula a multa por atraso na devolução de um livro.
        data_atual = datetime.date.today()
        if data_atual > data_devolucao:
            dias_atraso:int = (data_atual - data_devolucao).days
            multa:float = dias_atraso * 0.50  # Cada dia de atraso tem uma multa de R$ 0,50
            print(f"Você está devolvendo o livro com {dias_atraso} dia(s) de atraso. Sua multa é de R${multa:.2f}.")
        else:
            print("Livro devolvido dentro do prazo. Sem multa.")

    def salvar_usuario(self) -> None:
        # Salva os dados do usuário em um arquivo.
        with open('usuarios.txt', 'a') as file:
            file.write(f'{self.get_ID_perfil_usuario()}, {self.get_email_perfil_usuario()}, {self.get_senha_perfil_usuario()}, {self.get_papel_usuario()}\n')
