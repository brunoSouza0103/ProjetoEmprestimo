def menuInicial():
    menu = 1
    while menu != 0:
        print("Escolha o que você deseja fazer\n 1. Cadastrar Funcionário\n 2. Cadastrar Equipamento\n 3. Emprestar Equipamento\n 4. Devolver Equipamento\n 5. Listar Equipamentos\n 0. Sair")
        menu = int(input("Digite uma opção: "))

        if menu == 1:
            # cadastrar pessoa
            print("cadastrar pessoa")
        elif menu == 2:
            # cadastrar equipamento
            print("cadastrar equipamento")
        elif menu == 3:
            # emprestar equipamento
            print("emprestar equipamento")
        elif menu == 4:
            # devolver equipamento
            print("devolver equipamento")
        elif menu == 5:
            # listar equipamentos
            print("listar equipamentos")
        else:
            # sair
            print("sair")

menuInicial()