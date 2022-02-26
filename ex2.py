# 2. Escreva um algoritmo que leia três valores inteiros e mostre em ordem decrescente.
print("Ordem Decrescente dos números")
n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
n3 = int(input("Informe o terceiro número: "))

if n1 < n2:
    if n2 < n3:
        maior = n3
    else:
        maior = n2
else:
    if n1 < n3:
        menor = n1
        mediano = n3
    else:
        mediano = n1
        menor = n3

print("Ordem Decrescente: {}, {}, {}".format(maior, mediano, menor))
