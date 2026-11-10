num = int ( input (" Digite um número"))
primo = num >= 2
metade = int (num/2)

while metade > 1 : 
    if num%metade == 0 :
        primo = False
    metade -=1

if  primo == True: 
    print ('Numero é primo')
else: 
 print (' Numero não é primo ')
