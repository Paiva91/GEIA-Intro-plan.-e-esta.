def variancia():
    n = int(input("Qual o valor de N? "))

    if n <= 0:
        print("A quantidade deve ser positiva")
        return

    numeros = []

    for i in range(n):
        x = float(input("Digite o valor: "))
        numeros.append(x)


    numeros.sort()
    valor_maximo = max(numeros)
    valor_minimo = min(numeros)
    variancia = valor_maximo - valor_minimo
    print("A variancia e:", variancia)

variancia()

numeros = [1, 2, 3, 4, 5, 6, 7, 43, 54543, 3453534, 354, 45, 665464]
x_max = max(numeros)
x_min = min(numeros)
intervalo = x_max - x_min
print(intervalo)