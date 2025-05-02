def calcular_z():
    x = float(input("Digite o valor individual: "))
    media = float(input("Digite a média: "))
    desvio_padrao = float(input("Digite o desvio: "))
    
    z_score = (x - media) / desvio_padrao

    print(f"z-score de {x} é {z_score}")

