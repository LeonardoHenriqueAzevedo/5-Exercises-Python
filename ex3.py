""" 3. Tendo como dados de entrada a altura (h) e o sexo de uma pessoa, construa um algoritmo que calcule seu
“peso”(p) ideal, utilizando as seguintes fórmulas:
Homens: (72.7 * h) – 58
Mulher: (62.1 * h) – 44.7
"""
sexo = str(input("Informe seu sexo [M/F]: "))
altura = float(input("Informe sua altura em metros: "))

if sexo[0].capitalize() == "M":
    peso_ideal = (72.7 * altura) - 58
    print(
        f"O Peso Ideal para uma pessoa do sexo masculino com {altura} de altura deve ser {peso_ideal} kg.")
else:
    peso_ideal = (62.1 * altura) - 44.7
    print(
        f"O Peso Ideal para uma pessoa do sexo feminino com {altura} de altura deve ser {peso_ideal} kg.")
