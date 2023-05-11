class Estacionamento:
    nome = None
    setor1 = None
    setor2 = None
    setor3 = None
    setor4 = None
    def __init__(self, nome):
        self.nome = nome
        self.setor1 = ['','','','']
        self.setor2 = ['','','','']
        self.setor3 = ['','','','']
        self.setor4 = ['','','','']
            
    def estacionar(self,setor, carro):
        for x in range(0,len(setor)):
           if setor[x] == "":
              setor[x] = carro
              return setor
           else:
              pass
    def retirar(self,setor,carro):
        for x in range(0,len(setor)):
           if setor[x] == carro:
              setor[x] = ""
              return setor

           else:
              pass
                   

estacionamento1 = Estacionamento("shopping")

while(True):
    print(f'1 - Setor 1: {estacionamento1.setor1}')
    print(f'2 - Setor 2: {estacionamento1.setor2}')
    print(f'3 - Setor 3: {estacionamento1.setor3}')
    print(f'4 - Setor 4: {estacionamento1.setor4}')
    carro = input ("Qual o nome do carro que você deseja estacionar? ")
    setor = int(input("Digite o numero do setor que deseja estacionar "))
    if setor == 1:
        estacionamento1.estacionar(estacionamento1.setor1,carro)
    elif setor == 2:
        estacionamento1.estacionar(estacionamento1.setor2,carro)
    elif setor == 3:
        estacionamento1.estacionar(estacionamento1.setor3,carro)
    elif setor == 4:
        estacionamento1.estacionar(estacionamento1.setor4,carro)
    else:
        print("Digite um setor existente")
    resposta = input("Deseja adicionar mais algum carro? s/n ")
    if resposta == "s":
        pass
    else:
        break
while(True):    
    print(f'1 - Setor 1: {estacionamento1.setor1}')
    print(f'2 - Setor 2: {estacionamento1.setor2}')
    print(f'3 - Setor 3: {estacionamento1.setor3}')
    print(f'4 - Setor 4: {estacionamento1.setor4}')
    carro = input("Qual carro você deseja retirar? ")
    setor = int(input("Em qual setor ele está?"))
    if setor == 1:
        estacionamento1.retirar(estacionamento1.setor1,carro)
    elif setor == 2:
        estacionamento1.retirar(estacionamento1.setor2,carro)
    elif setor == 3:
        estacionamento1.retirar(estacionamento1.setor3,carro)
    elif setor == 4:
        estacionamento1.retirar(estacionamento1.setor4,carro)
    else:
        print("Digite um setor existente")


    