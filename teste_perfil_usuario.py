import unittest
from perfil_usuario import PerfilUsuario

class PerfilUsuarioConcreto(PerfilUsuario):
    def consultar_acervo(self, acervo, titulo=None):
        # Implementação concreta apenas para fins de teste
        print("Consulta de acervo realizada")

class TestPerfilUsuario(unittest.TestCase):
    
    def setUp(self):
        # Configuração inicial para cada teste, se necessário
        self.usuario = PerfilUsuarioConcreto("email@exemplo.com", "senha123")
    
    def test_inicializacao(self):
        # Testa a inicialização do objeto PerfilUsuario
        print("Teste de inicialização:")
        print(f"ID: {self.usuario.get_ID_perfil_usuario()}")
        print(f"Email: {self.usuario.get_email_perfil_usuario()}")
        print(f"Senha: {self.usuario.get_senha_perfil_usuario()}")
        print(f"Cargo: {self.usuario.get_cargo_usuario()}")
        print()
        
        self.assertEqual(self.usuario.get_email_perfil_usuario(), "email@exemplo.com")
        self.assertEqual(self.usuario.get_senha_perfil_usuario(), "senha123")
        self.assertIsNone(self.usuario.get_cargo_usuario())

    def test_consultar_acervo(self):
        # Testa o método consultar_acervo
        print("Teste do método consultar_acervo:")
        self.usuario.consultar_acervo(None)
        print()
        
        # Sem asserção específica, apenas verificando se o método pode ser chamado sem erros

if __name__ == '__main__':
    unittest.main()
