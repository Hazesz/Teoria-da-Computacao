from functools import reduce

# Lista de pessoas com seus respectivos salários (nome, salário)
pessoas = [
    ("Galisteu", 2500),
    ("Chico-Moedas", 3500),
    ("Pitucho", 4000),
    ("Marquinho-do-Bocha", 1500),
    ("Carlinhos-Manda-Braza", 2800)
]

#Map: Aumentar o salario de cada pessoa em 10%
salarios_aumentados = list(map(lambda pessoa: (pessoa[0], pessoa[1] * 1.1), pessoas))

#Filter: Filtrar pessoas com salario superior a R$ 3000
pessoas_com_salario_alto = list(filter(lambda pessoa: pessoa[1] > 3000, salarios_aumentados))

#Reduce: Calcular o salario total das pessoas com salario superior a R$ 3000
salario_total = reduce(lambda total, pessoa: total + pessoa[1], pessoas_com_salario_alto, 0)


print("Pessoas com salarios aumentados:", salarios_aumentados)
print("Pessoas com salario superior a R$ 3000:", pessoas_com_salario_alto)
print("Salário total das pessoas com salario superior a R$ 3000: R$", salario_total)