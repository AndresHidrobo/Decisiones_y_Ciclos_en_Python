while True:
    age = input("\nIngrese su edad: ")
    if not age.isnumeric() or age.isspace():
        print("\nIngrese una respuesta válida")
        continue
    age=int(age)
    if 100 < age or age<18:
        print("\nIngrese una edad válida")
    else:
        break
while True:
        license=input("\nDigite la opción, posee licencia de conducir vigente (si/no): ").lower()
        if not license or license.isspace():
            print("\nIngrese una respuesta válida")
            continue
        if license=="si":
            permiso=True
            break
        elif license=="no":
            permiso=False
            break
        else:
            print("\nIngrese una opción válida")
while True:
        option=input("\n¿Posee vehículo propio? (si/no): ").lower()
        if not option or option.isspace():
            print("\nIngrese una respuesta válida")
            continue
        if option=="si":
            car=True
            break
        elif option=="no":
            while True:
                    option_2 =input("\n¿Tiene algún vehículo que se le autorizó su prestamo? (si/no): ").lower()
                    if not option_2 or option_2.isspace():
                        print("\nIngrese una respuesta válida")
                        continue
                    if option_2=="si":
                        car=True
                        break
                    elif option_2=="no":
                        car=False
                        break
                    else:
                        print("\nIngrese una opción válida")
            break
        else:
            print("\nIngrese una opción válida")
if age>=18 and permiso and car:
    print("\nUsted es apto para participar en la competencia")
else:
    print("\nUsted no es apto para participar en la competencia")   
