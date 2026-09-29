personagens = [
    {
        "nome":"Arthos",
        "classe":"Guerreiro",
        "nivel":1,
        "inventario":[
            ("Espada de ferro","arma"),
            ("Poção de cura","poção")
        ]
    }
]

personagem = []

def criar_personagem():
    nome = input("Nome do personagem: ")
    classe = input("Classe do personagem: ")
    nivel = int(input("Nível do personagem: "))

    personagem = {
        "nome": nome,
        "classe": classe,
        "nivel": nivel,
        "inventario":[]
    }

    personagens.append(personagem)

def adicionar_item_inventario():
    nome = input("Nome do personagem: ")

    for personagem in personagens:
        if personagem["nome"] == nome:
            item_nome = input("Nome do item: ")
            item_tipo = input("Tipo do item (arma, poção, armadura): ")

            item = (item_nome, item_tipo)

            personagem["inventario"].append(item)

            print("Item adicionado ao inventário!\n")
            return
    print("Personagem não encontrado.\n")

def exibir_inventario():
    nome = input("Nome do personagem: ")

    for personagem in personagens:
        if personagem["nome"] == nome:
            if not personagem["inventario"]:
                print("Inventário vazio.\n")
                return

            print(f"\nInventário de {personagem['nome']}:")
            for item in personagem["inventario"]:
                print(f"- {item[0]} ({item[1]})")
            print()
            return

    print("Personagem não encontrado.\n")

def remover_item_inventario():
    nome = input("Nome do personagem: ")

    for personagem in personagens:
        if personagem["nome"] == nome:
            if not personagem["inventario"]:
                print("Inventário vazio.\n")
                return

            item_nome = input("Nome do item a remover: ")

            for item in personagem["inventario"]:
                if item[0] == item_nome:
                    personagem["inventario"].remove(item)
                    print("Item removido do inventário!\n")
                    return

            print("Item não encontrado.\n")
            return

    print("Personagem não encontrado.\n")

while True:
    print("\n=== MENU PRINCIPAL DO JOGO ===")
    print("1 - Criar personagem")
    print("2 - Adicionar item ao inventário")
    print("3 - Exibir inventário do personagem")
    print("4 - Remover item do inventário")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        criar_personagem()
    elif opcao == "2":
        adicionar_item_inventario()
    elif opcao == "3":
        exibir_inventario()
    elif opcao == "4":
        remover_item_inventario()
    elif opcao == "0":
        print("Encerrando o jogo...")
        break
    else:
        print("Opção inválida.\n")