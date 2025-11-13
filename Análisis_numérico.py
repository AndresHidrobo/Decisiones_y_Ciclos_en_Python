n1=int(input("\nIngrese un número: "))
n2=int(input("\nIngrese otro número: "))
n3=int(input("\nIngrese un último número: "))
while True:
    n1=int(input("\nIngrese un número: "))
    if n1.isspace() or not n1:
        print("\nIngrese una respuesta válida")
        continue
    else:
        break
while True:
    n2=int(input("\nIngrese un número: "))
    if n2.isspace() or not n2:
        print("\nIngrese una respuesta válida")
        continue
    else:
        break
while True:
    n3=int(input("\nIngrese un número: "))
    if n3.isspace() or not n3:
        print("\nIngrese una respuesta válida")
        continue
    else:
        break

if n1>0 and n2>0 and n3>0:
    print("Los tres números son positivos")
elif n1<0 or n2<0 or n3<0:
    print("Por lo menos uno de los número ingresados es negativo")
elif (n1==0 and n2!=0 and n3!=0) or (n2==0 and n1==0 and n3!=0) or (n3==0 and n1!=0 and n2!=0):
    print("Exactamente un número de los ingresados es igual a cero")
