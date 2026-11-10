palavras = ["python","c","java","javascript","go"]
numero_letras = []

for palavra in palavras:
    numero = len(palavra)
    if numero < 5:
        numero_letras.append(palavra)
print (numero_letras)
