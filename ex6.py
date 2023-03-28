valorEntrada = int(input("Quantos Bits deseja sacar? "))
notaDe50 = valorEntrada // 50
attValor = valorEntrada % 50 

notaDe10 = attValor // 10
attValor1 = attValor % 10

notaDe5 = attValor1 // 5
attValor2 = attValor1 % 5

notaDe1 = attValor2 // 1

print(f"Para o Valor B${valorEntrada} você receberá: ")
print(f'{notaDe50} notas de B$50,00 ')
print(f'{notaDe10} notas de B$10,00 ')
print(f'{notaDe5} notas de B$5,00 ')
print(f'{notaDe1} notas de B$1,00 ')