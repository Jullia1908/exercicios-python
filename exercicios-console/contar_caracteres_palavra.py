palavra = "programação"

contagem_caracteres = {}

for caractere in palavra:
    if caractere in contagem_caracteres:
        contagem_caracteres[caractere] += 1
    else:
        contagem_caracteres[caractere] = 1

print(contagem_caracteres)

