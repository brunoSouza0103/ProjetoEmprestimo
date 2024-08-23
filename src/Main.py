#Equipamento
# código;
# descrição;
# estado(novo, usado, defeito, baixado);
# situação(disponivel, manutenção, emprestado);
# responsável;
# data e hora (se emprestado);

def cadastrarEquipamento():
    equipamentos = []
    print("Cadastrar novo equipamento. \n")
    cod = str(input("Código: "))
    desc = str(input("Descrição: "))
    estado = str(input("Estado (Novo, Usado, Defeito, Baixado): "))
    situacao = str(input("Situação (Disponivel, Manutenção, Emprestado): "))
    responsavel = str(input("Responsável: "))
    dataehora = str(input("Data e hora (Se emprestado): "))

    equipamento = (cod, desc, estado, situacao, responsavel, dataehora)
    equipamentos.append(equipamento)

    print(equipamentos[0])

cadastrarEquipamento()



