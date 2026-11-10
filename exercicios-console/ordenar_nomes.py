nomes = ['', '','','']
i=0
while i<=3:
    nomes[i] = input ( ' Digite o nome' )
    i+=1

nomes_ordenados = sorted(nomes)

i=0
while i<=3:
    print(nomes_ordenados[i])
    i+=1
