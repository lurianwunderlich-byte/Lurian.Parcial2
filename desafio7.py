# Programa para calcular juros simples

# Pedindo ao usuário o valor do capital inicial
capital = float(input("Digite o capital (valor inicial): "))

# Pedindo a taxa de juros (em porcentagem)
taxa = float(input("Digite a taxa de juros (%): "))

# Pedindo o tempo (em meses, anos, etc.)
tempo = float(input("Digite o tempo: "))

# Convertendo a taxa de porcentagem para decimal
taxa_decimal = taxa / 100

# Calculando o juros simples (J = C * i * t)
juros = capital * taxa_decimal * tempo

# Calculando o montante final (M = C + J)
montante = capital + juros

# Exibindo os resultados
print("Juros:", juros)
print("Montante final:", montante)
