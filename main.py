# Referencias a bibliotecas, archivos e frameworks

from datetime import datetime
import math
import time
import os

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
    print("8 - Consultar data e hora")
    print("9 - Calcular área do quadrado")
    print("10 - Calcular área do retângulo")
    print("11 - Calcular área do triângulo")
    print("12 - Calcular área do círculo")
    print("13 - Consultar data")
    print("14 - Consultar hora militar")
    print("15 - Consultar hora")
    print("16 - Sobre datas")

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
        case "8":
            consultar_data_hora() 
        case "9":
            calcular_area_do_quadrado()
        case "10":
            calcular_area_do_retangulo()
        case "11":
            calcular_area_do_triangulo()
        case "12":
            calcular_area_do_circulo()
        case "13":
            consultar_data()
        case "14":
            consultar_hora_militar()
        case "15":
            consultar_hora()
        case "16":
            sobre_datas()
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
        for i in range(num, -1, -1):
            # To Do: Limpar linha via system
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela 
            print(i, end=' ')
            # print()
        # print()    # imprime uma nova linha
            time.sleep(1) # espera 1 segundo

    except ValueError:
        print("Erro: Digite apenas números e sem parte decimal")

def consultar_data_hora():
    agora = datetime.datetime.now()
    print(f"Data e hora atual: {agora.strftime('%d/%m/%Y, %H:%M:%S')}")

def calcular_area_do_quadrado():
    try:
        lado = float(input("Digite o comprimento do lado do quadrado: "))
        print(f"Área do quadrado = {lado ** 2}")
    except ValueError:
        print("Erro: Digite apenas números e use '.' para separar decimais.")

def calcular_area_do_retangulo():
    try:
        base = float(input("Digite o comprimento da base do retângulo: "))
        altura = float(input("Digite o comprimento da altura do retângulo: "))
        print(f"Área do retângulo = {base * altura}")
    except ValueError:
        print("Erro: Digite apenas números e use '.' para separar decimais.")

def calcular_area_do_triangulo():
    try:
        base = float(input("Digite o comprimento da base do triângulo: "))
        altura = float(input("Digite o comprimento da altura do triângulo: "))
        print(f"Área do triângulo = {0.5 * base * altura}")
    except ValueError:
        print("Erro: Digite apenas números e use '.' para separar decimais.")

def calcular_area_do_circulo():
    try:
        raio = float(input("Digite o comprimento do raio do círculo: "))
        area = math.pi * (raio ** 2)
        print(f"Área do círculo = {area:.2f}")
    except ValueError:
        print("Erro: Digite apenas números e use '.' para separar decimais.") 

def consultar_data():
    agora = datetime.now()
    print(f"Data atual: {agora.strftime('%d de %B de %Y')}")

def consultar_hora_militar():
    agora = datetime.now()
    print(f"Hora atual: {agora.strftime('%H:%M')}")

def consultar_hora():
    agora = datetime.now()
    print(f"Hora atual: {agora.strftime('%I:%M %p')}")  # Formato 12 horas

def sobre_datas():
    sua_data = input('Digite uma data no formato dd/mm/aaaa: ')
    sua_data_convertida = datetime.strptime(sua_data, "%d/%m/%Y")
    agora = datetime.now()

    if int(sua_data_convertida.strftime("%Y")) == int(agora.strftime("%Y")):
        print(f"Data digitada: {sua_data_convertida.strftime('%d/%m/%Y')} é o {sua_data_convertida.strftime('%j')} dia do ano")
        print(f"Data atual: {agora.strftime('%d/%m/%Y')} é o {agora.strftime('%j')} dia do ano")

        if int(sua_data_convertida.strftime("%j")) < int(agora.strftime("%j")):
            print("A data digitada está no passado.")
            dias_transcorridos = int(agora.strftime("%j")) - int(sua_data_convertida.strftime("%j"))
            print(f'Já se passaram {dias_transcorridos} dias desde a data digitada')
        else:
            print("A data digitada está no futuro")
            dias_faltando = int(sua_data_convertida.strftime("%j")) - int(agora.strftime("%j"))
            print(f'Faltam {dias_faltando} dias para a data digitada')
    else:
        print("Tente novamente, utilize uma data do ano atual.")

if __name__ == "__main__":
    main()