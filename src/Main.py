def devolver_equipamento(equipamentos, id):
    """Função para devolver um equipamento dado um dicionário de equipamentos e um ID."""
    if id in equipamentos:
        equipamento = equipamentos[id]
        if equipamento['status'] == 'emprestado':
            equipamento['status'] = 'disponível'
            print(f"Equipamento '{equipamento['nome']}' devolvido com sucesso.")
        else:
            print(f"Equipamento '{equipamento['nome']}' já está disponível.")
    else:
        print(f"Equipamento com ID {id} não encontrado.")

def listar_equipamentos(equipamentos):
    """Função para listar todos os equipamentos e seus status."""
    for id, info in equipamentos.items():
        print(f"ID: {id}, Nome: {info['nome']}, Status: {info['status']}")

