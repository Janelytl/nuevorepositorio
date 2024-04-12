#este programa divide 2 numeros y da error si el usuario introduce 0 o no digita un numero
dividendo= float(input("Introduce el dividendo: "))
divisor = float(input("Introduce el divisior: "))
if divisor == 0:
    print("¡Error! No se puede dividir por 0.")
else:
    print(dividendo/divisor)