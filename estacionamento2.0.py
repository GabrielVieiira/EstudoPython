class Estacionamento:
    nome = None
    setor = None
    def __init__(self,vagas):
        self.setor = [['','','',''],['','','',''],['','','',''],['','','','']]
        self.vagas = vagas    
    def estacionar(self):
        placa = input("Nos informe a placa do seu veículo: ")
        for l in range(4):
            for c in range(4):
                if estacionamento1.setor[c][l] == "":
                    estacionamento1.setor[c][l] = placa
                    estacionamento1.vagas -= 1 
                    return estacionamento1
                else:
                    pass

    def retirar(self):
        placa = input("Nos informe a placa do seu veículo: ")
        for l in range(4):
            for c in range(4):
                if estacionamento1.setor[c][l] == placa:
                    estacionamento1.setor[c][l] = ""
                    estacionamento1.vagas += 1 
                    return estacionamento1
                else:
                    pass

    def verificar_vagas(self):
        if estacionamento1.vagas == 0:
            print(estacionamento1.setor)
            print(f'Restam {estacionamento1.vagas} vagas')
            print("O estacionamento está lotado!")
            resposta = input("Deseja retirar algum carro? s/n ")
            return resposta 
        else:
                              
            print(f'Restam {estacionamento1.vagas} vagas')
            resposta = input("Digite o que deseja fazer: \n 1 - Estacionar \n 2 - Retirar Carro \n 3 - Sair ")
            return resposta
vagas = 16                
estacionamento1 = Estacionamento(vagas)

print("Bem vindo ao estacionamento SENAC")
while(True):   
    resposta = estacionamento1.verificar_vagas()    
    while(resposta == "s") :
        estacionamento1.retirar()
        print(estacionamento1.setor)
        resposta = input("Deseja retirar mais algum carro? s/n ")
        if resposta == "s":
            resposta = "s"
        elif resposta == "n":
            break
        else:
            print("Opção invalida")
            break
    if resposta == "1":
        estacionamento1.estacionar()
        print(estacionamento1.setor)
    elif resposta == "2":
        estacionamento1.retirar()
        print(estacionamento1.setor)    
    elif resposta == "3":
        break    
    else:
        print("Dixa de ser burro")
                        
                    
                    
                    
                        
        d