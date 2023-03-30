from ctypes.wintypes import PINT


n1 = int(input("digite um numero: "))
n2 = int(input("Digite o segundo numero: "))
if n1 > n2:
    print(f"Os numeros na ordem crescente é: {n2}; {n1}")
else:
    if n2 > n1:
        print(f"Os numeros na ordem crescente é: {n1}; {n2}")
    else:
        print("Não existe um ordem definida, pois os numeros são iguais.")