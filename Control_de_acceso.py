ban=["antony","pussydestroyer"]
name=input("\nIngrese su nombre de usuario: ").lower()
while True:
    if name.isspace() or not name:
        print("\nIngrese una respuesta válida")
        continue
    elif name in ban:
        print("\nAcceso denegado: Usted está en la lista restringida")
        break
    else:
        code=input("\nIngrese su código numérico: ")
        if not code.isnumeric() or code.isspace() or not code:
            print("\nIngrese una respuesta válida")
            continue
        else:
            last_char=int(code[-1])
            code=int(code)
            if code % 2 == 0 or last_char==7:
                print("\nAcceso concedido")
                break
            else:
                print("\nAcceso denegado: Código no cumple con los requisitos")
                break

