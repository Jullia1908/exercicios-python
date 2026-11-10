cen = float (input ("Me dê um valor em centavos: "))
vinte, um = divmod(cen, 25)
print ("São necessárias {} moedas de 25 centavos e {} de um centavo".format (vinte, um))
