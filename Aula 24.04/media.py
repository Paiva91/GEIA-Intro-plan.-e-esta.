valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(valores)
i = 0
soma = 0
while i < n:
    soma += valores[i]
    i += 1
print(soma/n)

numeros = input("Digite os números separados por espaço: ").split()
numeros = [float(n) for n in numeros]
media = sum(numeros) / len(numeros)
print(f"Média: {media:.2f}")

def media_aritmetica():
    n = int(input("Qual o valor de N? "))

    if n <= 0:
        print("A quantidade deve ser positiva")
        return

    acc = 0

    for i in range(n):
        x1 = float(input("Digite o valor: "))
        acc = x1 + acc

    x_linha = acc / n
    print("A média é", x_linha)

media_aritmetica()