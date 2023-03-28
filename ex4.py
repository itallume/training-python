odometroInicial = float(input("Quantos KM marcava o odometro incialmente? "))
odometroFinal = float(input("Quanto marca após a viagem? "))
kmAndados = odometroFinal - odometroInicial

gasolinaInicial = float(input("Quantos litro de gasolina tinha inicialmente? "))
gasolinaFinal = float(input("Quantos litro de gasolina tem após a viagem? "))
precoGasolina = float(input("Qual o preço atual do litro da gasolina? "))
gasolinaGasta = gasolinaInicial - gasolinaFinal
custoViagem = gasolinaGasta * precoGasolina

capacidadeTanque = float(input("Qual a capcidade maxima do tanque em litros? "))
KmPorLitro = kmAndados / gasolinaGasta
autonomia = KmPorLitro * capacidadeTanque

print()
print(f"A quilometragem rodada foi de {kmAndados}KM.")
print(f'Com um litro de gasolina, o carro anda {KmPorLitro}KM')
print(f'A autonomia do automovel é de {autonomia}')
print(f'A viagem custou R${custoViagem}')
