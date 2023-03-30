salarioMin = 1302
vendas = int(input('Digite o valor total de vendas: '))
comi = vendas * 0.05
salarioF = salarioMin + comi
if comi > salarioMin:
    print('Seu salário é:', salarioF )
else:
    print('seu salário é:', salarioMin)