

#este programa muestra por pantalla todos los números impares desde 1 hasta ese número separados por comas.
n = int(input("Introduce un número entero positivo: "))
for i in range(1, n+1, 2):
    print(i, end=", ")
