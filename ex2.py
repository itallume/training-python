nota1 = float(input('Qual foi sua nota em matemática? '))
nota2 = float(input('Qual foi sua nota em português? '))
pn1 = 6
pn2 = 4
media = ((nota1 * pn1) + (nota2 * pn2)) / (pn1 + pn2)

print(f'A média ponderadas das notas é: {media}')