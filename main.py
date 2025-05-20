# Referencias a bibliotecas, archivos e frameworks


# (Opcional) Classe

# Definition = def - ações do programa

def main():
    print("############ MENU PRINCIPAL ############")
    print("1 - Soma de dois números")
    opcao = input("Digite o número da opção desejada: ")   
    if opcao == "1":
        num1 = int(input("Digite o valor do 1o número: "))
        num2 = int(input("Digite o valor do 2o número: "))
        # # jeito mais antigo
        # soma = num1 + num2
        # print("Soma =",soma)
        
        # jeito mais atual
        print(f"Soma = {num1 + num2}")

if __name__ == "__main__":
    main()