import random

class Banco:
    nome = ''
    db_funcionario = []
    db_clientes = []
    def __init__(self,nome):
        self.nome = nome
        self.db_funcionario = []
        self.db_clientes = []
    
    def criarFuncionario(self, usuario, senha,nome):
        funcionario = Adm(usuario,senha,nome)
        self.db_funcionario.append(funcionario)
        return funcionario
    
    def criarCliente(self,nome, saldo, usuario, senha,cpf):
        conta = random.randint(100,999)
        cliet = Cliente(nome,conta,saldo,usuario,senha,cpf)
        self.db_clientes.append(cliet)
        return cliet

    def localizaCliente(self,cpf):
        i = 0 
        while(i<len(self.db_clientes)):
            if self.db_clientes[i].getCpf() == cpf:
                print('cpf encontrado')
                return self.db_clientes[i]
            else:
                print('cpf não encontrado')
                i+=1


    def getLendb(self):
        return (self.db_funcionario)
    
    def getName(self):
        return self.nome

class Adm:
    usuario:str
    senha:str
    nome:str
    def __init__(self, usuario, senha,nome):
        self.usuario = usuario
        self.senha = senha
        self.nome = nome
    
    def getUser(self):
        return self.usuario
    def getSenha(self):
        return self.senha
    def getName(self):
        return self.nome
    
    @classmethod
    def funcionarioLogin(cls,usuario,senha):
        i = 0
        while(i<len(banco_1.db_funcionario)):
            if banco_1.db_funcionario[i].getUser() == usuario:
                if banco_1.db_funcionario[i].getSenha() == senha:
                    return banco_1.db_funcionario[i]
                else:
                    print('Senha incorreta')
            else:
                print("Usuario não encontrado")
            i += 1   

class Cliente:
    nome = ''
    cpf:int
    conta:int
    saldo:float
    usuario:str
    senha:str
    transacoes = []
    def __init__(self, nome,conta,saldo,usuario,senha,cpf):
        self.nome = nome
        self.cpf = cpf
        self.conta = conta
        self.saldo = saldo
        self.usuario = usuario
        self.senha = senha
        self.transacoes = []
    def getConta(self):
        return self.conta
    def getCpf(self):
        return self.cpf

banco_1 = Banco('SENAC')
Flag = True  
print(f'Bem vindo ao sistema bancario {banco_1.getName()}')
print('Vamos começar cadastrando os funcionarios!!')
while(Flag):
    nome = input("Digite o nome do funcionario: ")
    usuario = input("Digite o usuario: ")
    usuario_verificacao = input("Digite novamente: ")
    
    if usuario == usuario_verificacao:
        while(True):
            senha = input("Digite uma senha: ")
            senha_verificacao = input("Digite a senha novamente? ")
            if senha == senha_verificacao:
                banco_1.criarFuncionario(usuario,senha,nome)
                print("Cliente cadastrado com sucesso")
                resp = input("Deseja cadastrar mais algum funcionario? s/n    ")
                if resp == 's':
                    break
                else:
                    Flag = False
                    break
            else:
                print("Verifique os campos digitados")                
    else:
        print("Verifique os campos digitados")
print('---------------------------------------------------------------------------------')
print('Agora vamos logar com algum funcionario criado anteriormente')

while(True):
    usuario = input('Digite um usuario: ')
    senha = input('Digite sua senha: ')
    funcionario = Adm.funcionarioLogin(usuario,senha)
    if funcionario == None:
        pass
    else:
        break
while(True):    
    print(f'Olá, {funcionario.getName()}!')
    resp = input(f'Digite a função que deseja realizar:\n 1 - Adicionar Cliente \n 2 - Localizar Cliente')
    if resp == '1':
        Flag = True
        nome = input("Digite o nome do cliente: ")
        saldo = 0
        cpf = int(input("Digite o CPF do cliente: "))
        while(Flag):
            usuario = input("Digite o usuario: ")
            usuario_verificacao = input("Digite novamente: ")
            if usuario == usuario_verificacao:
                while(True):
                    senha = input("Digite uma senha: ")
                    senha_verificacao = input("Digite a senha novamente? ")
                    if senha == senha_verificacao:
                        cliente_selecionado = banco_1.criarCliente(nome, saldo, usuario, senha,cpf)
                        print("Usuario cadastrado com sucesso")
                        resp = input("Deseja cadastrar mais algum Cliente? s/n    ")
                        if resp == 's':
                            break
                        else:
                            Flag = False
                            break
                    else:
                        print("Verifique os campos digitados")                
            else:
                print("Verifique os campos digitados")
    elif resp == '2':
        cpf = int(input('Digite o CPF do cliente: '))
        cliente_selecionado = banco_1.localizaCliente(cpf)
        print(cliente_selecionado.getConta())
        

