numeros = [1, 2, 2, 3, 4, 4, 5]
retirado = []

print("Lista inicial:",numeros)

for numero in numeros:
    if numero in retirado:
        print("O número {} é duplicado.".format(numero))
    else:
        retirado.append(numero)
print ("Nova lista sem duplicados:",retirado)


