def has_duplicates(data):
    return len(data) != len(set(data))
list=[]
i=0
while True:
    name=input('\nIngrese su nombre (Digite "fin" para finalizar): ').lower()
    if not name or name.isspace():
        print("\nNo deje el espacio vacio")
    elif name =="fin":
        break
    else:
        list.append(name)
        i+=1
if has_duplicates(list):
    print(f"\nSe registraron {i} nombres")
    print("La lista contiene nombres duplicados.")
else:
    print(f"\nSe registraron {i} nombres")
    print("La lista no contiene nombres duplicados.")