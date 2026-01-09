##
##Cajero automatico
##
saldoInicial = float(input("ingresa el monto inicial en soles: "))

while True:
    print("\n---Cajero automático---")
    print("1. consultar saldo")
    print("2. Depositar saldo")
    print("3. Retirar dinero")
    print("4. Salir")
    opcion = input("Selecciona una opción:")
    
    if opcion == "1":
        print(f"tu saldo actual es: ${saldoInicial}")
    elif opcion == "2":
        monto = float(input("Ingresa el monto a depositar. "))
        if monto > 0:
            saldoInicial += monto
            print(f"Has depositado ${monto}. Saldo actual: ${saldoInicial}")
        else:
            print("monto inválido")
    elif opcion == "3":
        monto = float(input("Ingresa el monto a retirar: "))
        if 0 < monto <= saldoInicial:
            saldoInicial -= monto
            print(f"Has retirado ${monto}. Saldo actual: ${saldoInicial}")
        else:
            print("monto inválido o saldo insuficiente.")
    elif opcion == "4":
        print(f"Gracias por usar el cajero. ¡Bye!")
        break
    else:
        print("opción no valida. intenta de nuevo")
print("============Finalizo el programa============")