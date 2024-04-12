#este programa almacena una cadena de caracteres (contraseña) en una variable
Clave = "contraseña"
password= input("Introduce la contraseña: ")
if Clave == password.lower():
    print("La contaseña coincide")
else:
    print("La contraseña no coincide")