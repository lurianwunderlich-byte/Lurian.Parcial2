# Programa de calculadora simples

# Pedindo ao usuário dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Mostrando as opções de operação
print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

# Recebendo a escolha do usuário
opcao = input("Digite o número da operação: ")

# Verificando qual operação foi escolhida
if opcao == "1":
    resultado = num1 + num2
    print("Resultado:", resultado)

elif opcao == "2":
    resultado = num1 - num2
    print("Resultado:", resultado)

elif opcao == "3":
    resultado = num1 * num2
    print("Resultado:", resultado)

elif opcao == "4":
    # Verificando se o segundo número não é zero
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado:", resultado)
    else:
        print("Erro: divisão por zero não é permitida.")

else:
    print("Opção inválida!")
