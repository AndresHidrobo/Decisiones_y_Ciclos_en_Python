def has_duplicates(data):
    return len(data) != len(set(data))
list=[]
while True:
    name=input('Ingrese su nombre (Digite "fin" para finalizar): ').lower()
    if not name or name.isspace():
        print("No deje el espacio vacio")
    elif name =="fin":
        break
    else:
        list.append(name)
if has_duplicates(list):
    print("La lista contiene nombres duplicados.")
else:
    print("La lista no contiene nombres duplicados.")