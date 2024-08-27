matriz_pessoa = []

def cpf_existente(matriz_pessoa, cpf):
    for linha in matriz_pessoa:
        if linha[1] == cpf:
            return True
    return False

def add_linha_pessoa(nome, cpf, email, celular):
    matriz_pessoa.append([nome, cpf, email, celular])

def cadastrarPessoa() :

    while True:
        nome = input("Digite o seu nome (ou 'sair' para encerrar): ").strip()
        if nome.lower() == 'sair':
            break

        while True:
            cpf = input("Digite o seu CPF (somente números): ").strip()
            cpf = cpf.replace('.', '').replace('-', '')
            if cpf.isdigit() and len(cpf) == 11:
                if cpf_existente(matriz_pessoa, cpf):
                    print("O CPF já existe no sistema. Vamos começar novamente.")
                    break
                else:
                    break
            else:
                print("CPF inválido, deve ter exatamente 11 dígitos.")
        
        if cpf_existente(matriz_pessoa, cpf):
            continue

        while True:
            email = input("Digite o seu e-mail: ").strip()
            if '@' in email:
                break
            else:
                print("Email inválido, adicione o '@'.")

        while True:
            celular = input("Digite o seu número celular com DDD (somente números e 11 dígitos): ").strip()
            if celular.isdigit() and len(celular) == 11:
                break
            else:
                print("Número celular inválido, digite um número com exatamente 11 dígitos sem espaços ou caracteres especiais.")
        
        add_linha_pessoa(nome, cpf, email, celular)
        print("Funcionário adicionado com sucesso")

        print("\nMatriz atual:")
        for linha in matriz_pessoa:
            print(linha)

    print("\nMatriz final:")
    for linha in matriz_pessoa:
        print(linha)

cadastrarPessoa()

