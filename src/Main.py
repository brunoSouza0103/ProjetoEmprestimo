matriz_pessoa = []
matriz_equipamentos = []

def adicionarPessoa():
    def cpf_existente(matriz_pessoa, cpf):
        for linha in matriz_pessoa:
            if linha[1] == cpf:
                return True
        return False

    def add_linha_pessoa(nome, cpf, email, celular):
        matriz_pessoa.append([nome, cpf, email, celular])

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

def cadastrarEquipamento():
    def adicionar_linha(matriz_equipamentos, codigo, descricao, status='disponível', responsavel=None, situacao='novo'):
        matriz_equipamentos.append([codigo, descricao, status, responsavel, situacao])

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

        adicionar_linha(matriz_equipamentos, codigo, descricao, status, responsavel, situacao)
        print("Equipamento adicionado com sucesso")

def logicaEmprestimo():
    print("Você escolheu emprestar um equipamento.\n")
    
    nome = input("Digite seu nome:")
    cpf = input("Informe seu CPF:")
    
    while True:
        print("Atual lista de equipamentos disponíveis para empréstimo:")
        for i, linha in enumerate(matriz_equipamentos):
            if linha[2] == 'disponível':
                print(f"{i} - {linha}")
        
        try:
            linhae = int(input("Informe a linha do equipamento que deseja emprestar, ou digite 's' para sair (0,1,2,3...):"))

            if linhae < 0 or linhae >= len(matriz_equipamentos):
                print("Esta linha não existe, escolha outra!")
                continue

            if matriz_equipamentos[linhae][2] == 'disponível':
                print("Empréstimo realizado com sucesso!")
                matriz_equipamentos[linhae][2] = 'emprestado'
                matriz_equipamentos[linhae][3] = nome
                break
            elif matriz_equipamentos[linhae][2] == 'emprestado':
                print("Este equipamento já está emprestado, selecione outro!")
                continue
            elif matriz_equipamentos[linhae][2] == 'manutenção':
                print("Este equipamento está em manutenção, selecione outro!")
                continue
        except ValueError:
            break
            
def devolver_equipamento():
    print("Devolver Equipamento\n")
    codigo = input("Digite o código do equipamento a ser devolvido: ")

    for equipamento in matriz_equipamentos:
        if equipamento[0] == codigo and equipamento[2] == 'emprestado':
            equipamento[2] = 'disponível'
            equipamento[3] = None
            print(f"Equipamento '{equipamento[1]}' devolvido com sucesso.")
            return
    print("Equipamento não encontrado ou não está emprestado.")

def listarEquipamentos():
    def emprestados(matriz):
        encontrou_emprestado = False
    
        print("\nEquipamentos emprestados e com quem está:")
        for linha in matriz_equipamentos:
            if linha[1] == 'emprestado':                                 #Verifica se esta na situação "emprestado"
                print(f"Equipamento: {linha[1]}, Código: {linha[0]}, Responsável: {linha[3]}")
                encontrou_emprestado = True
        
        if not encontrou_emprestado:
            print("Nenhum equipamento está emprestado")

    def disponiveis(matriz):
        encontrou_disponivel = False
    
        print("\nEquipamentos disponíveis para empréstimo:")
           
        for linha in matriz_equipamentos:
            if linha[2] == 'disponível':                                 #Verifica se esta na situação "disponível"
                print(f"Equipamento: {linha[1]}, Código: {linha[0]}")
                encontrou_disponivel = True
        
        if not encontrou_disponivel: #se n encontrar disponivel da o print
            print("Nenhum equipamento está disponivel.")

    def manutencao(matriz_equipamentos):
        encontrou_manutencao = False
        
        print("\nEquipamentos em manutenção:")
            
        for linha in matriz_equipamentos:
            if linha[2] == 'manutenção':
                print(f"Equipamento: {linha[1]}, Código: {linha[0]}")
                encontrou_manutencao = True
        
        if not encontrou_manutencao: #se n encontrar manutencao da o print
            print("Nenhum equipamento está em manutenção.")

    def baixados(matriz):
        equipamento_baixado = False
    
        print("\nEquipamentos baixados (para jogar fora):")
        for linha in matriz:
            if linha[3] == 'baixado':                                    #Verifica se esta com o status "baixado"
                print(f"Equipamento: {linha[1]}, Código: {linha[0]}")
                equipamento_baixado = True
        
        if not equipamento_baixado:
            print("Nenhum equipamento foi baixado")

    def listagem(matriz_equipamentos):
        print("\n1- Equipamentos emprestados e com quem está")
        print("2- Equipamentos disponíveis para empréstimo")
        print("3- Equipamentos em manutenção")
        print("4- Equipamentos baixados")
        print("\nO que você deseja ver? (Digite o número da opção)")
    
        escolha = input()

        if escolha == '1':
            emprestados(matriz_equipamentos)
        elif escolha == '2':
            disponiveis(matriz_equipamentos)
        elif escolha == '3':
            manutencao(matriz_equipamentos)
        elif escolha == '4':
            baixados(matriz_equipamentos)
        else:
            print("Opção inválida. Por favor, digite um número de 1 a 4.")
            listagem(matriz_equipamentos)
    listagem(matriz_equipamentos)

def Main():
    menu = 1
    while menu != 0:
        print("\nEscolha o que você deseja fazer\n 1. Cadastrar Funcionário\n 2. Cadastrar Equipamento\n 3. Emprestar Equipamento\n 4. Devolver Equipamento\n 5. Listar Equipamentos\n 0. Sair")
        menu = input("Digite uma opção: ")

        if menu == '1':
            adicionarPessoa()
        elif menu == '2':
            cadastrarEquipamento()
        elif menu == '3':
            logicaEmprestimo()
        elif menu == '4':
            devolver_equipamento()
        elif menu == '5':
            listarEquipamentos()
        elif menu == '0':
            print("Saindo...")
        else:
            print("\nO que você digitou está errado, digite um dos numeros pedidos")

Main()
