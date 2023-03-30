tipo = input("a/g: ")
litros = float(input ('litros: '))

if tipo == "g" or tipo == "G" or tipo == "gasolina" or tipo == "Gasolina":
    if litros <= 20:
        print("deu errado")
    else: 
        print("sla")

elif tipo == "a" or "A" or "alcool" or "Alcool":
    if litros <= 20:
        print('Deu certo mlk')
else:
    print('wtf')
