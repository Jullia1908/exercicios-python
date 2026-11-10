def soma_digitos(numero):
    soma = 0
    for digito in str(numero):
        soma += int(digito)
    return soma

numero = int(input("Digite um número: "))
resultado = soma_digitos(numero)
print(f"A soma dos dígitos de {numero} é {resultado}")
