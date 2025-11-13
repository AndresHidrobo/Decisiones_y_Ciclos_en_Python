while True:
    try:
        age = input("\nIngrese su edad: ")
        if not age.isnumeric():
            print("\nIngrese una respuesta válida")
            continue
        if 100 < age or age<0:
            print("\nIngrese una edad válida")
        else:
            break
    except ValueError:
        print("\nIngrese un valor válido\n")
while True:
    oficio=input("\nIngrese la opción de lo que se dedica (1.Nada/2.estudia/3.trabaja):")
    if not oficio.isnumeric():
        print("\nIngrese una valor válido")
        continue
    oficio=int(oficio)
    if 0<oficio<4:
        if oficio==1 and age<6:
            print("\nUsted es un infante")
        elif oficio==2 and 5<age<18:
            print("\nUsted es un Estudiante escolar")
        elif oficio==2 and 17<age<26:
            print("\nUsted es un Estudiante universitario")
        elif oficio==3 and 25<age<60:
            print("\nUsted es un adulto activo")
        elif oficio==1 and age>=60:
            print("\nUsted es un adulto mayor jubilado")
        else:
            print("\nUsted es un NO DETERMINADO")
        break
    else:
        print("\nIngrese una opción válida")
