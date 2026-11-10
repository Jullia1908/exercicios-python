velocidade = int (input("Indique a sua velocidade"))
multa = 80

if velocidade > 80:
    while velocidade > 80:
        velocidade = velocidade - 1
        multa += 5
    print("Você foi multado. O valor da multa é:",multa)
else:
    print("Está tudo certo!")
