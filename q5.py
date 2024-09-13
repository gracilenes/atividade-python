"""
Suponha que um caixa eletrônico disponha apenas de notas de 1, 10 e 50 reais. Considerando que o cliente está querendo fazer um saque de um valor qualquer 
(considere esse valor inteiro). Faça um algoritmo que mostre o número mínimo de notas que o caixa deve fornecer para o cliente. 
Mostre também, o valor do saque, e a quantidade de cada nota a ser entregue. 
Obs: O caixa não trabalha com moedas
"""

notas = [50, 10, 1]
quantidade_notas = [0, 0, 0]

valor_saque = int(input("Digite o valor do saque:"))
valor_total, notas_50, notas_10, notas_1 = saque(valor_saque)

print("Valor do saque:", valor_total)
print("Notas de 50 reais:", notas_50)
print("Notas de 10 reais:", notas_10)
print("Notas de 1 real:", notas_1)


