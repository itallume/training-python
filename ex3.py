n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 > n2 and n1 > n3:
    print(n1, "É o meior número.")
else:
    if n2 > n1 and n2 > n3:
        print(n2, 'é o maior número.')
    else: 
        print(n3, "é o maior número.")