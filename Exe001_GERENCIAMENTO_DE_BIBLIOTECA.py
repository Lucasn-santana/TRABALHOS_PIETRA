# Sistema de Gerenciamento de Biblioteca

#ESTRUTURA PARA ARMAZENAR OS LIVROS
class Biblioteca:
    def __init__(self):
        self.livros = []
        self.livros_emprestados = []

#CADASTRANDO OS LIVROS
    def cadastrar_livro(self, titulo, autor, ano):
        if len(self.livros) < 5:
            self.livros.append({'titulo': titulo, 'autor': autor, 'ano': ano})
            print(f"Livro '{titulo}' cadastrado com sucesso!")
        else:
            print("Limite de 5 livros cadastrados atingido.")

#CONSULTANDO LIVROS DISPONÍVEIS
    def consultar_livros(self):
        if self.livros:
            print("Livros disponíveis na biblioteca:")
            for livro in self.livros:
                print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}")
        else:
            print("Nenhum livro disponível na biblioteca.")

#LISTANDO LIVROS CADASTRADOS
    def listar_livros_cadastrados(self):
        if self.livros:
            print("Lista de livros cadastrados:")
            for livro in self.livros:
                print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}")
        else:
            print("Nenhum livro cadastrado na biblioteca.")

#EMPRESTANDO LIVROS DISPONÍVEIS
    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro['titulo'] == titulo:
                self.livros_emprestados.append(livro)
                self.livros.remove(livro)
                print(f"Livro '{titulo}' emprestado com sucesso!")
                return
        print(f"Livro '{titulo}' não encontrado ou já emprestado.")

#DEVOLVENDO LIVROS EMPRESTADOS
    def devolver_livro(self, titulo):
        for livro in self.livros_emprestados:
            if livro['titulo'] == titulo:
                self.livros.append(livro)
                self.livros_emprestados.remove(livro)
                print(f"Livro '{titulo}' devolvido com sucesso!")
                return
        print(f"Livro '{titulo}' não está emprestado.")

#RODANDO MENU APÓS CADA OPÇÃO ESCOLHIDA
def menu():
    biblioteca = Biblioteca()

    while True:
        print("\n1. Cadastrar Livro")
        print("2. Consultar Livros Disponíveis")
        print("3. Empréstimo de Livro")
        print("4. Devolução de Livro")
        print("5. Listar Livros Cadastrados")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")

#ESTRUTURA PARA CADASTRAR, CONSULTAR, EMPRESTAR, DEVOLVER, LISTAR LIVROS CADASTRADOS E SAIR DO SISTEMA.
        if escolha == '1':
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = input("Ano de Publicação: ")
            biblioteca.cadastrar_livro(titulo, autor, ano)
        elif escolha == '2':
            biblioteca.consultar_livros()
        elif escolha == '3':
            titulo = input("Título do livro para empréstimo: ")
            biblioteca.emprestar_livro(titulo)
        elif escolha == '4':
            titulo = input("Título do livro para devolução: ")
            biblioteca.devolver_livro(titulo)
        elif escolha == '5':
            biblioteca.listar_livros_cadastrados()
        elif escolha == '6':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
