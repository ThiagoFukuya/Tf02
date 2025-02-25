# Criando um inventário como um dicionário
inventario = {}

def adicionar_produto(nome, preco, quantidade):
    inventario[nome] = {
        'preco': preco,
        'quantidade': quantidade
    }
    print(f"Produto '{nome}' adicionado ao inventário.")

def remover_produto(nome):
    if nome in inventario:
        del inventario[nome]
        print(f"Produto '{nome}' removido do inventário.")
    else:
        print(f"Produto '{nome}' não encontrado no inventário.")

def mostrar_inventario():
    if not inventario:
        print("O inventário está vazio.")
        return
    print("\nInventário de Produtos:")
    for nome, info in inventario.items():
        print(f"Nome: {nome}, Preço: R${info['preco']:.2f}, Quantidade: {info['quantidade']}")

# Loop principal para interação com o usuário
while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar produto")
    print("2. Remover produto")
    print("3. Listar produtos")
    print("4. Sair")
    
    opcao = input("Opção: ")

    if opcao == "1":
        nome = input("Nome do produto: ")
        preco = float(input("Preço do produto: "))
        quantidade = int(input("Quantidade do produto: "))
        adicionar_produto(nome, preco, quantidade)
    
    elif opcao == "2":
        nome = input("Nome do produto a remover: ")
        remover_produto(nome)
    
    elif opcao == "3":
        mostrar_inventario()
    
    elif opcao == "4":
        print("Saindo do programa.")
        break
    
    else:
        print("Opção inválida. Tente novamente.")
