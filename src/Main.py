matriz = []

def adicionar_linha(matriz, codigo, status='disponível', responsavel=None, situacao='novo'):
    matriz.append([codigo, status, responsavel, situacao ])

while True:
    codigo = input("Digite o código do equipamento (ou 'sair' para encerrar): ").strip()
   
    if codigo.lower() == 'sair':
        break
   
    entrada = input("Digite o status do equipamento (d para Disponível, e para Emprestado, m para Manutenção): ").strip().lower()
    if entrada == 'd':
        status = 'disponível'
    elif entrada == 'i':
        status = 'indisponível'
    elif entrada == 'm':
        status = 'manutenção'
    else:
        print("Status inválido. Por favor, digite 'd' para disponível, 'i' para indisponível, 'm' para manutenção: ")
        continue  
   
    responsavel = input("Digite o nome do responsável (deixe em branco se não houver): ").strip() or None
    estado = input("Digite o estado do equipamento (letra n para novo, u para usado, d para defeito, b para baixado: ")
    if estado == 'n':
        situacao = 'novo'
    if estado == 'u':
        situacao = 'usado'
    if estado =='d':
        situacao = 'defeito'
    if estado =='b':
        situacao ='baixado'
    else:
        print("Estado inválido. Por favor, digite 'n' para novo, 'u' para usado, 'd' para defeito ou 'b' para baixado")
        continue 
   
    adicionar_linha(matriz, codigo, status, responsavel, situacao)
   
    print("\nMatriz atual:")
    for linha in matriz:
        print(linha)

print("\nMatriz final:")
for linha in matriz:
    print(linha)

