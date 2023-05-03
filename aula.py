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
    
    def deposito(self, saldo):
        valor = float(input("Digite o valor que deseja depositar "))
        novo_saldo = valor + saldo
        print("Depósito realizado com sucesso! Seu saldo atual é R$ ", novo_saldo)
        self.transacoes.append(("DEPÓSITO",valor))
        return novo_saldo
    
    def saque(self, saldo):
        print(f"Você possui um saldo de {saldo}")
        valor = float(input("Digite o valor que deseja sacar "))
        if saldo>=valor:
            novo_saldo = saldo - valor
            print(f"Saque realizado com sucesso. Seu novo saldo é de R$:{novo_saldo}")
            self.transacoes.append(("DEPOSITO",valor))
        else:
            print("Você não possui saldo suficiente para realizar esta transação")
        return novo_saldo
    
    def extrato(self):
        print(f"Extrato de {cliente.nome}")
        print(f"Você realizou {len(cliente.transacoes)} transações")
        for i in range(0,len(cliente.transacoes)):
            print(cliente.transacoes[i])
    
saldo = 0
nome = input("Olá, Digite seu nome: ")
cliente = Cliente(nome, 123, saldo, "fisica", "joao", 123)
flag = True
while(flag):
    print(f"Olá ,{nome}! Qual operação desejá realizar? ")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Extrato ")
    print("4 - Sair")
    operacao = input()


    if operacao == "1":
        saldo = cliente.deposito(saldo)
    elif operacao == "2":
        saldo = cliente.saque(saldo)
    elif operacao == "3":
        cliente.extrato()
    elif operacao == "4":
        flag = False
    else:
        print("Digite uma operação válida")




    
    
