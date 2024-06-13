import datetime
from abc import ABC, abstractmethod
from typing import Optional

class Exemplar(ABC):
    # Inicializa um objeto Exemplar com os detalhes fornecidos.
    # ValueError: Se o código ou ano de publicação não forem números inteiros positivos.
    def __init__(self, codigo:int, autor:str, titulo:str, ano_publicacao:int, genero:str) -> None:
        if not isinstance(codigo, int) or codigo <= 0:
            raise ValueError("O código deve ser um número inteiro positivo.")
        if not isinstance(ano_publicacao, int) or ano_publicacao <= 0:
            raise ValueError("O ano de publicação deve ser um número inteiro positivo.")

        self._codigo:int = codigo
        self._autor:str = autor
        self._titulo:str = titulo
        self._ano_publicacao:int = ano_publicacao
        self._genero:str = genero
        self._emprestado:bool = False
        self._data_emprestimo:Optional[datetime.date] = None

    @abstractmethod
    def calcula_multa(self, data_devolucao:datetime.date) -> float:
        # Calcula a multa para a devolução atrasada do exemplar.
        # Returns: float: Valor da multa.
        pass

    def calcula_data_devolucao(self) -> datetime.date:
        """ Calcula a data de devolução com base na data de empréstimo.
        Returns: datetime.date: Data de devolução do exemplar.
        ValueError: Se o exemplar ainda não foi emprestado.
        """
        if self._data_emprestimo is None:
            raise ValueError("O exemplar ainda não foi emprestado, portanto não é possível calcular a data de devolução.")
        
        # Adicionando 7 dias à data de empréstimo
        data_devolucao = self._data_emprestimo + datetime.timedelta(days=7)
        return data_devolucao

    def emprestar(self) -> None:
        """ Marca o exemplar como emprestado e define a data de empréstimo como a data atual.
        ValueError: Se o exemplar já está emprestado. """
        if self._emprestado:
            raise ValueError("O exemplar já foi emprestado.")
        
        self._emprestado = True
        self._data_emprestimo = datetime.datetime.now().date()

    def devolver(self) -> None:
        # Marca o exemplar como devolvido e limpa a data de empréstimo.
        if not self._emprestado:
            raise ValueError("O exemplar ainda não foi emprestado.")
        
        self._emprestado = False
        self._data_emprestimo = None

    # Retorna o código do exemplar.
    def get_codigo(self) -> int:
        return self._codigo

    # Retorna o autor do exemplar.
    def get_autor(self) -> str:
        return self._autor

    # Retorna o título do exemplar.
    def get_titulo(self) -> str:
        return self._titulo

    # Retorna o ano de publicação do exemplar.
    def get_ano_publicacao(self) -> int:
        return self._ano_publicacao

    # Retorna o gênero do exemplar.
    def get_genero(self) -> str:
        return self._genero

    # Verifica se o exemplar está emprestado.
    def is_emprestado(self) -> bool:
        return self._emprestado

    # Retorna a data de empréstimo do exemplar.
    def get_data_emprestimo(self) -> Optional[datetime.date]:
        return self._data_emprestimo

    # Converte os detalhes do exemplar para uma string formatada.
    # Returns: str: String com os detalhes do exemplar.
    def to_string(self) -> str:
        return f"{self._codigo},{self._autor},{self._titulo},{self._ano_publicacao},{self._genero},{self._emprestado},{self._data_emprestimo}"

    @classmethod
    def from_string(cls, linha: str) -> 'Exemplar':
        # Converte uma string formatada em um objeto Exemplar.
        # Returns: Exemplar: Objeto Exemplar.
        valores = linha.strip().split(',')
        codigo, autor, titulo, ano_publicacao, genero, emprestado, data_emprestimo = valores
        exemplar = cls(int(codigo), autor, titulo, int(ano_publicacao), genero)
        exemplar._emprestado = bool(emprestado)
        exemplar._data_emprestimo = datetime.datetime.strptime(data_emprestimo, "%Y-%m-%d").date() if emprestado else None
        return exemplar
