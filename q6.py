"Construa um pseudocódigo que informe se o aluno foi aprovado, reprovado ou fará uma nova avaliação (recuperação) em uma determinada disciplina, sabendo que:
A média é calculada com a leitura de 3 notas, O aluno será reprovado se a média for menor que 50, O aluno será aprovado se a média for maior ou igual a 70, 
O aluno fará uma nova avaliação (recuperação) caso sua média seja 50 (inclusive) ou menor que 70.""

def verificar_situacao(nota1, nota2, nota3):
  """Verifica a situação de um aluno com base em três notas.

  Args:
    nota1: A primeira nota.
    nota2: A segunda nota.
    nota3: A terceira nota.
  """

  media = (nota1 + nota2 + nota3) / 3

  if media < 50:
    print("Reprovado")
  elif media >= 70:
    print("Aprovado")
  else:
    print("Recuperação")

# Exemplo de uso:
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota:"))

verificar_situacao(nota1, nota2, nota3)