import csv

class Acervo:
    def __init__(self, codigo:int, autor:str, titulo:str, ano_publicacao:int, genero:str) -> None:
        """Inicializa um exemplar do acervo com código, autor, título, ano de publicação e gênero."""
        self._codigo:int = codigo
        self._autor:str = autor
        self._titulo:str = titulo
        self._ano_publicacao:int = ano_publicacao
        self._genero:str = genero

    def get_codigo(self) -> None:
        """Retorna o código do exemplar."""
        return self._codigo

    def get_autor(self) -> str:
        """Retorna o autor do exemplar."""
        return self._autor

    def get_titulo(self) -> str:
        """Retorna o título do exemplar."""
        return self._titulo

    def get_ano_publicacao(self) -> int:
        """Retorna o ano de publicação do exemplar."""
        return self._ano_publicacao

    def get_genero(self) -> str:
        """Retorna o gênero do exemplar."""
        return self._genero

class GestorAcervo:
    def __init__(self) -> None:
        """Inicializa o gestor de acervo com um dicionário vazio para armazenar os exemplares."""
        self.acervo = {}

    def carregar_acervos(self, arquivo:str ="acervos.txt") -> None:
        """Carrega os exemplares do acervo a partir do arquivo acervos.txt."""
        try:
            with open(arquivo, "r") as arquivo_acervos:
                acervos_reader = csv.reader(arquivo_acervos)
                next(acervos_reader)  # Pular o cabeçalho
                for linha in acervos_reader:
                    if len(linha) != 5:
                        print("Erro: Linha incompleta no arquivo. Ignorando.")
                        continue

                    codigo, autor, titulo, ano_publicacao, genero = linha

                    try:
                        codigo = int(codigo)
                        ano_publicacao = int(ano_publicacao)
                    except ValueError as e:
                        print(f"Erro ao converter valores para inteiros: {e}. Linha: {linha}")
                        continue

                    exemplar = Acervo(codigo, autor, titulo, ano_publicacao, genero)

                    if codigo not in self.acervo:
                        self.acervo[codigo] = []

                    self.acervo[codigo].append(exemplar)

        except FileNotFoundError:
            print("Erro: Arquivo de acervos não encontrado.")
        except Exception as e:
            print(f"Erro ao carregar acervos: {e}")
