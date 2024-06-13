from perfil_usuario import PerfilUsuario
from typing import Optional

class Bibliotecario(PerfilUsuario):
    def __init__(self, email:str, senha:int) -> None:
        # Inicializa o objeto Bibliotecario com email e senha.
        super().__init__(email, senha)
        self._papel = "Bibliotecario"

    def consultar_acervo(self, acervo, titulo: Optional[str]=None) -> None:
        # Consulta o acervo para encontrar livros pelo título.
        if titulo:
            for exemplares in acervo.values():
                for exemplar in exemplares:
                    if titulo.lower() in exemplar.get_titulo().lower():
                        print(f"Código: {exemplar.get_codigo()}, Título: {exemplar.get_titulo()}, Autor: {exemplar.get_autor()}, Ano: {exemplar.get_ano_publicacao()}, Gênero: {exemplar.get_genero()}")
        else:
            for exemplares in acervo.values():
                for exemplar in exemplares:
                    print(f"Código: {exemplar.get_codigo()}, Título: {exemplar.get_titulo()}, Autor: {exemplar.get_autor()}, Ano: {exemplar.get_ano_publicacao()}, Gênero: {exemplar.get_genero()}")

    # Salva os dados do usuário em um arquivo.
    def salvar_usuario(self) -> None:
        try:
            with open('usuarios.txt', 'a') as file:
                file.write(f'{self.get_ID_perfil_usuario()}, {self.get_email_perfil_usuario()}, {self.get_senha_perfil_usuario()}, {self.get_papel_usuario()}\n')
        except IOError as e:
            print(f"Erro ao salvar o usuário: {e}")

    # Adiciona um exemplar ao acervo.
    def adicionar_acervo(self, acervo, exemplar) -> None:
        try:
            if exemplar.codigo not in acervo:
                acervo[exemplar.codigo] = exemplar
                print("Exemplar adicionado com sucesso ao acervo.")
            else:
                print("Exemplar já existe no acervo.")
        except Exception as e:
            print(f"Erro ao adicionar exemplar ao acervo: {e}")

    def remover_acervo(self, acervo, codigo:int) -> None:
        # Remove um exemplar do acervo.
        try:
            if codigo in acervo:
                del acervo[codigo]
                print("Exemplar removido com sucesso do acervo.")
            else:
                print("Exemplar não encontrado no acervo.")
        except Exception as e:
            print(f"Erro ao remover exemplar do acervo: {e}")
