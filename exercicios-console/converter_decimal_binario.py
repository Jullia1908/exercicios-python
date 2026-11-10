while True:
    try:
        numero_decimal = int(input("Digite um número decimal: "))
        break  # Sai do loop se a conversão for bem-sucedida
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

# Converte o número decimal para binário
numero_binario = bin(numero_decimal)[2:]

# Exibe o resultado
print(f"O número decimal {numero_decimal} em binário é {numero_binario}")
