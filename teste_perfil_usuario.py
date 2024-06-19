import unittest
from perfil_usuario import PerfilUsuario

class PerfilUsuarioConcreto(PerfilUsuario):
    def consultar_acervo(self, acervo, titulo=None):
        # Implementação concreta apenas para fins de teste
        print(f"Consultando acervo com título: {titulo}")

class TestPerfilUsuario(unittest.TestCase):

    def setUp(self):
        # Configuração inicial para cada teste
        # Não resetar o contador aqui para testar a sequência de IDs
        self.usuario1 = PerfilUsuarioConcreto("email1@exemplo.com", "senha123")
        self.usuario2 = PerfilUsuarioConcreto("email2@exemplo.com", "senha456")
        self.usuario3 = PerfilUsuarioConcreto("email3@exemplo.com", "senha789")
        print(f"Setup: ID do usuário 1: {self.usuario1.ID_perfil_usuario}, ID do usuário 2: {self.usuario2.ID_perfil_usuario}, ID do usuário 3: {self.usuario3.ID_perfil_usuario}")

    def tearDown(self):
        # Resetar o contador após cada teste para garantir que outros testes não sejam afetados
        PerfilUsuario.CONTADOR_ID_perfil_usuario = 0

    def test_inicializacao(self):
        # Testa a inicialização do objeto PerfilUsuario
        print("Teste de Inicialização:")
        print(f"ID do usuário: {self.usuario1.ID_perfil_usuario}")
        print(f"Email do usuário: {self.usuario1.email_perfil_usuario}")
        print(f"Senha do usuário: {self.usuario1.senha_perfil_usuario}")
        print(f"Cargo do usuário: {self.usuario1.cargo_usuario}")
        
        self.assertEqual(self.usuario1.email_perfil_usuario, "email1@exemplo.com")
        self.assertEqual(self.usuario1.senha_perfil_usuario, "senha123")
        self.assertIsNone(self.usuario1.cargo_usuario)
        print("Inicialização verificada com sucesso.\n")

    def test_ids_unicos(self):
        # Testa se IDs são atribuídos de forma única
        print("Teste de IDs Únicos:")
        print(f"ID do usuário 1: {self.usuario1.ID_perfil_usuario}")
        print(f"ID do usuário 2: {self.usuario2.ID_perfil_usuario}")
        print(f"ID do usuário 3: {self.usuario3.ID_perfil_usuario}")
        
        self.assertEqual(self.usuario1.ID_perfil_usuario, 0)
        self.assertEqual(self.usuario2.ID_perfil_usuario, 1)
        self.assertEqual(self.usuario3.ID_perfil_usuario, 2)
        print("IDs Únicos verificados com sucesso.\n")
    
    def test_setter_cargo(self):
        # Testa o setter de cargo
        print("Teste de Setter de Cargo:")
        print(f"Cargo inicial do usuário 1: {self.usuario1.cargo_usuario}")
        
        self.usuario1.cargo_usuario = "Administrador"
        print(f"Novo cargo do usuário 1: {self.usuario1.cargo_usuario}")
        self.assertEqual(self.usuario1.cargo_usuario, "Administrador")
        
        self.usuario2.cargo_usuario = "Usuário"
        print(f"Novo cargo do usuário 2: {self.usuario2.cargo_usuario}")
        self.assertEqual(self.usuario2.cargo_usuario, "Usuário")
        print("Setter de Cargo verificado com sucesso.\n")
    
    def test_consultar_acervo(self):
        # Testa o método consultar_acervo
        print("Teste de Consultar Acervo:")
        try:
            self.usuario1.consultar_acervo(None)
            print("Método consultar_acervo chamado com sucesso.")
        except Exception as e:
            self.fail(f"consultar_acervo levantou uma exceção: {e}")
        print("Método consultar_acervo verificado com sucesso.\n")

if __name__ == '__main__':
    unittest.main()
