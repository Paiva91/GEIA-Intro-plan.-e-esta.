def mediana():
    n = int(input("Qual o valor de N? "))

    if n <= 0:
        print("A quantidade deve ser positiva")
        return

    numeros = []

    for i in range(n):
        x = float(input("Digite o valor: "))
        numeros.append(x)


    numeros.sort()

    if n % 2 == 1:
        mediana_impares = numeros[n // 2]
        print("A mediana é: ", mediana_impares)
    else:
        mediana_pares = (numeros[n // 2 - 1] + numeros[n // 2]) / 2
        print("A mediana é: ", mediana_pares)

mediana()