# Programa para converter segundos em horas, minutos e segundos

# Pedindo ao usuário o tempo em segundos
segundos = int(input("Digite o tempo em segundos: "))

# Calculando as horas (1 hora = 3600 segundos)
horas = segundos // 3600

# Pegando o restante dos segundos após tirar as horas
resto = segundos % 3600

# Calculando os minutos (1 minuto = 60 segundos)
minutos = resto // 60

# Pegando o restante dos segundos após tirar os minutos
segundos_restantes = resto % 60

# Exibindo o resultado
print("Tempo convertido:")
print(horas, "hora(s),", minutos, "minuto(s) e", segundos_restantes, "segundo(s)")
