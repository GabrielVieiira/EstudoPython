class Banco:
    def __init__(self):
        pass
    @classmethod    
    def deposito(self, saldo, valor):
        novo_saldo = valor + saldo
        return novo_saldo
    @classmethod 
    def saque(self, saldo, valor):
        novo_saldo = saldo - valor
        return novo_saldo
    @classmethod
    def extrato(self,cliente):   
        for i in range(0,len(cliente.transacoes)):
            print(cliente.transacoes[i])
class Adm:
    usuario:str
    senha:str
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
    @classmethod
    def admLogin(self):
        while(True):    
                nome_usuario = input('Nome de usuário: ')
                if nome_usuario == adm.usuario:
                        print('Cliente encontrado')
                        break
                else:
                    print("Usuario não encontrado")
        while(True):
                senha = input('Senha: ')
                if senha == adm.senha:
                    print('Senha correta')
                    break
                else:
                    print("Senha não encontrada")
class Funcionario:
    usuario:str
    senha:str
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
    
    def criarFuncionario():
        while(True):    
            funcionario_usuario = input("Qual vai ser o usuario? ")
            funcionario_usuario_verificar = input("Digite novamente ")
            if funcionario_usuario == funcionario_usuario_verificar:
                while(True):    
                    funcionario_senha = input("Qual vai ser a senha? ")
                    funcionario_senha_verificar = input("Digite novamente ")
                    if funcionario_senha == funcionario_senha_verificar:
                        print('Usuario criado com sucesso!')
                        return  Funcionario(funcionario_usuario,funcionario_senha)
                    else:
                        print('Verifique a senha digitada')  
            else:
                print('Verifica o usuario digitado')
                pass
    @classmethod
    def funcionarioLogin(self):
        while(True):    
                nome_usuario = input('Nome de usuário: ')
                if nome_usuario == funcionario.usuario:
                        print('Cliente encontrado')
                        break
                else:
                    print("Usuario não encontrado")
        while(True):
                senha = input('Senha: ')
                if senha == funcionario.senha:
                    print('Senha correta')
                    break
                else:
                    print("Senha não encontrada")         
class Cliente:
    nome:str
    conta:int
    saldo:float
    tipo_de_conta:str
    usuario:str
    senha:str
    def __init__(self, nome, conta,saldo, tipo_de_conta,usuario,senha):
        self.nome = nome
        self.conta = conta
        self.saldo = saldo
        self.tipo_de_conta = ["fisica","juridica"]
        if tipo_de_conta in self.tipo_de_conta:
            self.tipo_de_conta = tipo_de_conta
        else:
            print("Tipo de conta inválido")
        self.usuario = usuario
        self.senha = senha
        self.transacoes = []
    def clienteLogin(lista_clientes):
        flag = True
        while(flag):    
            nome_usuario = input('Nome de usuário: ')
            i = 0
            while(i<len(lista_clientes)):
                if nome_usuario == lista_clientes[i].usuario:
                    print('Cliente encontrado')
                    cliente_selecionado = lista_clientes[i]
                    flag = False
                    break
                elif i == len(lista_clientes)-1:
                    print('Usuario não encontrado')
                    break
                else:
                    i += 1               
        while(True):
            senha = input('Senha: ')
            if senha == cliente_selecionado.senha:
                print('Senha correta')
                return cliente_selecionado
            else:
                print('Senha incorreta')                                     
adm = Adm('adm', 'adm')
Adm.admLogin()
resposta = input('Para cadastrar funcionario digite : 1 \n Para alterar funcionario : 2')
while(True):
    if resposta == '1':
        funcionario = Funcionario.criarFuncionario()
        break
    elif resposta == '2':
        break
    else:
        print('Digite uma opção válida! ')
print('Logue com o funcionario!')
Funcionario.funcionarioLogin()
resposta = input('Para cadastrar cliente digite : 1 \n Para alterar cliente : 2')
while(True):
    if resposta == '1':
        cliente1 = Cliente("José", 123, 1000, "fisica", "Jose", "123")
        cliente2 = Cliente("João", 123, 2000, "fisica", "Joao", "123")
        cliente3 = Cliente("Sebastião", 123, 3000, "fisica", "Sebastiao", "123")
        cliente4 = Cliente("Maria", 123, 4000, "fisica", "Maria", "123")
        lista_clientes = [cliente1,cliente2,cliente3,cliente4]
        break
    elif resposta == '2':
        break
    else:
        print('Digite uma opção válida! ')
print('logue com o cliente')
cliente_selecionado = Cliente.clienteLogin(lista_clientes)
print('Login realizado')
while(True):
    print(f"Olá ,{cliente_selecionado.nome}! Qual operação desejá realizar? ")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Extrato ")
    print("4 - Sair")
    operacao = input()
    if operacao == "1":
        valor = float(input("Qual o valor desejeja depositar? R$: "))
        cliente_selecionado.saldo = Banco.deposito(cliente_selecionado.saldo, valor)
        print(f"Depósito realizado com sucesso! Seu saldo atual é R$: {cliente_selecionado.saldo}")
        cliente_selecionado.transacoes.append(("DEPÓSITO",valor))
    elif operacao == "2":
        valor = float(input("Digite o valor que deseja sacar R$: "))
        if cliente_selecionado.saldo>=valor:
            cliente_selecionado.saldo = Banco.saque(cliente_selecionado.saldo, valor)
            print(f"Saque realizado com sucesso. Seu novo saldo é de R$:{cliente_selecionado.saldo}")
            cliente_selecionado.transacoes.append(("SAQUE",valor*-1))
        else:
            print("Você não possui saldo suficiente para realizar esta transação")        
    elif operacao == "3":
        print(f"Extrato de {cliente_selecionado.nome}")
        print(f"Você realizou {len(cliente_selecionado.transacoes)} transações")
        Banco.extrato(cliente_selecionado)
    elif operacao == "4":
        break
    else:
        print("Digite uma operação válida")







    
    
     
     

        











# class Banco:
#     def __init__(self):
#         pass
#     @classmethod    
#     def deposito(self, saldo, valor):
#         novo_saldo = valor + saldo
#         return novo_saldo
#     @classmethod 
#     def saque(self, saldo, valor):
#         novo_saldo = saldo - valor
#         return novo_saldo
#     @classmethod
#     def extrato(self,cliente):   
#         for i in range(0,len(cliente.transacoes)):
#             print(cliente.transacoes[i])

# cliente1 = Cliente("José", 123, 1000, "fisica", "Jose", "123")
# cliente2 = Cliente("João", 123, 2000, "fisica", "Joao", "123")
# cliente3 = Cliente("Sebastião", 123, 3000, "fisica", "Sebastiao", "123")
# cliente4 = Cliente("Maria", 123, 4000, "fisica", "Maria", "123")
# lista_clientes = [cliente1,cliente2,cliente3,cliente4]

# while(True):
#     while(True):    
#         nome_usuario = input('Nome de usuário: ')
#         i = 0
#         while(i<4):
#             if nome_usuario == lista_clientes[i].usuario:
#                 print('Cliente encontrado')
#                 cliente_selecionado = lista_clientes[i]
#                 break
#             else:
#                 print("Usuario não encontrado")
#             i += 1
#         while(True):
#             senha = input('Senha: ')
#             if senha == cliente_selecionado.senha:
#                 print('Senha correta')
#                 while(True):
#                     print(f"Olá ,{cliente_selecionado.nome}! Qual operação desejá realizar? ")
#                     print("1 - Depósito")
#                     print("2 - Saque")
#                     print("3 - Extrato ")
#                     print("4 - Sair")
#                     operacao = input()
#                     if operacao == "1":
#                         valor = float(input("Qual o valor desejeja depositar? R$: "))
#                         cliente_selecionado.saldo = Banco.deposito(cliente_selecionado.saldo, valor)
#                         print(f"Depósito realizado com sucesso! Seu saldo atual é R$: {cliente_selecionado.saldo}")
#                         cliente_selecionado.transacoes.append(("DEPÓSITO",valor))
#                     elif operacao == "2":
#                         valor = float(input("Digite o valor que deseja sacar R$: "))
#                         if cliente_selecionado.saldo>=valor:
#                             cliente_selecionado.saldo = Banco.saque(cliente_selecionado.saldo, valor)
#                             print(f"Saque realizado com sucesso. Seu novo saldo é de R$:{cliente_selecionado.saldo}")
#                             cliente_selecionado.transacoes.append(("SAQUE",valor))
#                         else:
#                             print("Você não possui saldo suficiente para realizar esta transação")        
#                     elif operacao == "3":
#                         print(f"Extrato de {cliente_selecionado.nome}")
#                         print(f"Você realizou {len(cliente_selecionado.transacoes)} transações")
#                         Banco.extrato(cliente_selecionado)
#                     elif operacao == "4":
#                         break
#                     else:
#                         print("Digite uma operação válida")
#             else:
#                 print('Senha incorreta')