propietarios = {}
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
                placas = {}
                for i in range(cantidad_vehiculos):
                    placa = str(input("Ingrese la placa del vehiculo: "))
                    marca = str(input("Ingrese la marca del vehiculo: "))
                    modelo = str(input("Ingrese el modelo del vehiculo: "))
                    ano_vehiculo = int(input("Ingrese el año del vehiculo: "))
                    pago = str(input("Se tiene pagado el impuesto del vehiculo (Si/No)?: ")).lower()
                    placas[placa] = {"marca": marca, "modelo": modelo, "ano": ano_vehiculo, "pago": pago}
                    propietarios[nit] = {"nombre":nombre, "telefono":telefono, 'carros':placas}
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
                for placa, data in datos['carros'].items():
                    print(f"Placa: {placa}, Marca:{data['marca']}, Modelo:{data['modelo']}, Año: {data['ano']}, Pago: {data['pago']}")
                    print()
        case "3":
            print("Buscar propietario")
            nit_busqueda = int(input("Ingrese el NIT del propietario: "))
            if nit_busqueda in propietarios:
                print(f"Nombre: {propietarios[nit_busqueda]['nombre']}")
                print(f"Telefono: {propietarios[nit_busqueda]['telefono']}")
            for placa, data in propietarios[nit_busqueda]['carros'].items():
                print("Información del vehiculo")
                print(f"Placa: {placa}, Marca:{data['marca']}, Modelos:{data['modelo']}, Año:{data['ano']}, Pago:{data['pago']}")
                print()
        case "4":
            print("Verificación de pago")
            pago = 0
            no_pago = 0
            for i in propietarios.values():
                for j in i['carros'].values():
                    if j['pago']=="si":
                        pago+=1
                    else:
                        no_pago+=1
            print(f"Cantidad de vehiculos que han pagado: {pago}")
            print(f"Cantidad de vehiculos que no han pagado: {no_pago}")
            print()
        case "5":
            print("Saliendo del programa, gracias por su preferencia")
            break
        case _:
            print("Valor invalido, vuelva a intentar")