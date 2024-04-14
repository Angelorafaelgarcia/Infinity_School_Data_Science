# Você está desenvolvendo um programa para gerenciar uma lista de compras. 
# O programa permite adicionar produtos à lista, visualizar a lista de produtos, 
# atualizar as informações de um produto existente e remover produtos da lista. 
# Além disso, o programa calcula o valor total de todos os produtos da lista.

# O programa oferece as seguintes opções:
# Adicionar produtos: O usuário pode adicionar um novo produto à lista informando o nome, a quantidade e o valor unitário do produto. O programa calcula automaticamente o valor total do produto (quantidade * valor unitário) e atualiza o valor total de todos os produtos.
# Ver a lista de produtos: O programa exibe a lista de produtos adicionados até o momento, mostrando o nome do produto, o valor unitário, a quantidade e o valor total do produto. Além disso, exibe o valor total de todos os produtos da lista.
# Atualizar produtos: O usuário pode atualizar as informações de um produto existente na lista. O programa solicita o nome do produto que deseja atualizar e, em seguida, permite editar o nome, a quantidade e o valor unitário do produto. O programa recalcula automaticamente o valor total do produto e o valor total de todos os produtos.
# Remover produto: O usuário pode remover um produto da lista informando o nome do produto que deseja remover. O programa atualiza automaticamente o valor total de todos os produtos.
# Encerrar programa: Encerra a execução do programa.
# O programa utiliza uma lista para armazenar os produtos, onde cada produto é representado por um dicionário com as informações: "produto", "valor", "quantidade" e "total". A variável totalProdutos é utilizada para armazenar o valor total de todos os produtos da lista.
# A cada operação realizada, o programa exibe mensagens indicando o resultado da operação.

produtos = []
total_produtos = 0

def adic_produto():
    nome = str(input("Informe o Nome do Produto: "))
    quant_itens = int(input("Informe a Quantidade: "))
    valor_unitario = float(input("Informe o Valor Unitario: "))

    total = quant_itens * valor_unitario
    global total_produtos
    total_produtos += total
    produtos.append({
        "Produto":nome,
        "Valor":valor_unitario,
        "Quantidade":quant_itens,
        "Total":total
    })
    print("Produto Adicionado Com Sucesso!")

def visual_Lista():
    if not produtos:
        print("Alista de Produtos Esta Vazia.")
    else:
        print("Lista De Produtos: ")
        for produto in produtos:
            print(f"Nome:{produto['Produto']},Quantidade:{produto['Quantidade']},Valor Unitario:{produto['Valor']},Valor Total:{produto['Total']}")
            print(f"Valor Total De Todos Os Produtos:{total_produtos}")

def atualizar_produto():
    nome = str(input("Informe O Nome Do Produto Que Deseja Atualizar: "))
    for produto in produtos:
        if produto ["Produto"] == nome:
            quantidade = int(input("Informe A Nova Quantidade: "))
            valor_Unitario = float(input("Informe O Novo Valor Unitario: "))
            produto["Quantidade"] = quantidade
            produto["Valor"] = valor_Unitario
            produto["Total"] = quantidade * valor_Unitario
            recalcular_total()
            print("Produto Atualizado Com Sucesso!")
            return
        print("Produto Não Encontrado Na Lista.")

def remover_produto():
    nome = str(input("Informe O Nome Do Produto Que Deseja Remover: "))
    global total_produtos
    for produto in produtos:
        if produto["Produto"] == nome:
            total_produtos -= produto["Total"]
            produtos.remove(produto)
            print("Produto Removido Com Sucesso. ")
            return
        print("Produto Não Encontrado Na Lista. ")

def recalcular_total():
    global total_produtos
    total_produtos = 0
    for produto in produtos:
        total_produtos += produto["Total"]

def main():
    while True:
        print("\nEscolha a Opção: ")
        print("1. Adicionar Produto ")
        print("2. Ver Lista De Produtos ")
        print("3. Atualizar Produto ")
        print("4. Remover Produto ")
        print("5. Encerra Programa ")

        opcao = int(input("Opção: "))

        if opcao == 1:
            adic_produto()
        elif opcao == 2:
            visual_Lista()
        elif opcao == 3:
            atualizar_produto()
        elif opcao == 4:
            remover_produto()
        elif opcao == 5:
            print("Programa Encerrado. ")
            break
        else:
            print("Opção Invalida. Escolha Um Numero De 1 A 5. ")
if __name__ == "__main__":
    main()
