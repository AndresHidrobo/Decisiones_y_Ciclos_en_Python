luces=False
calefaccion=False
Estado_luces=""
Estado_calefaccion=""
while True:
    temperatura=input("\nIngrese a cuantos grados celcius está ahora:")
    verificar_temperatura=temperatura.lstrip('+-').isnumeric()
    if not verificar_temperatura:
        print("\nIngrese una respuesta válida")
        continue
    else:
        temperatura=int(temperatura)
        print("\nSe registro exitosamente")
        break
while True:
    time=input("\nIngrese en que momento del día es (Mañana / Tarde / Noche):").lower()
    if not time or time.isspace():
        print("\nIngrese una respuesta válida")
        continue
    else:
        if time=="mañana":
            print("\nSe registro exitosamente")
            break
        elif time=="tarde":
            print("\nSe registro exitosamente")
            break
        elif time=="noche":
            print("\nSe registro exitosamente")
            break
        else:
            print("\nIngrese una opción válida")

while True:
    print(f"""\n
        ======================================      
            Panel de control doméstico
        ======================================
        1. Encender/Apagar luces
        2. Activar/Desactivar calefacción
        3. Ver estados
        4. Salir""")
    opcion=input("\nSeleccione la acción que desea realizar (#): ")
    if not opcion or opcion.isspace():
        print("\nIngrese una opción válida")
        continue

    if opcion=="1":
        if time=="noche":
            if not luces:
                while True:
                    confirmar_luces=input("\n¿Desea encender las luces? (si/no): ").lower()
                    if not confirmar_luces or confirmar_luces.isspace():
                        print("\nIngrese una opción válida")
                        continue
                    if confirmar_luces=="si":
                        luces=True
                        print("\nSe encendieron las luces")
                        break
                    elif confirmar_luces=="no":
                        print("\nNo se hizo ningún cambio")
                        break
                    else:
                        print("\nIngrese una respuesta válida")
            elif luces:
                while True:
                    confirmar_luces=input("\n¿Desea apagar las luces? (si/no): ").lower()
                    if not confirmar_luces or confirmar_luces.isspace():
                        print("\nIngrese una opción válida")
                        continue
                    if confirmar_luces=="si":
                        luces=False
                        calefaccion=False
                        print("\nSe apagaron las luces")
                        break
                    elif confirmar_luces=="no":
                        print("\nNo se hizo ningún cambio")
                        break
                    else:
                        print("\nIngrese una respuesta válida")
        else:
            print("\nNo es de noche, no se pueden encender las luces")
            continue

    #Funcionamiento de la opcion 2   
    elif opcion=="2":
            if not calefaccion:
                while True:
                        confirmar_calefaccion=input("\n¿Desea encender la calefacción? (si/no): ").lower()
                        if not confirmar_calefaccion or confirmar_calefaccion.isspace():
                            print("\nIngrese una opción válida")
                            continue
                        if confirmar_calefaccion=="si":
                            if luces==True and temperatura<18:
                                calefaccion=True
                                print("\nSe encendio la calefacción")
                                break
                            else:
                                print("\nNo se cumplen las condiciones para encender la calefacción")
                                break
                        elif confirmar_calefaccion=="no":
                            print("\nNo se hizo ningún cambio")
                            break
                        else:
                            print("\nIngrese una respuesta válida")
            else:
                while True:
                        confirmar_calefaccion=input("\n¿Desea apagar la calefacción? (si/no): ").lower()
                        if not confirmar_calefaccion or confirmar_calefaccion.isspace():
                            print("\nIngrese una opción válida")
                            continue
                        if confirmar_calefaccion=="si":
                            calefaccion=False
                            print("\nSe apago la calefacción")       
                            break
                        elif confirmar_calefaccion=="no":
                            print("\nNo se hizo ningún cambio")
                            break
                        else:
                            print("\nIngrese una respuesta válida")

    #Funcionamiento de la opción 3                            
    elif opcion=="3":
        if luces:
            Estado_luces="Encendidas"
        else:
            Estado_luces="Apagadas"
        if calefaccion:
            Estado_calefaccion="Encendido"
        else:
            Estado_calefaccion="Apagada"
        print(f"""\n 
            ======================================      
                Estados dentro de la casa
            ======================================
                Las luces están {Estado_luces}
              
                La calefacción está {Estado_calefaccion}""")
    elif opcion=="4":
        print("\nSe finalizó el proceso, adios")
        break
    else:
        print("\nIngrese una opción válida")