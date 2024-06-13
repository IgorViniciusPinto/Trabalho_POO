from perfil_usuario import PerfilUsuario
from bibliotecario import Bibliotecario
from acervo import Acervo
from aluno import Aluno
import os

class Admin(PerfilUsuario):
    def __init__(self, email:str, senha:str) -> None:
        """Inicializa um administrador com email e senha."""
        super().__init__(email, senha)
        self._papel:str = "Admin"

    # Métodos de gestão do acervo
    # Returns: bool: True se o exemplar for adicionado, False se já existir.
    def adicionar_acervo(self, acervo, exemplar:Acervo) -> bool:
        codigo:int = exemplar.get_codigo()
        if codigo in acervo:
            print(f"Erro: Já existe um exemplar com o código {codigo} no acervo.")
            return False
        acervo[codigo] = exemplar
        print(f"Exemplar '{exemplar.get_titulo()}' adicionado ao acervo com sucesso.")
        return True

    def remover_acervo(self, acervo, codigo_exemplar:int) -> bool:
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

    def listar_acervo(self, acervo) -> None:
        # Lista todos os exemplares no acervo.
        if not acervo:
            print("O acervo está vazio.")
        else:
            for exemplar in acervo.values():
                status:str = "Emprestado" if exemplar.is_emprestado() else "Disponível"
                print(f"Código: {exemplar.get_codigo()}, Título: {exemplar.get_titulo()}, Autor: {exemplar.get_autor()}, Ano: {exemplar.get_ano_publicacao()}, Gênero: {exemplar.get_genero()}, Status: {status}")

    def consultar_acervo(self, acervo, titulo:str=None) -> None:
        # Consulta exemplares no acervo por título ou lista todos se nenhum título for fornecido.
        found:bool = False
        if titulo:
            for exemplar in acervo.values():
                if titulo.lower() in exemplar.get_titulo().lower():
                    found = True
                    print(f"Código: {exemplar.get_codigo()}, Título: {exemplar.get_titulo()}, Autor: {exemplar.get_autor()}, Ano: {exemplar.get_ano_publicacao()}, Gênero: {exemplar.get_genero()}")
            if not found:
                print("Livro não encontrado no acervo.")
        else:
            for exemplar in acervo.values():
                print(f"Código: {exemplar.get_codigo()}, Título: {exemplar.get_titulo()}, Autor: {exemplar.get_autor()}, Ano: {exemplar.get_ano_publicacao()}, Gênero: {exemplar.get_genero()}")

    # Métodos de gestão de usuários
    def adicionar_usuario(self, usuarios, email:str, senha:int, tipo_usuario:str) -> bool:
        # Adiciona um novo usuário.
        # Returns: bool: True se o usuário for adicionado, False caso contrário.
        if email in usuarios:
            print(f"Erro: Já existe um usuário com o email {email}.")
            return False
        
        if tipo_usuario == "Aluno":
            novo_usuario = Aluno(email, senha)
        elif tipo_usuario == "Bibliotecario":
            novo_usuario = Bibliotecario(email, senha)
        elif tipo_usuario == "Admin":
            novo_usuario = Admin(email, senha)
        else:
            print("Erro: Tipo de usuário inválido.")
            return False
        
        usuarios[email] = novo_usuario
        print(f"Usuário '{email}' adicionado com sucesso como '{tipo_usuario}'.")
        return True

    def remover_usuario(self, usuarios, email:str) -> bool:
        # Remove um usuário.
        # Returns: bool: True se o usuário for removido, False caso contrário.
        if email not in usuarios:
            print(f"Erro: Usuário com email {email} não encontrado.")
            return False
        del usuarios[email]
        print(f"Usuário '{email}' removido com sucesso.")
        return True

    def listar_usuarios(self, usuarios) -> None:
        # Lista todos os usuários.
        if not usuarios:
            print("Não há usuários cadastrados.")
        else:
            for email, perfil in usuarios.items():
                print(f"ID: {perfil.get_ID_perfil_usuario()}, Email: {email}, Papel: {perfil.get_papel_usuario()}")

    def consultar_usuario(self, usuarios, email:str) -> None:
        # Consulta um usuário pelo email.
        if email in usuarios:
            perfil = usuarios[email]
            print(f"ID: {perfil.get_ID_perfil_usuario()}, Email: {email}, Papel: {perfil.get_papel_usuario()}")
        else:
            print("Usuário não encontrado.")

    def salvar_usuario(self) -> None:
        # Salva o usuário atual no arquivo 'usuarios.txt'.
        with open('usuarios.txt', 'a') as file:
            file.write(f'{self.get_ID_perfil_usuario()}, {self.get_email_perfil_usuario()}, {self.get_senha_perfil_usuario()}, {self.get_papel_usuario()}\n')

    # Método para salvar o acervo em um arquivo
    def salvar_acervo(self, acervo, filename:str='acervo.txt') -> None:
        try:
            with open(filename, 'w') as file:
                for exemplar in acervo.values():
                    file.write(exemplar.to_string() + '\n')
            print(f"Acervo salvo com sucesso em '{filename}'.")
        except Exception as e:
            print(f"Erro ao salvar o acervo: {e}")

    # Método para carregar o acervo
    def carregar_acervo(self, filename:str='acervo.txt'):
        #Returns: Dict[int, Acervo]: Dicionário representando o acervo carregado.
        acervo = {}
        try:
            if os.path.exists(filename):
                with open(filename, 'r') as file:
                    for linha in file:
                        exemplar = Acervo.from_string(linha.strip())
                        acervo[exemplar.get_codigo()] = exemplar
                print(f"Acervo carregado com sucesso de '{filename}'.")
            else:
                print(f"O arquivo '{filename}' não existe.")
        except Exception as e:
            print(f"Erro ao carregar o acervo: {e}")
        return acervo

    # Método para salvar usuários no arquivo
    def salvar_usuarios(self, usuarios, filename:str='usuarios.txt') -> None:
        try:
            with open(filename, 'w') as file:
                for perfil in usuarios.values():
                    file.write(f'{perfil.get_ID_perfil_usuario()}, {perfil.get_email_perfil_usuario()}, {perfil.get_senha_perfil_usuario()}, {perfil.get_papel_usuario()}\n')
            print(f"Usuários salvos com sucesso em '{filename}'.")
        except Exception as e:
            print(f"Erro ao salvar os usuários: {e}")

    # Método para carregar usuários de um arquivo
    # Returns: Dict[str, PerfilUsuario]: Dicionário representando os usuários carregados.
    def carregar_usuarios(self, filename:str='usuarios.txt'):
        usuarios = {}
        try:
            if os.path.exists(filename):
                with open(filename, 'r') as file:
                    for linha in file:
                        id_perfil, email, senha, papel = linha.strip().split(', ')
                        if papel == "Aluno":
                            novo_usuario = Aluno(email, senha)
                        elif papel == "Bibliotecario":
                            novo_usuario = Bibliotecario(email, senha)
                        elif papel == "Admin":
                            novo_usuario = Admin(email, senha)
                        else:
                            print(f"Erro: Tipo de papel '{papel}' desconhecido para o usuário '{email}'.")
                            continue
                        usuarios[email] = novo_usuario
                print(f"Usuários carregados com sucesso de '{filename}'.")
            else:
                print(f"O arquivo '{filename}' não existe.")
        except Exception as e:
            print(f"Erro ao carregar os usuários: {e}")
        return usuarios
