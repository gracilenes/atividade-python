"""
Construir um algoritmo para calcular as raízes de uma equação do 2 grau, sendo que os valores a,b e c são fornecidos pelo usuário. 
Entrada: obter os valores de a,b e c do usuário. Consideremos somente a obtenção de raízes reais.

2x² + 5x - 10 = 0
ax² + bx - c = 0
raizes = (-b +- sqrt(b² - 4ac)) / 2 a
"""
print("Considere uma equação de segunto grau no formato:")
print("ax² + bx - c = 0")
a = int(input("Digite o valor de 'a':"))
b = int(input("Digite o valor de 'b':"))
c = int(input("Digite o valor de 'c':"))
delta = b**2 - 4*a*c
raiz1 = (-b + delta**(1/2)) / (2 * a)
raiz2 = (-b - delta**(1/2)) / (2 * a)

print("As raizes são: ", raiz1, raiz2)

