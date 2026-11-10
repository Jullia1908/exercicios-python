lista = []
i = 0
while i < 5:
    palavras = str( input ("Digite uma palavra:"))
    lista.append(palavras)
    i += 1
    menor = min (lista, key=len)
print("a menor palavra é ",(menor))
