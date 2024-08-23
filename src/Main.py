matriz = []

def adicionar_linha(matriz, nome, status='disponível', responsavel=None):
    matriz.append([nome, status, responsavel])

while True:
    nome = input("Digite o nome do equipamento (ou 'sair' para encerrar): ").strip()
   
    if nome.lower() == 'sair':
        break
   
    entrada = input("Digite o status (d para disponível ou i para indisponível): ").strip().lower()
    if entrada == 'd':
        status = 'disponível'
    elif entrada == 'i':
        status = 'indisponível'
    else:
        print("Status inválido. Por favor, digite 'd' para disponível ou 'i' para indisponível.")
        continue  # Pular para a próxima iteração do loop sem adicionar a linha
   
    responsavel = input("Digite o nome do responsável (deixe em branco se não houver): ").strip() or None
   
    adicionar_linha(matriz, nome, status, responsavel)
   
    print("\nMatriz atual:")
    for linha in matriz:
        print(linha)

print("\nMatriz final:")
for linha in matriz:
    print(linha)

