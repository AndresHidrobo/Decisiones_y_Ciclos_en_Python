user="Pepe"
passw="Riwi13579"
left=False
i=0
for i in range(0,3):
    sign=input("\nIngrese su usuario: ")
    clave=input("\nIngrese su contraseña: ")
    if not sign or sign.isspace() or not clave or clave.isspace():
        print("\nNo deje ningún espacio vacio")
        i=i-1
    elif sign==user and clave==passw:
        print("\nIniciós sesión con éxito")
        left=True
        break
    else:
        print("\nEl usuario o la contraseña son incorrectos, intente de nuevo")
if left==False:
    print("\nSe terminaron los intentos disponibles, intentelo más tarde")