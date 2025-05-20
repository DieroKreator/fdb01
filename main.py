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
            somar_dois_numeros()
        case "2":
            subtrair_dois_numeros()
        case "3":
            multiplicar_dois_numeros()
        case "4":
            dividir_dois_numeros_if_else()
        case _:
            print("Opção inválida, execute o programa novamente.")

# sintaxe camelCase comun en JAva, JavaScript e C#
# def somarDoisNumeros(num1, num2):

# sintaxa snake_case comum em Python
def somar_dois_numeros():
    num1 = float(input("Digite o valor do 1o número: "))
    num2 = float(input("Digite o valor do 2o número: "))
    print(f"Soma = {num1 + num2}")

def subtrair_dois_numeros():
    num1 = float(input("Digite o valor do 1o número: "))
    num2 = float(input("Digite o valor do 2o número: "))
    print(f"Subtração = {num1 - num2}")

def multiplicar_dois_numeros():
    num1 = float(input("Digite o valor do 1o número: "))
    num2 = float(input("Digite o valor do 2o número: "))
    print(f"Multiplicação = {num1 * num2}")

def dividir_dois_numeros_if_else():
    num1 = float(input("Digite o valor do 1o número: "))
    num2 = float(input("Digite o valor do 2o número: "))
    if num2 == 0:
        print("Divisão por zero não é permitida.")
    else:
        print(f"Divisão = {num1 / num2}")

def dividir_dois_numeros_try_except():
    try:
        num1 = float(input("Digite o valor do 1o número: "))
        num2 = float(input("Digite o valor do 2o número: "))
        print(f"Divisão = {num1 / num2}")
    except ZeroDivisionError:
        print("Divisão por zero não é permitida.")

if __name__ == "__main__":
    main()