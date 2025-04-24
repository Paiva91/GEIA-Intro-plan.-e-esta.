from collections import Counter

def moda():
  n = int(input("Qual o valor de N? "))

  if n <= 0:
    print("A quantidade deve ser positiva")
    return

  numeros = []

  for i in range(n):
    x = float(input("Digite o valor: "))
    numeros.append(x)


  contagem = Counter(numeros)
  max_freq = max(contagem.values())

  modas = [num for num, freq in contagem.items() if freq == max_freq]

  if max_freq == 1:
    print("Amodal- Não temos uma MODA!")
  elif len(modas) == 1:
    print(f"O conjunto é UNIMODAL. Moda: {modas[0]}")
  elif len(modas) == 2:
    print(f"O conunto é BIMODAL. Modas: {modas[0]} e {modas[1]}")

moda()
