print("""
Tabla de montos:
si pago igual o mayor a: 1000000$ | monto mayor     
si pago igual o mayor a: 100000$  | monto medio
si pago menor a: 100000$          | monto menor""")
while True:
    cash=input("\nIngrese en cuanto salio el valor de su compra: ")

    if not cash.isnumeric():
        print("\nIngrese una respuesta válida")
        continue
    cash=float(cash)
    if cash<=0:
        print("\nIngrese un valor real")
    else:
        break

while True:
    membership=input("\nSeleccione su tipo de membresia #(1.Activa | 2.temporal | 3.ninguna): ")
    if not membership.isnumeric():
        print("\nIngrese una respuesta válida")
        continue
    membership=int(membership)
    if membership<1 or membership>3:
        print("\nIngrese una opción válida")
    elif membership==1 and cash>=1000000:
        print("\nUsted está clasificado como un cliente premium")
        break
    elif (membership==2 or membership==1) or cash>=100000:
        print("\nUsted está clasificado como un cliente frecuente")    
        break
    else:
        print("\nUsted está clasificado como un cliente regular")
        break
    
