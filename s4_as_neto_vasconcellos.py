"""
Nome:  Neto Vasconcellos
Curso: Raciocínio Computacional (11100010563_20251_20)
"""

def main():
    """
    Exibe o menu e para direcionar as operações.
    """
    estudantes = []
    while True:
        print("\n=== Menu Principal ===")
        print("1 - Estudantes")
        print("2 - Professores")
        print("3 - Disciplinas")
        print("4 - Turmas")
        print("5 - Matrículas")
        print("0 - Sair")
        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            menu_estudantes(estudantes)
        elif opcao in ["2", "3", "4", "5"]:
            # Funcionalidades ainda em desenvolvimento
            print("\n Ainda em desenvolvimento, tente outra hora.")
        elif opcao == "0":
            print("\n Obrigado por usar nosso sistema.Até logo!")
            break
        else:
            print("\n Opção inválida, caso deseje, tente novamente.")

def menu_estudantes(estudantes):
    """
    Sub-menu para operações relacionadas a estudantes:
    incluir, listar, atualizar e excluir (estas duas últimas em desenvolvimento).
    """
    while True:
        print("\n--- Menu Estudantes ---")
        print("1 - Acresentar estudante")
        print("2 - Listar estudantes")
        print("3 - Atualizar estudante")
        print("4 - Excluir estudante")
        print("0 - Voltar ao menu principal")
        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            # Para incluir um novo estudante na lista
            nome = input("Nome do estudante: ").strip()
            if nome:
                estudantes.append(nome)
                print(f"Estudante '{nome}' incluído com sucesso.")
            else:
                print("Nome vazio. Nenhum estudante foi incluído.")
        elif opcao == "2":
            # Listar todos os estudantes cadastrados
            if not estudantes:
                print("Não há estudantes cadastrados.")
            else:
                print("\nLista de estudantes cadastrados:")
                for i, nome in enumerate(estudantes, start=1):
                    print(f"{i}. {nome}")
        elif opcao in ["3", "4"]:
            # Atualização e exclusão ainda não implementadas
            print("\nAinda em desenvolvimento, tente outra hora.")
        elif opcao == "0":
            # Retorna ao menu principal
            break
        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
