while True:
    n1=input("\nIngrese un número entero: ")
    verificar_n1=n1.lstrip('+-.').isnumeric()
    if not verificar_n1:
        print("\nIngrese una respuesta válida")
        continue
    else:
        n1=float(n1)
        break
while True:
    n2=input("\nIngrese un número entero: ")
    verificar_n2= n2.lstrip('+-').isnumeric()
    if not verificar_n2:
        print("\nIngrese una respuesta válida")
        continue
    else:
        n2=int(n2)
        break
while True:
    n3=input("\nIngrese un número entero: ")
    verificar_n3= n3.lstrip('+-').isnumeric()
    if not verificar_n3:
        print("\nIngrese una respuesta válida")
        continue
    else:
        n3=int(n3)
        break

if n1>0 and n2>0 and n3>0:
    print("\nLos tres números son positivos")
elif n1<0 or n2<0 or n3<0:
    print("\nPor lo menos uno de los número ingresados es negativo")
    if (n1==0 and n2!=0 and n3!=0) or (n2==0 and n1==0 and n3!=0) or (n3==0 and n1!=0 and n2!=0):
        print("\nExactamente un número de los ingresados es igual a cero")
elif (n1==0 and n2!=0 and n3!=0) or (n2==0 and n1==0 and n3!=0) or (n3==0 and n1!=0 and n2!=0):
    print("\nExactamente un número de los ingresados es igual a cero")
else:
    print("\nNo se cumplen ninguna de las condiciones requeridas para imprimir")