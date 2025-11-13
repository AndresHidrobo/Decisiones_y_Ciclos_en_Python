while True:
    try:
        age = int(input("\nIngrese su edad: "))
        if 100 < age or age<18:
            print("\nIngrese una edad válida")
        else:
            break
    except ValueError:
        print("\nIngrese un valor válido")
while True:
    try:
        license=int(input("\nDigite la opción, posee licencia de conducir vigente (1.si | 2.no):"))
        if license==1:
            permiso=True
            break
        elif license==2:
            permiso=False
            break
        else:
            print("\nIngrese una opción válida")
    except ValueError:
        print("\nIngrese un valor válido")
while True:
    try:
        option=int(input("\n¿Posee vehículo propio? (1.si | 2.no): "))
        if option==1:
            car=True
            break
        elif option==2:
            while True:
                try:
                    option_2 = int(input("\n¿Tiene algún vehículo que se le autorizó su prestamo? (1.si | 2.no): "))
                    if option_2==1:
                        car=True
                        break
                    elif option_2==2:
                        car=False
                        break
                    else:
                        print("\nIngrese una opción válida")
                except ValueError:
                    print("\nIngrese un valor válido")
            break
        else:
            print("\nIngrese una opción válida")
    except ValueError:
        print("\nIngrese un valor válido")
if age>=18 and permiso==True and car==True:
    print("\nUsted es apto para participar en la competencia")
else:
    print("\nUsted no es apto para participar en la competencia")   