def logicaEmprestimo():

    print("Voce escolheu emprestar um equipamento.\n")
    
    nome = input("Digite seu nome:")
    cpf = input("Informe seu CPF:")
    
    while True:
        print("Atual lista de equipamentos disponíveis para empréstimo:")
        for linha in matriz:
            print(linha)
        
        linhae = int(input("Informe a linha do equipamento que deseja esmprestar(0,1,2,3...):"))
        
        if matriz[linhae][2] == 'disponível':
            print("Empréstimo realizado com sucesso!")
            matriz[linhae][2] = 'emprestado'
            break
        elif matriz [linhae][2] == 'emprestado':
            print("Este equipamente já está emprestado, selecione outro!")
            continue
        else:
            print("Este equipamento está em manutenção, selecione outro!")
            continue
            
    print("\nLista de equipamentos atualizada:")
        
    for linha in matriz:
        print(linha)

logicaEmprestimo()