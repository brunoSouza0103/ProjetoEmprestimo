# Listar equipamentos emprestados e com quem está;
# Listar equipamentos disponíveis para empréstimo;
# Listar equipamentos em manutenção;
# Listar equipamentos baixados (para jogar fora);

def listagem(): 
    print("\n1- Os equipamentos emprestados e com quem está")
    print("\n2- Os equipamentos disponíveis para empréstimo")
    print("\n3- Os equipamentos em manutenção")
    print("\n4- Os equipamentos baixados (para jogar fora)")
    print("\nO que você deseja ver ?")
    escolha = int(input())

    if escolha == 1:
        emprestados()
    elif escolha == 2:
        disponiveis()
    elif escolha ==3:
        manutencao()
    elif escolha==4:
        baixados()


def emprestados():
    
def disponiveis():

def manutencao():

def baixados():
