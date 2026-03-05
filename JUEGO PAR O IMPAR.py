#"JUEGO ESCRIBE UN NÚMERO, Y YO ADIVINARÉ SI ES PAR O IMPAR"

print("Bienvenido! Escribe un número y yo adivinaré si es par o impar") 

intento = int(input("Introduce un numero: "))

if intento % 2 == 0:
    print ("ES UN NUMERO PAR")
else:
    print ("ES UN NUMERO IMPAR")

