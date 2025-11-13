s=0
n=0
while True:
    edad=input("\nIngrese su edad (Ingrese 0 para terminar el registro): ")
    if edad.isspace() or not edad or not edad.isnumeric():
        print("\nIngrese una respuesta válida")
    else:
        edad=int(edad)
        if edad>0:
            while True:
                answer=input("\n¿Te gusta programar? (si/no): ").lower()
                if answer=="si":
                    s+=1
                    print("\nRegistro exitoso")
                    break
                elif answer=="no":
                    n+=1
                    print("\nRegistro exitoso")
                    break
                else:
                    print("\nIngrese una respuesta válida")
        elif edad==0:
            print("\nSe ha terminado el proceso")
            break
        else:
            print("\nIngrese un número válido")
print(f"\nLa cantidad de personas que le gustan la programacion fue de:{s} \ny el número de personas que no le gustan programas fue de: {n}")