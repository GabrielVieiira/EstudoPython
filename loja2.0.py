def add_produtos(dicionario):
    flag = True
    indice = 1
    while(flag):      
        produto = input("Qual produto deseja adicionar? ")
        valor = float(input("Qual o valor do produto? R$"))
        dicionario["produto"].append(produto)
        dicionario["valor"].append(valor)
        dicionario["indice"].append(indice)
        indice += 1
        flag1 = True
        while(flag1):  
            resp = input("Deseja adicionar mais um produto? s/n ")
            if resp == "s":
                flag1 = False
            elif resp == "n":
                flag1 = False
                flag = False
            else:
                print("Digite uma opção válida")
    return dicionario
     

def menu(dicionario):
    print("Digite o numero do item que deseja adicionar ao carrinho?")
    for chave in range(0,len(dicionario["indice"])):
        print(dicionario["indice"][chave], " - ",dicionario["produto"][chave], " - R$:",dicionario["valor"][chave])
    resp = int(input())
    return resp


def add_carrinho(dicionario, produto_selecao):
    quantidade = 0
    produto_selecionado = dicionario["produto"][produto_selecao-1]
    valor = dicionario["valor"][produto_selecao-1]
    quantidade += int(input(f'O item selecionado foi {produto_selecionado}. Qual a quantidade deseja?'))    
    carrinho["produto"].append(produto_selecionado)
    carrinho["quantidade"].append(quantidade)
    valor = valor * quantidade
    carrinho["valor"].append(valor)
    print(f'Você adicionou {quantidade} {produto_selecionado}    Total: R$: {valor}')
    return carrinho

def valor_compra(carrinho):
    valor = 0
    for x in range(0,len(carrinho['produto'])):
        valor += carrinho['valor'][x]
    return valor

carrinho = {
    'produto': [],
    'quantidade': [],
    'valor': []
}

dicionario = {
    'indice': [],
    'produto': [],
    'valor':[]
}


print('Olá! Bem vindo sistema de vendas SENAC')
dicionario = add_produtos(dicionario)
flag = True
while(flag):
    resposta = menu(dicionario)
    carrinho = add_carrinho(dicionario, resposta)
    resposta = input("Deseja adicionar mais produtos? s/n ")
    if resposta == "s":
        pass
    elif resposta == "n":
        flag = False
    else:
        print("Digite uma opção válida")
for chave in range(0,len(carrinho["produto"])):
    print('Você adicionou:', carrinho["quantidade"][chave], " ",carrinho["produto"][chave], " Valor: R$:",carrinho["valor"][chave])
resposta = input('Confirma? s/n')
if resposta == "s":
    carrinho_set = set(carrinho['produto'])
    print(len(carrinho_set))
    valor_carrinho = valor_compra(carrinho)
    if len(carrinho_set) >= 3 and len(carrinho_set) < 5 :
            valor_carrinho = valor_carrinho*0.9
            print(f'Você se elege para a nossa promoção(que não vem ao caso explicar qual é) e recebeu 10% de desconto valor da compra: R$ {valor_carrinho}')
    elif len(carrinho_set) >= 5:
            valor_carrinho = valor_carrinho*0.8
            print(f'Você se elege para a nossa promoção(que não vem ao caso explicar qual é) e recebeu 20% de desconto valor da compra: R$ {valor_carrinho}')
    else:
            print(f'Valor da compra: R$ {valor_carrinho}')
elif resposta =="n":
     print("Deseja retirar algum item?")    

   