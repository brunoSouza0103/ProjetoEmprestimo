def adicionar_linha(matriz, codigo, descricao, status='disponível', responsavel=None, situacao='novo'):
    matriz.append([codigo, descricao, status, responsavel, situacao])

matriz = []

while True:
    codigo = input("Digite o código do equipamento (ou 'sair' para encerrar): ").strip()
    
    if codigo.lower() == 'sair':
        break
    descricao = input("Digite a descrição do seu equipamento: ")
    entrada = input("Digite o status do equipamento (d para Disponível, e para Emprestado, m para Manutenção): ").strip().lower()
    
    if entrada == 'd':
        status = 'disponível'
    elif entrada == 'e':
        status = 'emprestado'
    elif entrada == 'm':
        status = 'manutenção'
    else:
        print("Status inválido. Por favor, digite 'd' para disponível, 'e' para emprestado ou 'm' para manutenção.")
        continue
    
    responsavel = input("Digite o nome do responsável (deixe em branco se não houver): ").strip() or None
    
    estado = input("Digite o estado do equipamento (n para novo, u para usado, d para defeito, b para baixado): ").strip().lower()
    
    if estado == 'n':
        situacao = 'novo'
    elif estado == 'u':
        situacao = 'usado'
    elif estado == 'd':
        situacao = 'defeito'
    elif estado == 'b':
        situacao = 'baixado'
    else:
        print("Estado inválido. Por favor, digite 'n' para novo, 'u' para usado, 'd' para defeito ou 'b' para baixado.")
        continue

    
    adicionar_linha(matriz, codigo, descricao, status, responsavel, situacao)
    
    print("\nMatriz atual:")
    for linha in matriz:
        print(linha)

print("\nMatriz final:")
for linha in matriz:
    print(linha)

