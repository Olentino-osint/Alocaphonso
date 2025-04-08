def mostrar_menu():
    while True:
       
        print("Escolha uma opção:")
        print("1 - Opção 1")
        print("2 - Opção 2")
        print("3 - Opção 3")
        print("0 - Sair")

       
        try:
            opcao = int(input("Digite o número da opção: "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

       
        if opcao == 1:
            print("Você escolheu a Opção 1.")
            
        elif opcao == 2:
            print("Você escolheu a Opção 2.")
            
        elif opcao == 3:
            print("Você escolheu a Opção 3.")
            
        elif opcao == 0:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    mostrar_menu()
