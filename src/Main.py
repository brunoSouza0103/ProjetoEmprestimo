#Funcionário:
#   cpf;
#   nome;
#   telefone (whats);
#   email;

def cadastrarPessoa():
    pessoas = []
    print("Cadastrar novo funcionário. \n")
    cpf = str(input("Cpf: "))
    nome = str(input("Nome: "))
    telefone = str(input("Telefone: "))
    email = str(input("Email: "))

    # Adicionando os dados como uma tupla
    pessoa = (cpf, nome, telefone, email)
    pessoas.append(pessoa)

    print(pessoas[0])

cadastrarPessoa()



