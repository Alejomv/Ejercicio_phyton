def format_currency(amount):
    return "${:,.0f}".format(amount).replace(",", ".")

# Precios de los destinos
precios = {
    "Guajira": {"adulto": 1450000, "niño": 870000},
    "Cañon del Chicamocha": {"adulto": 1600000, "niño": 960000},
    "Llanos Orientales": {"adulto": 1200000, "niño": 720000},
}

# Lista para almacenar las reservas
reservas = []

# Contadores para las estadísticas
total_viajeros = {"Guajira": 0, "Cañon del Chicamocha": 0, "Llanos Orientales": 0}
total_dinero = {"Guajira": 0, "Cañon del Chicamocha": 0, "Llanos Orientales": 0}
total_adultos = 0
total_niños = 0

while True:
    print("Seleccione una opción:")
    print("1. Ingresar información")
    print("2. Ver datos ingresados")
    print("3. Modificar viaje")
    print("4. Eliminar viaje")
    print("5. Salir")
    opcion = input()

    if opcion == '1':
      # Ingreso de nueva reserva
        nombre_cliente = input("Nombre del cliente: ")
        nro_personas_adultas = int(input("Número de personas adultas: "))
        nro_niños = int(input("Número de niños: "))
        print("Seleccione entre los siguientes destinos:")
        print("1. Guajira")
        print("2. Cañon del Chicamocha")
        print("3. Llanos Orientales")
        destino_opcion = int(input())
        if destino_opcion == 1:
            destino = "Guajira"
        elif destino_opcion == 2:
            destino = "Cañon del Chicamocha"
        else:
            destino = "Llanos Orientales"
        total_a_pagar = (nro_personas_adultas * precios[destino]["adulto"]
                         + nro_niños * precios[destino]["niño"])
        reserva = {
            'nombre_cliente': nombre_cliente,
            'nro_personas_adultas': nro_personas_adultas,
            'nro_niños': nro_niños,
            'destino': destino,
            'total_a_pagar': total_a_pagar
        }
        reservas.append(reserva)
        print("\nDatos ingresados:")
        print(f"✓ Nombre Cliente: {nombre_cliente}")
        print(f"✓ Nombre del destino: {destino}")
        print(f"✓ Nro Personas Adultas: {nro_personas_adultas}")
        print(f"✓ Nro Niños: {nro_niños}")
        print(f"✓ Valor Total a Pagar: {format_currency(total_a_pagar)}")
        # Actualización de las estadísticas
        total_adultos += nro_personas_adultas
        total_niños += nro_niños
        total_viajeros[destino] += nro_personas_adultas + nro_niños
        total_dinero[destino] += total_a_pagar

    elif opcion == '2':
	
	
	        # Ver estadísticas y datos ingresados
        print("\nEstadísticas:")
        print("Cantidad de personas que viajan para la Guajira:", total_viajeros["Guajira"])
        print("Cantidad de personas que viajan para Cañón del Chicamocha:", total_viajeros["Cañon del Chicamocha"])
        print("Cantidad de personas que viajan para los llanos orientales:", total_viajeros["Llanos Orientales"])
        print("Total de dinero de los viajes para la Guajira:", format_currency(total_dinero["Guajira"]))
        print("Total de dinero de los viajes para Cañón del Chicamocha:", format_currency(total_dinero["Cañon del Chicamocha"]))
        print("Total de dinero de los viajes para los llanos orientales:", format_currency(total_dinero["Llanos Orientales"]))
        print("Total de personas Adultas:", total_adultos)
        print("Total de niños:", total_niños)
        print("Total de dinero de todos los destinos:", format_currency(sum(total_dinero.values())))
       

    elif opcion == '3':
        # Modificar viaje
        if not reservas:
            print("No hay reservas para modificar.")
            continue
        for i, reserva in enumerate(reservas):
            print(f"{i+1}. {reserva['nombre_cliente']} - {reserva['destino']}")
        idx = int(input("Seleccione el viaje que desea modificar: ")) - 1
        if 0 <= idx < len(reservas):
            # Guardamos los valores antiguos para actualizar las estadísticas
            reserva_antigua = reservas[idx]

        # Código para modificar la reserva seleccionada
            print("Datos actuales de la reserva:")
            print(f"Nombre Cliente: {reservas[idx]['nombre_cliente']}")
            print(f"Destino: {reservas[idx]['destino']}")
            print(f"Nro Personas Adultas: {reservas[idx]['nro_personas_adultas']}")
            print(f"Nro Niños: {reservas[idx]['nro_niños']}")
            print(f"Valor Total a Pagar: {format_currency(reservas[idx]['total_a_pagar'])}")
            print("Ingrese los nuevos datos:")
            
            nombre_cliente = input("Nombre del cliente: ")
            nro_personas_adultas = int(input("Número de personas adultas: "))
            nro_niños = int(input("Número de niños: "))
            
            print("Seleccione entre los siguientes destinos:")
            print("1. Guajira")
            print("2. Cañon del Chicamocha")
            print("3. Llanos Orientales")
            
            destino_opcion = int(input())
            if destino_opcion == 1:
                destino = "Guajira"
            elif destino_opcion == 2:
                destino = "Cañon del Chicamocha"
            else:
                destino = "Llanos Orientales"         

            # Actualizamos las estadísticas con los valores antiguos
            total_adultos -= reserva_antigua['nro_personas_adultas']
            total_niños -= reserva_antigua['nro_niños']
            total_viajeros[reserva_antigua['destino']] -= (reserva_antigua['nro_personas_adultas'] + reserva_antigua['nro_niños'])
            total_dinero[reserva_antigua['destino']] -= reserva_antigua['total_a_pagar']

            total_a_pagar = (nro_personas_adultas * precios[destino]["adulto"]
                             + nro_niños * precios[destino]["niño"])  # Calcula el nuevo total a pagar

            # Actualiza la reserva con los nuevos datos
            reservas[idx] = {
                'nombre_cliente': nombre_cliente,
                'nro_personas_adultas': nro_personas_adultas,
                'nro_niños': nro_niños,
                'destino': destino,
                'total_a_pagar': total_a_pagar  # Aquí se actualiza el total a pagar
            }
            
            # Actualizamos las estadísticas con los nuevos valores
            total_adultos += nro_personas_adultas
            total_niños += nro_niños
            total_viajeros[destino] += (nro_personas_adultas + nro_niños)
            total_dinero[destino] += total_a_pagar  # Aquí actualizas el total de dinero para el destino

    elif opcion == '4':
       
	   # Eliminar viaje
        if not reservas:
            print("No hay reservas para eliminar.")
            continue
        for i, reserva in enumerate(reservas):
            print(f"{i+1}. {reserva['nombre_cliente']} - {reserva['destino']}")
        idx = int(input("Seleccione el viaje que desea eliminar: ")) - 1
        if 0 <= idx < len(reservas):
            # Actualizamos las estadísticas antes de eliminar
            reserva_eliminar = reservas[idx]
            total_adultos -= reserva_eliminar['nro_personas_adultas']
            total_niños -= reserva_eliminar['nro_niños']
            total_viajeros[reserva_eliminar['destino']] -= (reserva_eliminar['nro_personas_adultas'] + reserva_eliminar['nro_niños'])
            total_dinero[reserva_eliminar['destino']] -= reserva_eliminar['total_a_pagar']
            
            # Eliminamos la reserva
            del reservas[idx]
            print("Reserva eliminada exitosamente.")
        else:
            print("Índice inválido.")

    elif opcion == '5':
        print("Programa Terminado!")
        break

    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
##MARTINEZ VELEZ DANIEL ALEJANDRO 
##VALENCIA MONA JONATHAN LEANDRO