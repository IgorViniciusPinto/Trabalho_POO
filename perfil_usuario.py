from abc import ABC, abstractmethod
from typing import Optional, Any

class PerfilUsuario(ABC):
    """
    Classe base para perfis de usuário, contendo informações comuns e métodos abstratos.
    Contador estático usado para atribuir IDs únicos aos perfis de usuário.
    _ID_perfil_usuario (int): Identificador único do perfil de usuário.
    _email_perfil_usuario (str): Email do perfil de usuário.
    _senha_perfil_usuario (str): Senha do perfil de usuário.
    _papel (Optional[str]): Papel do usuário.
    """
    CONTADOR_ID_perfil_usuario:int = 0

    def __init__(self, email:str, senha:int) -> None:
        # Inicializa um novo perfil de usuário com email e senha, e atribui um ID único.
        self._ID_perfil_usuario: int = PerfilUsuario.CONTADOR_ID_perfil_usuario
        PerfilUsuario.CONTADOR_ID_perfil_usuario += 1
        self._email_perfil_usuario: str = email
        self._senha_perfil_usuario: str = senha
        self._papel: Optional[str] = None

    @abstractmethod
    def consultar_acervo(self, acervo: Any, titulo: Optional[str] = None) -> None:
        # Método abstrato para consultar o acervo.
        pass

    # Retorna o ID único do perfil de usuário.
    def get_ID_perfil_usuario(self) -> int:
        return self._ID_perfil_usuario

    # Retorna o email do perfil de usuário.
    def get_email_perfil_usuario(self) -> str:
        return self._email_perfil_usuario

    # Retorna a senha do perfil de usuário.
    def get_senha_perfil_usuario(self) -> int:
        return self._senha_perfil_usuario

    # Retorna o papel do perfil de usuário.
    def get_papel_usuario(self) -> Optional[str]:
        return self._papel
