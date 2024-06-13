import csv
from bibliotecario import Bibliotecario
from typing import Dict, List, Union, Optional
from exemplar import Exemplar
from admin import Admin
from aluno import Aluno

class EmailJaCadastradoError(Exception):
# Exceção personalizada para indicar que um email já foi cadastrado.
    pass

class Sistema:
    # Classe responsável por gerenciar o sistema de biblioteca, incluindo acervos e usuários.
    def __init__(self) -> None:
    # Inicializa o sistema com dicionários vazios para acervo e usuários.
        self.biblioteca: Dict[int, List[Exemplar]] = {}  # Mapeia o código de acervo para uma lista de exemplares
        self.usuarios: Dict[str, Union[Aluno, Bibliotecario, Admin]] = {}  # Mapeia o email do usuário para uma instância de PerfilUsuario

    def inicia_sistema(self) -> None:
        # Método principal para iniciar o sistema, carregando acervos e usuários, e realizando login ou cadastro.
        print("Olá! Bem-vindo ao sistema de biblioteca.\n")

        print("Carregando livros:\n")
        self.carregar_acervos("acervos.txt")

        print("Carregando usuários:\n")
        self.carregar_usuarios("usuarios.txt")

        try:
            cargo = int(input("Digite o número correspondente ao seu cargo (0 para Aluno, 1 para Bibliotecário, 2 para Admin): "))
        except ValueError:
            print("Entrada inválida. Encerrando o sistema.")
            return
        
        cadastro = self.tela_cadastro(cargo)
        if cadastro:
            self.tela_login()

    def carregar_acervos(self, arquivo:str) -> None:
        # Carrega os acervos a partir de um arquivo CSV.
        try:
            with open(arquivo, "r") as arquivo_acervos:
                acervos_reader = csv.reader(arquivo_acervos)
                next(acervos_reader)  # Pular o cabeçalho
                for linha in acervos_reader:
                    codigo_acervo, autor, titulo, ano_publicacao, genero = linha
                    codigo_acervo = int(codigo_acervo)
                    ano_publicacao = int(ano_publicacao)
                    
                    exemplar = Exemplar(codigo_acervo, codigo_acervo, autor, titulo, ano_publicacao, genero)

                    if codigo_acervo not in self.biblioteca:
                        self.biblioteca[codigo_acervo] = []

                    self.biblioteca[codigo_acervo].append(exemplar)

        except FileNotFoundError:
            print("Falha ao abrir o arquivo de acervos.")
        except Exception as e:
            print(f"Erro ao carregar acervos: {e}")

    def carregar_usuarios(self, arquivo:str) -> None:
    # Carrega os usuários a partir de um arquivo CSV.
        try:
            with open(arquivo, "r") as arquivo_usuarios:
                usuarios_reader = csv.reader(arquivo_usuarios)
                next(usuarios_reader)  # Pular o cabeçalho
                for linha in usuarios_reader:
                    tipo_usuario, email, senha = linha
                    if email in self.usuarios:
                        continue
                    if tipo_usuario == "Aluno":
                        perfil_usuario = Aluno(email, senha)
                    elif tipo_usuario == "Bibliotecario":
                        perfil_usuario = Bibliotecario(email, senha)
                    elif tipo_usuario == "Admin":
                        perfil_usuario = Admin(email, senha)
                    else:
                        continue  # Ignora usuários com tipo inválido
                    self.usuarios[email] = perfil_usuario

        except FileNotFoundError:
            print("Falha ao abrir o arquivo com os usuários.")
        except Exception as e:
            print(f"Erro ao carregar usuários: {e}")

    def tela_cadastro(self, cargo:int) -> bool:
    # Tela de cadastro para novos usuários.
    # Returns: bool: True se o cadastro foi bem-sucedido ou se o usuário já tem cadastro, False caso contrário.
    
        entrada = input("Possui cadastro? Digite 0 para não e 1 para sim:\n")
        if entrada == "0":
            email = input("Cadastre seu email:\n")
            senha = int(input("Cadastre sua senha (somente números):\n"))
        
            if email in self.usuarios:
                print("Email já cadastrado.")
                return False

            if cargo == 0:
                novo_usuario = Aluno(email, senha)
            elif cargo == 1:
                novo_usuario = Bibliotecario(email, senha)
            elif cargo == 2:
                novo_usuario = Admin(email, senha)
            else:
                print("Cargo inválido.")
                return False

            self.usuarios[email] = novo_usuario
            print(f"Usuário {email} cadastrado com sucesso.")

            return True

        elif entrada == "1":
            return True

        return False

    def tela_login(self) -> None:
    # Tela de login para usuários existentes.
        email = input("Digite seu email:\n")
        tentativas = 0

        while tentativas < 3:
            senha = input("Digite sua senha:\n")

            if email in self.usuarios:
                perfil = self.usuarios[email]
                if perfil.get_senha_perfil_usuario() == senha:
                    if isinstance(perfil, Aluno):
                        self.tela_aluno(perfil)
                    elif isinstance(perfil, Bibliotecario):
                        self.tela_bibliotecario(perfil)
                    elif isinstance(perfil, Admin):
                        self.tela_admin(perfil)
                    return
                else:
                    print("Senha incorreta. Tente novamente.")
                    tentativas += 1
            else:
                resposta = input("Email não encontrado.\nDeseja fazer cadastro? Digite 0 para não e 1 para sim:\n")
                if resposta == "1":
                    if self.tela_cadastro():
                        self.tela_login()
                else:
                    print("Até mais!!")
                return  

        print("Você excedeu o número máximo de tentativas. O programa será encerrado.")

    def tela_aluno(self, aluno:Aluno) -> None:
    # Tela para alunos consultarem seus livros ou o acervo.
        while True:
            entrada_aluno = input("Olá aluno!\nDigite 1 para consultar seus livros:\nDigite 2 para consultar um livro específico:\nDigite 3 para sair:\n")

            if entrada_aluno == "1":
                print("Livros com você:")
                aluno.get_livros_com_aluno()
            elif entrada_aluno == "2":
                titulo_pesquisa = input("Digite o título do livro:\n")
                aluno.consultar_acervo(self.biblioteca, titulo_pesquisa)
            elif entrada_aluno == "3":
                print("Até logo!!")
                break

    def tela_bibliotecario(self, bibl:Bibliotecario) -> None:
    # Tela para bibliotecários consultarem o acervo.
        while True:
            print("Olá", bibl.get_email_perfil_usuario())
            print("Digite 1 para consultar todos os livros")
            print("Digite 2 para consultar um livro")
            print("Digite 0 para sair")
            op = input("> ")

            if op == "0":
                break
            elif op == "1":
                bibl.consultar_acervo(self.biblioteca)
            elif op == "2":
                titulo = input("Digite o título do livro que deseja consultar:\n")
                bibl.consultar_acervo(self.biblioteca, titulo)

    def tela_admin(self, admin:Admin) -> None:
    # Tela para administradores consultarem livros e gerenciar usuários.
        while True:
            print("Olá", admin.get_email_perfil_usuario())
            print("Digite 1 para consultar todos os livros")
            print("Digite 2 para consultar um livro")
            print("Digite 7 para consultar usuários")
            print("Digite 8 para adicionar usuário")
            print("Digite 9 para remover usuário")
            print("Digite 0 para sair")
            op = input("> ")

            if op == "0":
                break
            elif op == "1":
                admin.consultar_acervo(self.biblioteca)
            elif op == "2":
                titulo = input("Digite o título do livro que deseja consultar:\n")
                admin.consultar_acervo(self.biblioteca, titulo)
            elif op == "7":
                admin.consultar_usuarios(self.usuarios)
            elif op == "8":
                email = input("Digite o email do novo usuário:\n")
                senha = input("Digite a senha do novo usuário:\n")
                tipo_usuario = input("Digite o tipo do usuário (Aluno, Bibliotecario, Admin):\n")
                admin.adicionar_usuario(self.usuarios, email, senha, tipo_usuario)
            elif op == "9":
                email = input("Digite o email do usuário que deseja remover:\n")
                admin.remover_usuario(self.usuarios, email)

if __name__ == "__main__":
    sistema = Sistema()
    sistema.inicia_sistema()