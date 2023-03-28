nome = input("Informe seu nome: ")
numeroCarros = float(input("Quantos carros você vendeu esse mês? "))
totalVendas = float(input('Qual o valor total de suas vendas? '))
salario = 1000
numeroCarros = numeroCarros * 200
totalVendas = (totalVendas * 5) / 100
salario += numeroCarros + totalVendas

print(f'{nome}, seu salário total ficou no valor de R${salario}.')
print()
print("################################################")
print()
print(f"Detalhamento do valor: \n Salário base: R$1000,00 \n Comisão total: R${numeroCarros} \n Bonificação de 5%: {totalVendas} \n Total: {salario}")