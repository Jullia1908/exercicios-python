energiaG = int(input("Digite o valor de energia gerada esse mês: "))
energiaC = int(input("Digite o valor de energia consumida esse mês: "))
fioB = 0.10 * energiaC
taxaI = float(input("Digie o valor da Taxa de Iluminaçõa Pública: "))

saldoEnergia = energiaG - energiaC
print(saldoEnergia)

custosFixos = taxaI + fioB
print(custosFixos)

if saldoEnergia >= 0:
    print(f"Saldo Sustentável: {saldoEnergia} créditos gerados. Você deverá pagar apenas R${custosFixos:.2f} referente aos Custos Fixos.")

elif saldoEnergia < 0:
    print(f"Não houve acúmulo de créditos, o total de kWh a ser pago para a concessionária é de {abs(saldoEnergia)}, mais os Custos Fixos de R${custosFixos:.2f}")
