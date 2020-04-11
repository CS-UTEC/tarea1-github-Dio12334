import math

numero = int(input())

raiz = int(math.sqrt(numero))

prim = False

cont = 2

while cont <= raiz:

    if numero % cont == 0:
        print("No es primo")

        prim = True

        break

    cont += 1
    
if prim == False:

    print("Es primo")
