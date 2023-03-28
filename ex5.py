segundosEntrada = int(input("Digite um valor em segundos: "))

horas = segundosEntrada // 3600
resto = segundosEntrada % 3600
minutos = resto // 60
resto = resto % 60
segundos = resto

print(f'{horas} horas, {minutos} minutos e {segundos} segundos')