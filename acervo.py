from typing import List, Dict, Optional
import csv

class Acervo:
    def __init__(self, codigo: int, autor: str, titulo: str, ano_publicacao: int, genero: str) -> None:
        """Inicializa um exemplar do acervo com código, autor, título, ano de publicação e gênero."""
        self._codigo: int = codigo
        self._autor: str = autor
        self._titulo: str = titulo
        self._ano_publicacao: int = ano_publicacao
        self._genero: str = genero
        self._emprestado: bool = False

    @property
    def codigo(self) -> int:
        """Retorna o código do exemplar."""
        return self._codigo

    @property
    def autor(self) -> str:
        """Retorna o autor do exemplar."""
        return self._autor

    @property
    def titulo(self) -> str:
        """Retorna o título do exemplar."""
        return self._titulo

    @property
    def ano_publicacao(self) -> int:
        """Retorna o ano de publicação do exemplar."""
        return self._ano_publicacao

    @property
    def genero(self) -> str:
        """Retorna o gênero do exemplar."""
        return self._genero

    @property
    def emprestado(self) -> bool:
        """Retorna True se o exemplar está emprestado, False caso contrário."""
        return self._emprestado

    @emprestado.setter
    def emprestado(self, emprestado: bool) -> None:
        """Define o status de empréstimo do exemplar."""
        self._emprestado = emprestado

    def to_string(self) -> str:
        """Retorna uma string representando o exemplar para salvar em um arquivo."""
        return f'{self._codigo}, {self._autor}, {self._titulo}, {self._ano_publicacao}, {self._genero}, {"Emprestado" if self._emprestado else "Disponível"}'

    @classmethod
    def from_string(cls, exemplar_str: str) -> "Acervo":
        """Cria um exemplar a partir de uma string."""
        codigo, autor, titulo, ano_publicacao, genero, status = exemplar_str.strip().split(',')
        exemplar = cls(int(codigo), autor.strip(), titulo.strip(), int(ano_publicacao), genero.strip())
        exemplar.emprestado = (status.strip() == "Emprestado")
        return exemplar

class GestorAcervo:
    def __init__(self) -> None:
        """Inicializa o gestor de acervo com um dicionário vazio para armazenar os exemplares."""
        self.acervo: Dict[int, List[Acervo]] = {}

    def adicionar_exemplar(self, exemplar: Acervo) -> None:
        """Adiciona um exemplar ao acervo."""
        if exemplar.codigo not in self.acervo:
            self.acervo[exemplar.codigo] = []
        self.acervo[exemplar.codigo].append(exemplar)

    def consultar_exemplar_por_codigo(self, codigo: int) -> Optional[Acervo]:
        """Consulta um exemplar no acervo pelo código."""
        if codigo in self.acervo and self.acervo[codigo]:
            return self.acervo[codigo][0]  # Retorna o primeiro exemplar encontrado com o código
        else:
            return None

    def carregar_acervos(self, arquivo: str = "acervos.txt") -> None:
        """Carrega os exemplares do acervo a partir do arquivo acervos.txt."""
        try:
            with open(arquivo, "r", newline='', encoding='utf-8') as arquivo_acervos:
                acervos_reader = csv.reader(arquivo_acervos)
                next(acervos_reader)  # Pular o cabeçalho
                for linha in acervos_reader:
                    if len(linha) != 6:  # Verifique se há 6 campos na linha
                        print(f"Erro: Formato inválido de linha no arquivo. Linha: {linha}")
                        continue

                    codigo, autor, titulo, ano_publicacao, genero, status = linha
                    try:
                        codigo = int(codigo)
                        ano_publicacao = int(ano_publicacao)
                    except ValueError as e:
                        print(f"Erro ao converter valores para inteiros: {e}. Linha: {linha}")
                        continue

                    exemplar = Acervo(codigo, autor.strip(), titulo.strip(), ano_publicacao, genero.strip())
                    exemplar.emprestado = (status.strip() == "Emprestado")
                    self.adicionar_exemplar(exemplar)

        except FileNotFoundError:
            print("Erro: Arquivo de acervos não encontrado.")
        except Exception as e:
            print(f"Erro ao carregar acervos: {e}")

    def salvar_acervos(self, arquivo: str = "acervos.txt") -> None:
        """Salva os exemplares do acervo no arquivo acervos.txt."""
        try:
            with open(arquivo, "w", newline='', encoding='utf-8') as arquivo_acervos:
                writer = csv.writer(arquivo_acervos)
                writer.writerow(["codigo", "autor", "titulo", "ano_publicacao", "genero", "status"])
                for lista_exemplares in self.acervo.values():
                    for exemplar in lista_exemplares:
                        writer.writerow([
                            exemplar.codigo,
                            exemplar.autor,
                            exemplar.titulo,
                            exemplar.ano_publicacao,
                            exemplar.genero,
                            "Emprestado" if exemplar.emprestado else "Disponível"
                        ])
        except Exception as e:
            print(f"Erro ao salvar acervos: {e}")
