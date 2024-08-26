def cpf_existente(matriz, cpf):
    for linha in matriz:
        if linha[1]==cpf:
            return True
    return False

def adicionar_linha(nome, cpf, email, celular):
    matriz.append([nome, cpf, email, celular])

matriz = []

while True:
    nome = input("Digite o seu nome (ou 'sair' para encerrar): ").strip()
   
    if nome.lower() == 'sair':
        break
   
    while True:
        cpf = input("Digite o seu CPF: ").strip()
        cpf = cpf.replace('.', '').replace('-', '') #para retirar pontos e traços
        if cpf.isdigit() and len(cpf) == 11:
            if cpf_existente(matriz,cpf):
                print("\n")
            break
        else:
            break
    else:
        print("CPF inválido, digite apenas números no formato (12345678901).")
    
    if cpf_existente(matriz,cpf):
        print("O CPF ja existe no sistema, cadastre do começo.")
        continue
    
    while True:
        email = input("Digite o seu e-mail: ").strip()
        if '@' in email:
            break
        else:
            print("Email inválido, adicione o '@'.")

    while True:
        celular = input("Digite o seu número celular com DDD: ").strip()
        if celular.isdigit() and len(celular) == 11:
            break
        else:
            print("Número celular inválido, digite um número com apenas 11 dígitos sem espaço após o DDD.")
            
    if not cpf_existente(matriz,cpf):
        adicionar_linha(nome, cpf, email, celular)
        print ("Funcionário adicionado com sucesso")
    else:
       print ("Não foi possível adicionar o funcionário pois o CPF ja existe no sistema")

    print("\nMatriz atual:")
    for linha in matriz:
        print(linha)
        

print("\nMatriz final:")
for linha in matriz:
    print(linha)

