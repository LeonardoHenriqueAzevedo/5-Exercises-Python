# 2. Escreva um algoritmo que leia três valores inteiros e mostre em ordem decrescente.
print("Ordem Decrescente dos números")
lista = []
for n in range(3):
    num = int(input("Informe um número: "))
    lista.append(num)

lista.sort(reverse=True)
print(lista)
