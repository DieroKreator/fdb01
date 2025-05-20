# Referencias a bibliotecas, archivos e frameworks


# (Opcional) Classe

# Definition = def - ações do programa

def main():
    print("############ MENU PRINCIPAL ############")
    print("1 - Soma de dois números")
    print("2 - Subtração de dois números")

    opcao = input("Digite o número da opção desejada: ")   

    # # Antes do Python versão 3.10
    # if opcao == "1":
    #     num1 = int(input("Digite o valor do 1o número: "))
    #     num2 = int(input("Digite o valor do 2o número: "))
    #     # # jeito mais antigo
    #     # soma = num1 + num2
    #     # print("Soma =",soma)

    #     # jeito mais atual
    #     print(f"Soma = {num1 + num2}")
    # elif opcao == "2":
    #     num1 = int(input("Digite o valor do 1o número: "))
    #     num2 = int(input("Digite o valor do 2o número: "))

    #     print(f"Subtração = {num1 - num2}")
    # else:
    #     print("Opção inválida, execute o programa novamente.")

    match opcao:
        case "1":
            num1 = float(input("Digite o valor do 1o número: "))
            num2 = float(input("Digite o valor do 2o número: "))
            print(f"Soma = {num1 + num2}")
        case "2":
            num1 = float(input("Digite o valor do 1o número: "))
            num2 = float(input("Digite o valor do 2o número: "))
            print(f"Subtração = {num1 - num2}")
        case _:
            print("Opção inválida, execute o programa novamente.")

if __name__ == "__main__":
    main()