# Referencias a bibliotecas, archivos e frameworks

import os
import time

# (Opcional) Classe

# Definition = def - ações do programa

def main():
    print("############ MENU PRINCIPAL ############")
    print("1 - Soma de dois números")
    print("2 - Subtração de dois números")
    print("3 - Multiplicação de dois números")
    print("4 - Divisão de dois números (if/else)")
    print("5 - Divisão de dois números (try/except)")
    print("6 - Contagem progressiva")
    print("7 - Contagem regressiva")

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
        case "5":
            dividir_dois_numeros_try_except()
        case "6":
            contagem_progressiva()
        case "7":
            contagem_regressiva()
        case _:
            print("Opção inválida, execute o programa novamente.")

# sintaxe camelCase comun en JAva, JavaScript e C#
# def somarDoisNumeros(num1, num2):

# sintaxa snake_case comum em Python
def somar_dois_numeros():
    try:
        num1 = float(input("Digite o valor do 1o número: "))
        num2 = float(input("Digite o valor do 2o número: "))
        print(f"Soma = {num1 + num2}")
    except ValueError:
        print("Erro: Digite apenas números e use '.' para separar decimais.")

def subtrair_dois_numeros():
    try:
        num1 = float(input("Digite o valor do 1o número: "))
        num2 = float(input("Digite o valor do 2o número: "))
        print(f"Subtração = {num1 - num2}")
    except ValueError:
        print("Erro: Digite apenas números e use '.' para separar decimais.")

def multiplicar_dois_numeros():
    try:
        num1 = float(input("Digite o valor do 1o número: "))
        num2 = float(input("Digite o valor do 2o número: "))
        print(f"Multiplicação = {num1 * num2}")
    except ValueError:
        print("Erro: Digite apenas números e use '.' para separar decimais.")

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
    except ValueError:
        print("Erro: Digite apenas números e use '.' para separar decimais.")
    finally:
        print("Operação finalizada.")

def contagem_progressiva():
    try:
        num = int(input("Contar até o número: "))
        for i in range(num + 1):
            print(i, end=' ')
            print()    # imprime uma nova linha

    except ValueError:
        print("Erro: Digite apenas números e sem parte decimal")

def contagem_regressiva():
    try:
        num = int(input("Contar a partir do número: "))
        for i in range(num, 0, -1):
            # To Do: Limpar linha via system
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela 
            print(i, end=' ')
        # print()    # imprime uma nova linha
            time.sleep(1) # espera 1 segundo

    except ValueError:
        print("Erro: Digite apenas números e sem parte decimal")
    

if __name__ == "__main__":
    main()