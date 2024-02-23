# programa para verificar si un numero es positivo o negativo

# input
X = int(input("digite el numero: "))

# processing
if X > 0:
    RTA = "Positivo"
elif X == 0:
    RTA = "El numero es neutro"
else:
    RTA = "Negativo"

# output
print("el numero",X," es ",RTA)