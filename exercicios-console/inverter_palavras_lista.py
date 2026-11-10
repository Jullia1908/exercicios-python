palavras = ["python","java","c++","ruby"]
palavra_inversa = []

for palavra in palavras:
    inversa = palavra[::-1]
    palavra_inversa.append(inversa)
print(palavra_inversa)
