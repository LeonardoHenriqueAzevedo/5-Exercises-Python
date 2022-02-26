# 1. Escrever um algoritmo que leia um valor inteiro e mostre na tela se é par ou impar.
print("Descubra agora se o número é par ou ímpar")
num = float(input("Informe um número: "))
resto = num % 2

if resto == 0:
    print("O número {} é um PAR.".format(num))
else:
    print("O número {} é ÍMPAR".format(num))
