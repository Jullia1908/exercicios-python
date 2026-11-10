
def contar_positivos():
    count = 0

    while True:
        numero = int(input("Digite um número (0 para parar): "))
        if numero == 0:
            break
        elif numero > 0:
            count += 1
    print (f"Números de valores positivos: {count}")

contar_positivos()




