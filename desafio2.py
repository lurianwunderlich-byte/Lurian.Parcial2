# Programa para verificar se um número é par ou ímpar

# Pedindo ao usuário para digitar um número
numero = int(input("Digite um número: "))

# Verificando se o número é par
# Um número é par quando o resto da divisão por 2 é igual a 0
if numero % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")
