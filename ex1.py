# 1. Escrever um algoritmo que leia um valor inteiro e mostre na tela se é par ou impar.
print("Descubra agora se o número é par ou ímpar")
num = float(input("Informe um número: "))
resto = num % 2

if resto == 0:
    print(f"O número {num} é um PAR.")
else:
    print(f"O número {num} é ÍMPAR")
