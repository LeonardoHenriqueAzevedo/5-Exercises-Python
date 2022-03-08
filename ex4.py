"""4. Faça um algoritmo que leia o ano de nascimento de uma
pessoa, calcule e mostre a sua idade e, também, verifique e
mostre se ela já tem idade para votar (16 anos ou mais) e para
conseguir a carteira de habilitação (18 anos ou mais)."""

ano_nasc = int(input("Informe o ano em que você nasceu: "))
idade = 2022 - ano_nasc
print(f"Você tem {idade} anos.")
if idade >= 16:
    print("Você possui idade para votar!")
    if idade >= 18:
        print("Você possui idade para conseguir a carteira de habilitação!")
else:
    print("Você não possui idade para votar e nem para tirar carteira de habilitação!")
