def consultar_por_municipio(lista_municipios, historial_consultas):
    
    print("\n--- SELECCIONE UN MUNICIPIO ---")
    for i, mun in enumerate(lista_municipios, start=1):
        print(f"{i}. {mun.nombre}")

    try:
        opcion_mun = int(input("Ingrese el número del municipio: ")) - 1
    except ValueError:
        print("Entrada inválida. Debe ingresar un número.")
        return

    if opcion_mun < 0 or opcion_mun >= len(lista_municipios):
        print("Opción inválida.")
        return

    mun_seleccionado = lista_municipios[opcion_mun]
    
