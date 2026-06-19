if opcion == "1":
        print("\n--- REGISTRO DE NUEVA MUESTRA ---")
        codigo = input("Ingrese el código de la muestra (ej: M001): ")
        nombre = input("Ingrese el nombre del paciente: ")
        temperatura = float(input("Ingrese la temperatura de la muestra (°C): "))
        
        if temperatura < 2 or temperatura > 8:
            estado = "RECHAZADA"
            print(f"\nALERTA: Temperatura fuera de rango ({temperatura}°C). Muestra RECHAZADA.")
        elif temperatura >= 2 and temperatura <= 8:
            estado = "PENDIENTE"
            print(f"\nTemperatura válida ({temperatura}°C). Muestra registrada como PENDIENTE.")
       
        muestra_formateada = f"{codigo} - {nombre} - {estado}"
        muestras_lab.append(muestra_formateada)
        print(f"Muestra registrada: {muestra_formateada}")

    elif opcion == "2":
        print("\n--- BUSCAR Y GESTIONAR MUESTRA ---")
        if len(muestras_lab) == 0:
            print("No hay muestras registradas en el sistema.")
        else:
            codigo_buscar = input("Ingrese el código de la muestra a buscar: ")
            encontrada = False
            for i in range(len(muestras_lab)):
                if muestras_lab[i].startswith(codigo_buscar + " - "):
                    encontrada = True
                    print(f"\nMuestra encontrada: {muestras_lab[i]}")
                    print("\n  a) Actualizar estado")
                    print("  b) Desechar muestra")
                    accion = input("  Seleccione una acción (a/b): ")
                    if accion == "a":
                        nuevo_estado = input("Ingrese el nuevo estado (ej: ANALIZADA): ")
                        partes = muestras_lab[i].split(" - ")
                        muestras_lab[i] = f"{partes[0]} - {partes[1]} - {nuevo_estado}"
                        print(f"Estado actualizado: {muestras_lab[i]}")
                    elif accion == "b":
                        print(f"Muestra eliminada: {muestras_lab[i]}")
                        muestras_lab.pop(i)
                    else:
                        print("Acción no válida.")
                    break
            if not encontrada:
                print(f"El código '{codigo_buscar}' no existe en el sistema.") 