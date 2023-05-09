def addProdutos(produto, valor, indice):
    dicionario["produto"].append(produto)
    dicionario["valor"].append(valor)
    dicionario["indice"].append(indice)
     

def menu(dicionario):
    for chave in dicionario:
        print(f"{chave} valor R$: {dicionario[chave]}")

def addCarrinho(quantidade, produto_selecionado, valor):
    carrinho["produto"].append(produto_selecionado)
    carrinho["quantidade"].append(quantidade)
    valor = valor * quantidade
    print(f'Você adicionou {quantidade} {produto_selecionado}    Total: R$: {valor}')

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
flag = True
indice = 1
while(flag):      
    produto = input("Qual produto deseja adicionar? ")
    valor = float(input("Qual o valor do produto? R$"))
    addProdutos(produto, valor, indice)
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
flag2 = True


while(flag2):   
    quantidade = 0
    print("Digite o numero do item que deseja adicionar ao carrinho?")
    for chave in range(0,len(dicionario["indice"])):
        print(dicionario["indice"][chave], " - ",dicionario["produto"][chave], " - R$:",dicionario["valor"][chave])
    produto_selecao = int(input())
    produto_selecionado = dicionario["produto"][produto_selecao-1]
    valor_selecionado = dicionario["valor"][produto_selecao-1]
    quantidade += int(input(f'O item selecionado foi {produto_selecionado}. Qual a quantidade deseja?'))
    addCarrinho(quantidade,produto_selecionado, valor_selecionado)
   
    resp = input("Deseja adicionar mais produtos? s/n ")
    if resp == "s":
        pass
    elif resp == "n":
        flag2 = False
    else:
        print("Digite uma opção válida") 
print(carrinho)

    
