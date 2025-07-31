propietarios = {}
placas = {}
while True:
    print("--Menú--")
    print("1.- Ingresar propietario")
    print("2.- Mostrar resumen general")
    print("3.- Buscar propietario")
    print("4.- Verificación de pago")
    print("5.- Salir del programa")
    opcion = input("Ingrese el número de la opción que desea ingresar: ")
    print()
    match opcion:
        case "1":
            print("Ingresar propietario")
            cantidad_propietarios = int(input("Ingrese la cantidad de propietarios a registrar: "))
            for i in range(cantidad_propietarios):
                nit = int(input("Ingrese el número de identificación (NIT): "))
                nombre = str(input("Ingrese el nombre del propietario: "))
                telefono = int(input("Ingrese el número de telefono: "))
                cantidad_vehiculos = int(input("Ingrese la cantidad de vehiculos a registrar: "))
                for i in range(cantidad_vehiculos):
                    placa = str(input("Ingrese la placa del vehiculo: "))
                    marca = str(input("Ingrese la marca del vehiculo: "))
                    modelo = str(input("Ingrese el modelo del vehiculo: "))
                    ano_vehiculo = int(input("Ingrese el año del vehiculo: "))
                    pago = str(input("Se tiene pagado el impuesto del vehiculo (Si/No)?: "))
                    propietarios[nit] = {"nombre":nombre, "telefono":telefono}
                    placas[placa] = {"marca":marca, "modelo":modelo, "ano":ano_vehiculo, "pago":pago}
                    print()
            print("Se ha hecho el registro correctamente")
            print()
        case "2":
            print("Resumen general")
            for nit, datos in propietarios.items():
                print(f"Identificación: {nit}")
                print(f"Nombre: {datos['nombre']}")
                print(f"Telefono: {datos['telefono']}")
                print()
                for placa, datos in placas.items():
                    print(f"Placa: {placa}, Marcas:{datos['marca']}, Modelo:{datos['modelo']}, Año: {datos['ano']}, Pago: {datos['pago']}")
        case "3":
            print("Buscar propietario")
        case "4":
            print("Verificación de pago")
        case "5":
            print("Saliendo del programa, gracias por su preferencia")
        case _:
            print("Valor invalido, vuelva a intentar")