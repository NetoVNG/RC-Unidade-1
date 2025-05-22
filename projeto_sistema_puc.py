"""
Nome: Neto Vasconcellos
Curso: Raciocínio Computacional (11100010563_20251_20)
Disciplina: Raciocínio Computacional
Sistema de Navegação CRUD — Stubs
"""

def main():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Estudantes")
        print("2 - Professores")
        print("3 - Disciplinas")
        print("4 - Turmas")
        print("5 - Matrículas")
        print("0 - Sair")
        opcao = input("Selecione uma opção: ").strip()
        
        if opcao == "1":
            menu_entidade("Estudantes")
        elif opcao == "2":
            menu_entidade("Professores")
        elif opcao == "3":
            menu_entidade("Disciplinas")
        elif opcao == "4":
            menu_entidade("Turmas")
        elif opcao == "5":
            menu_entidade("Matrículas")
        elif opcao == "0":
            print("👋 Saindo do sistema. Até mais!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

def menu_entidade(nome_entidade):
    """
    Exibe o sub-menu CRUD para a entidade passada:
    Incluir, Listar, Atualizar, Excluir, Voltar
    """
    while True:
        print(f"\n--- MENU {nome_entidade.upper()} ---")
        print("1 - Incluir")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Excluir")
        print("0 - Voltar")
        opcao = input("Selecione uma opção: ").strip()
        
        if opcao == "1":
            print(f"🔄 {nome_entidade}: Incluir — Em desenvolvimento.")
        elif opcao == "2":
            print(f"🔄 {nome_entidade}: Listar — Em desenvolvimento.")
        elif opcao == "3":
            print(f"🔄 {nome_entidade}: Atualizar — Em desenvolvimento.")
        elif opcao == "4":
            print(f"🔄 {nome_entidade}: Excluir — Em desenvolvimento.")
        elif opcao == "0":
            print(f"↩️ Retornando ao menu principal...")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
