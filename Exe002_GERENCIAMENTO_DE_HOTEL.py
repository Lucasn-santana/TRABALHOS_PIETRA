# Sistema de Gerenciamento de Hotel

# Lista para armazenar os dados dos hóspedes
hospedes = []

# Função para cadastrar um hóspede
def cadastrar_hospede():
    nome = input("Nome do hóspede: ")
    numero_quarto = input("Número do quarto: ")
    data_entrada = input("Data de entrada (dd/mm/aaaa): ")
    data_saida = input("Data de saída (dd/mm/aaaa): ")
    hospedes.append({
        "nome": nome,
        "numero_quarto": numero_quarto,
        "data_entrada": data_entrada,
        "data_saida": data_saida
    })
    print("Hóspede cadastrado com sucesso!")

# Função para consultar quartos disponíveis
def consultar_quartos_disponiveis():
    quartos_ocupados = [hospede["numero_quarto"] for hospede in hospedes]
    todos_quartos = [str(i) for i in range(1, 21)]  # Supondo que o hotel tenha 20 quartos
    quartos_disponiveis = [quarto for quarto in todos_quartos if quarto not in quartos_ocupados]
    print("Quartos disponíveis:", ", ".join(quartos_disponiveis))

# Função para registrar entrada de hóspede
def registrar_entrada():
    nome = input("Nome do hóspede: ")
    for hospede in hospedes:
        if hospede["nome"] == nome:
            hospede["data_entrada"] = input("Nova data de entrada (dd/mm/aaaa): ")
            print("Entrada registrada com sucesso!")
            return
    print("Hóspede não encontrado!")

# Função para registrar saída de hóspede
def registrar_saida():
    nome = input("Nome do hóspede: ")
    for hospede in hospedes:
        if hospede["nome"] == nome:
            hospede["data_saida"] = input("Nova data de saída (dd/mm/aaaa): ")
            print("Saída registrada com sucesso!")
            return
    print("Hóspede não encontrado!")

# Função para listar todos os hóspedes cadastrados
def listar_hospedes():
    if not hospedes:
        print("Nenhum hóspede cadastrado.")
    else:
        for hospede in hospedes:
            print(f"Nome: {hospede['nome']}, Quarto: {hospede['numero_quarto']}, Entrada: {hospede['data_entrada']}, Saída: {hospede['data_saida']}")

# Menu principal
def menu():
    while True:
        print("\nSistema de Gerenciamento de Hotel")
        print("1. Cadastrar hóspede")
        print("2. Consultar quartos disponíveis")
        print("3. Registrar entrada de hóspede")
        print("4. Registrar saída de hóspede")
        print("5. Listar hóspedes cadastrados")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_hospede()
        elif opcao == "2":
            consultar_quartos_disponiveis()
        elif opcao == "3":
            registrar_entrada()
        elif opcao == "4":
            registrar_saida()
        elif opcao == "5":
            listar_hospedes()
        elif opcao == "6":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Executar o menu
menu()
