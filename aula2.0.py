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
    def extrato(self):   
        for i in range(0,len(cliente1.transacoes)):
            print(cliente1.transacoes[i])

class Cliente:
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

cliente1 = Cliente("José", 123, 1000, "fisica", "Jose", "123")
# cliente2 = Cliente("João", 123, 2000, "fisica", "Joao", 123)
# cliente3 = Cliente("Sebastião", 123, 3000, "fisica", "Sebastiao", 123)
# cliente4 = Cliente("Maria", 123, 4000, "fisica", "Maria", 123)
nome_usuario = input('Nome de usuário: ')
while nome_usuario != cliente1.usuario:
    print("Usuário incorreto")
    nome_usuario = input('Nome de usuário: ')

senha = input('Senha: ')
while senha != cliente1.senha:
    print("Senha incorreta")
    senha = input('Senha: ')

flag = True
while(flag):
    print(f"Olá ,{cliente1.nome}! Qual operação desejá realizar? ")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Extrato ")
    print("4 - Sair")
    operacao = input()

    if operacao == "1":
        valor = float(input("Qual o valor desejeja depositar? R$: "))
        cliente1.saldo = Banco.deposito(cliente1.saldo, valor)
        print(f"Depósito realizado com sucesso! Seu saldo atual é R$: {cliente1.saldo}")
        cliente1.transacoes.append(("DEPÓSITO",valor))
    elif operacao == "2":
        valor = float(input("Digite o valor que deseja sacar R$: "))
        if cliente1.saldo>=valor:
            cliente1.saldo = Banco.saque(cliente1.saldo, valor)
            print(f"Saque realizado com sucesso. Seu novo saldo é de R$:{cliente1.saldo}")
            cliente1.transacoes.append(("SAQUE",valor))
        else:
            print("Você não possui saldo suficiente para realizar esta transação")        
    elif operacao == "3":
        print(f"Extrato de {cliente1.nome}")
        print(f"Você realizou {len(cliente1.transacoes)} transações")
        Banco.extrato()
    elif operacao == "4":
        flag = False
    else:
        print("Digite uma operação válida")

    
    
