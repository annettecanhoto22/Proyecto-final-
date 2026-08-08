from funciones import consultar_clima_tiempo_real, mostrar_detalles_clima

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
    locs_validas = mun_seleccionado.obtener_localidades_con_coordenadas()

    if not locs_validas:
        print("Este municipio no tiene localidades con coordenadas válidas.")
        return

    print(f"\n--- LOCALIDADES EN {mun_seleccionado.nombre} ---")
    for j, loc in enumerate(locs_validas, start=1):
        print(f"{j}. {loc}")

    try:
        opcion_loc = int(input("\nIngrese el número de la localidad: ")) - 1
    except ValueError:
        print("Entrada inválida. Debe ingresar un número.")
        return

    if opcion_loc < 0 or opcion_loc >= len(locs_validas):
        print("Opción inválida.")
        return

    loc_seleccionada = locs_validas[opcion_loc]
    clima = consultar_clima_tiempo_real( mun_seleccionado.nombre, loc_seleccionada.nombre, loc_seleccionada.latitud, loc_seleccionada.longitud)

    if clima is not None:
        historial_consultas.append(clima)
        mostrar_detalles_clima(clima)

def consultar_por_busqueda_directa (lista_municipios, historial_consultas):

    busqueda = input("\nIngrese el nombre (o parte del nombre) de la localidad: ").strip().lower()

    coincidencias = []
    municipios_coincidencia = []

    for mun in lista_municipios:
        locs_validas = mun.obtener_localidades_con_coordenadas()
        for loc in locs_validas:
            if busqueda in loc.nombre.lower():
                coincidencias.append(loc)
                municipios_coincidencia.append(mun.nombre)

    if not coincidencias:
        print("No se encontraron localidades con coordenadas válidas que coincidan con la búsqueda.")
        return

    print("\n--- COINCIDENCIAS ENCONTRADAS ---")
    for idx, loc in enumerate(coincidencias, start=1):
        print(f"{idx}. {loc.nombre} (Municipio: {municipios_coincidencia[idx - 1]})")

    try:
        seleccion = int(input("Seleccione el número de la localidad: ")) - 1
    except ValueError:
        print("Entrada inválida. Debe ingresar un número.")
        return

    if seleccion < 0 or seleccion >= len(coincidencias):
        print("Selección inválida.")
        return

    loc_elegida = coincidencias[seleccion]
    mun_elegido = municipios_coincidencia[seleccion]

    clima = consultar_clima_tiempo_real(mun_elegido, loc_elegida.nombre, loc_elegida.latitud, loc_elegida.longitud)

    if clima is not None:
        historial_consultas.append(clima)
        mostrar_detalles_clima(clima)

    
