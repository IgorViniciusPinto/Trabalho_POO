from abc import ABC, abstractmethod
from typing import Optional
import datetime

class Exemplar(ABC):
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
        pass

    @abstractmethod
    def calcula_data_devolucao(self) -> datetime.date:
        pass

    @abstractmethod
    def emprestar(self) -> None:
        pass

    @abstractmethod
    def devolver(self) -> None:
        pass

    def get_codigo(self) -> int:
        return self._codigo

    def get_autor(self) -> str:
        return self._autor

    def get_titulo(self) -> str:
        return self._titulo

    def get_ano_publicacao(self) -> int:
        return self._ano_publicacao

    def get_genero(self) -> str:
        return self._genero

    def is_emprestado(self) -> bool:
        return self._emprestado

    def get_data_emprestimo(self) -> Optional[datetime.date]:
        return self._data_emprestimo

    def to_string(self) -> str:
        return f"{self._codigo},{self._autor},{self._titulo},{self._ano_publicacao},{self._genero},{self._emprestado},{self._data_emprestimo}"

    @classmethod
    @abstractmethod
    def from_string(cls, linha: str) -> 'Exemplar':
        pass

class ExemplarConcreto(Exemplar):
    def calcula_multa(self, data_devolucao: datetime.date) -> float:
        if self._data_emprestimo is None:
            raise ValueError("O exemplar ainda não foi emprestado, não é possível calcular a multa.")
        
        # Calculando dias de atraso
        dias_atraso = (data_devolucao - self._data_emprestimo).days
        
        # Se não houver atraso, multa é zero
        if dias_atraso <= 0:
            return 0.0
        
        # Calculando multa baseada no número de dias de atraso (exemplo de R$ 2,00 por dia de atraso)
        multa = dias_atraso * 2.0
        return multa

    def calcula_data_devolucao(self) -> datetime.date:
        if self._data_emprestimo is None:
            raise ValueError("O exemplar ainda não foi emprestado, não é possível calcular a data de devolução.")
        
        data_devolucao = self._data_emprestimo + datetime.timedelta(days=7)
        return data_devolucao

    def emprestar(self) -> None:
        if self._emprestado:
            raise ValueError("O exemplar já foi emprestado.")
        
        self._emprestado = True
        self._data_emprestimo = datetime.datetime.now().date()

    def devolver(self) -> None:
        if not self._emprestado:
            raise ValueError("O exemplar ainda não foi emprestado.")
        
        self._emprestado = False
        self._data_emprestimo = None

    @classmethod
    def from_string(cls, linha: str) -> 'ExemplarConcreto':
        valores = linha.strip().split(',')
        codigo, autor, titulo, ano_publicacao, genero, emprestado, data_emprestimo = valores
        exemplar = cls(int(codigo), autor, titulo, int(ano_publicacao), genero)
        exemplar._emprestado = bool(emprestado)
        exemplar._data_emprestimo = datetime.datetime.strptime(data_emprestimo, "%Y-%m-%d").date() if emprestado else None
        return exemplar
