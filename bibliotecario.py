from perfil_usuario import PerfilUsuario
from typing import Dict, List, Any, Optional

class Bibliotecario(PerfilUsuario):
    def __init__(self, email: str, senha: str) -> None:
        # Inicializa o objeto Bibliotecario com email e senha.
        super().__init__(email, senha)
        self._cargo = "Bibliotecario"

    def consultar_acervo(self, biblioteca: Dict[str, List[Optional[Any]]], titulo: Optional[str] = None) -> None:
        # Consulta o acervo da biblioteca e imprime as informações dos exemplares.
        for codigo_acervo, exemplares in biblioteca.items():
            for exemplar in exemplares:
                if exemplar is not None and (titulo is None or exemplar.titulo.lower() == titulo.lower()):
                    print(f"Código: {codigo_acervo}, Título: {exemplar.titulo}, Autor: {exemplar.autor}, Ano: {exemplar.ano_publicacao}, Gênero: {exemplar.genero}")

    # Salva os dados do usuário em um arquivo.
    def salvar_usuario(self, filename: str = 'usuarios.txt') -> None:
        try:
            with open(filename, 'a') as file:
                file.write(f'{self.ID_perfil_usuario}, {self.cargo_usuario}, {self.email_perfil_usuario}, {self.senha_perfil_usuario}\n')
            print(f"Usuário salvo com sucesso em '{filename}'.")
        except Exception as e:
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

    def remover_acervo(self, acervo, codigo: int) -> None:
        # Remove um exemplar do acervo.
        try:
            if codigo in acervo:
                del acervo[codigo]
                print("Exemplar removido com sucesso do acervo.")
            else:
                print("Exemplar não encontrado no acervo.")
        except Exception as e:
            print(f"Erro ao remover exemplar do acervo: {e}")
