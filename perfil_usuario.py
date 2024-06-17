from abc import ABC, abstractmethod
from typing import Optional, Any

class PerfilUsuario(ABC):
    """
    Interface base para perfis de usuário, contendo informações comuns e métodos abstratos.
    Esta interface define os métodos que todas as classes de perfil de usuário devem implementar.
    Contador estático usado para atribuir IDs únicos aos perfis de usuário.
    _ID_perfil_usuario (int): Identificador único do perfil de usuário.
    _email_perfil_usuario (str): Email do perfil de usuário.
    _senha_perfil_usuario (str): Senha do perfil de usuário.
    _cargo (Optional[str]): Cargo do usuário.
    """
    CONTADOR_ID_perfil_usuario: int = 0

    def __init__(self, email: str, senha: str) -> None:
        """Inicializa um novo perfil de usuário com email e senha, e atribui um ID único."""
        self._ID_perfil_usuario: int = PerfilUsuario.CONTADOR_ID_perfil_usuario
        PerfilUsuario.CONTADOR_ID_perfil_usuario += 1
        self._email_perfil_usuario: str = email
        self._senha_perfil_usuario: str = senha
        self._cargo: Optional[str] = None

    @abstractmethod
    def consultar_acervo(self, acervo: Any, titulo: Optional[str] = None) -> None:
        """Método abstrato para consultar o acervo."""
        pass

    @property
    def ID_perfil_usuario(self) -> int:
        """Retorna o ID único do perfil de usuário."""
        return self._ID_perfil_usuario

    @property
    def email_perfil_usuario(self) -> str:
        """Retorna o email do perfil de usuário."""
        return self._email_perfil_usuario

    @property
    def senha_perfil_usuario(self) -> str:
        """Retorna a senha do perfil de usuário."""
        return self._senha_perfil_usuario

    @property
    def cargo_usuario(self) -> Optional[str]:
        """Retorna o cargo do perfil de usuário."""
        return self._cargo

    @cargo_usuario.setter
    def cargo_usuario(self, cargo: Optional[str]) -> None:
        """Define o cargo do perfil de usuário."""
        self._cargo = cargo
