def exibirMenu():
    print("****CALCULADORA DE SENO****")
    print("1. Calcule o seno")
    print("2. Calcule o cateto")
    print("3. Calcule a hipotenusa")
    print("4. Sair")

    select = int(input("O que você quer calcular? "))
    return select

while True:
    select = exibirMenu()

    if select == 1:
        print("- Selecionando opção 1 -\n")
        cateto = float(input("Qual o valor do cateto? "))
        hipotenusa = float(input("Qual o valor da hipotenusa? "))
        seno = cateto / hipotenusa
        print(f"O valor de seno é: {seno}\n")

    elif select == 2:
        print("- Selecionando opção 2 -\n")
        seno = float(input("Qual o valor do seno? "))
        hipotenusa = float(input("Qual o valor da hipotenusa? "))
        cateto = (seno * hipotenusa)
        print(f"O valor do cateto é: {cateto}\n")

    elif select == 3:
        print("- Selecionando opção 3 -\n")
        cateto = float(input("Qual o valor do cateto? "))
        seno = float(input("Qual o valor do seno? "))
        hipotenusa = (cateto / seno)
        print(f"O valor da hipotenusa é: {hipotenusa}\n")

    elif select == 4:
        print("Finalizando programa...")
        break
    
    else: 
        print("Opção inválida. Por favor, tente novamente.\n")
