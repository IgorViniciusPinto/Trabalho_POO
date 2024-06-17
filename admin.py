from perfil_usuario import PerfilUsuario
from bibliotecario import Bibliotecario
from typing import Dict, List
from acervo import Acervo
from aluno import Aluno
import os

class Admin(PerfilUsuario):
    def __init__(self, email: str, senha: str) -> None:
        """Inicializa um administrador com email e senha."""
        super().__init__(email, senha)
        self._cargo: str = "Admin"

    # Verifica se o código do exemplar já existe no acervo para evitar duplicatas. Se não existir, o exemplar é adicionado.
    def adicionar_acervo(self, acervo: Dict[int, Acervo], exemplar:Acervo) -> bool:
        codigo: int = exemplar.get_codigo()
        if codigo in acervo:
            print(f"Erro: Já existe um exemplar com o código {codigo} no acervo.")
            return False
        acervo[codigo] = exemplar
        print(f"Exemplar '{exemplar.get_titulo()}' adicionado ao acervo com sucesso.")
        return True

    def remover_acervo(self, acervo: Dict[int, Acervo], codigo_exemplar: int) -> bool:
        """ Remove um exemplar do acervo.
        Returns: bool: True se o exemplar for removido, False caso contrário."""
        if codigo_exemplar not in acervo:
            print(f"Erro: Não foi encontrado um exemplar com o código {codigo_exemplar} no acervo.")
            return False
        exemplar = acervo[codigo_exemplar]
        if exemplar.is_emprestado():
            print(f"Erro: O exemplar '{exemplar.get_titulo()}' está emprestado e não pode ser removido.")
            return False
        del acervo[codigo_exemplar]
        print(f"Exemplar '{exemplar.get_titulo()}' removido do acervo com sucesso.")
        return True

    def listar_acervo(self, acervo: Dict[int, Acervo]) -> List[str]:
        # Lista todos os exemplares no acervo.
        resultados = []
        if not acervo:
            resultados.append("O acervo está vazio.")
        else:
            for exemplar in acervo.values():
                status = "Emprestado" if exemplar.is_emprestado() else "Disponível"
                resultados.append(f"Código: {exemplar.get_codigo()}, Título: {exemplar.get_titulo()}, Autor: {exemplar.get_autor()}, Ano: {exemplar.get_ano_publicacao()}, Gênero: {exemplar.get_genero()}, Status: {status}")
        return resultados

    def consultar_acervo(self, exemplares: List[Acervo]) -> None:
        # Verifica se exemplares é uma lista
        if isinstance(exemplares, list):
            # Itera sobre a lista de exemplares
            for exemplar in exemplares:
                print(f"Código: {exemplar.get_codigo()}, Título: {exemplar.get_titulo()}, Autor: {exemplar.get_autor()}, Ano: {exemplar.get_ano_publicacao()}, Gênero: {exemplar.get_genero()}")
        else:
            print("Erro: esperava-se uma lista de exemplares.")

    # Métodos de gestão de usuários
    def adicionar_usuario(self, usuarios: Dict[str, PerfilUsuario], email: str, senha: str, cargo: str) -> bool:
        # Adiciona um novo usuário.
        # Returns: bool: True se o usuário for adicionado, False caso contrário.
        if email in usuarios:
            print(f"Erro: Já existe um usuário com o email {email}.")
            return False
        
        if cargo == "Aluno":
            novo_usuario = Aluno(email, senha)
        elif cargo == "Bibliotecario":
            novo_usuario = Bibliotecario(email, senha)
        elif cargo == "Admin":
            novo_usuario = Admin(email, senha)
        else:
            print("Erro: Cargo de usuário inválido.")
            return False
        
        usuarios[email] = novo_usuario
        print(f"Usuário '{email}' adicionado com sucesso como '{cargo}'.")
        return True

    def remover_usuario(self, usuarios: Dict[str, PerfilUsuario], email: str) -> bool:
        # Remove um usuário.
        # Returns: bool: True se o usuário for removido, False caso contrário.
        if email not in usuarios:
            print(f"Erro: Usuário com email {email} não encontrado.")
            return False
        del usuarios[email]
        print(f"Usuário '{email}' removido com sucesso.")
        return True

    def listar_usuarios(self, usuarios: Dict[str, PerfilUsuario]) -> List[str]:
        # Lista todos os usuários.
        resultados = []
        if not usuarios:
            resultados.append("Não há usuários cadastrados.")
        else:
            for email, perfil in usuarios.items():
                resultados.append(f"ID: {perfil.get_ID_perfil_usuario()}, Email: {email}, Cargo: {perfil.get_cargo_usuario()}")
        return resultados

    def consultar_usuario(self, usuarios: Dict[str, PerfilUsuario], email: str) -> None:
        # Consulta um usuário pelo email.
        if email in usuarios:
            perfil = usuarios[email]
            print(f"ID: {perfil.get_ID_perfil_usuario()}, Email: {email}, Cargo: {perfil.get_cargo_usuario()}")
        else:
            print("Usuário não encontrado.")

    # Escreve cada exemplar do acervo no arquivo especificado, convertendo o exemplar para uma string usando o 
    # método to_string de Acervo
    def salvar_acervo(self, acervo: Dict[int, Acervo], filename: str = 'acervo.txt') -> None:
        try:
            with open(filename, 'w') as file:
                for exemplar in acervo.values():
                    file.write(exemplar.to_string() + '\n')
            print(f"Acervo salvo com sucesso em '{filename}'.")
        except Exception as e:
            print(f"Erro ao salvar o acervo: {e}")
            
    # Método para carregar o acervo
    def carregar_acervo(self, filename: str = 'acervo.txt') -> Dict[int, Acervo]:
        acervo: Dict[int, Acervo] = {}
        try:
            if os.path.exists(filename):
                with open(filename, 'r') as file:
                    for linha in file:
                        exemplar = Acervo.from_string(linha.strip())  # Assume que from_string é um método estático de Acervo
                        if exemplar:
                            acervo[exemplar.get_codigo()] = exemplar
                print(f"Acervo carregado com sucesso de '{filename}'.")
            else:
                print(f"O arquivo '{filename}' não existe.")
        except Exception as e:
            print(f"Erro ao carregar o acervo: {e}")
        return acervo

    # Método para salvar usuários no arquivo
    def salvar_usuario(self, filename:str='usuarios.txt') -> None:
        try:
            with open(filename, 'w') as file:
                for perfil in self.usuarios.values():
                    file.write(f'{perfil.get_ID_perfil_usuario()}, {perfil.get_cargo_usuario()}, {perfil.get_email_perfil_usuario()}, {perfil.get_senha_perfil_usuario()}\n')
            print(f"Usuários salvos com sucesso em '{filename}'.")
        except Exception as e:
            print(f"Erro ao salvar os usuários: {e}")

    # Método para carregar usuários de um arquivo
    # Returns: Dict[str, PerfilUsuario]: Dicionário representando os usuários carregados.
    def carregar_usuarios(self, filename: str = 'usuarios.txt') -> Dict[str, PerfilUsuario]:
        usuarios: Dict[str, PerfilUsuario] = {}
        try:
            if os.path.exists(filename):
                with open(filename, 'r') as file:
                    for linha in file:
                        id, cargo, email, senha = linha.strip().split(',')
                        if cargo == "Aluno":
                            novo_usuario = Aluno(email, senha)
                        elif cargo == "Bibliotecario":
                            novo_usuario = Bibliotecario(email, senha)
                        elif cargo == "Admin":
                            novo_usuario = Admin(email, senha)
                        else:
                            print(f"Erro: Tipo de cargo '{cargo}' desconhecido para o usuário '{email}'.")
                            continue
                        usuarios[email] = novo_usuario
                print(f"Usuários carregados com sucesso de '{filename}'.")
            else:
                print(f"O arquivo '{filename}' não existe.")
        except Exception as e:
            print(f"Erro ao carregar os usuários: {e}")
        return usuarios
