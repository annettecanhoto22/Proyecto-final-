import json
from clases import Localidad, Municipio

def cargar_datos():
    
    archivo = open("zonas_caracas.json", "r", encoding="utf-8")
    contenido = json.load(archivo)
    archivo.close()

    lista_municipios = []

    for nombre_mun, lista_locs in contenido.items():
        objeto_mun = Municipio(nombre_mun)

        for loc_info in lista_locs:
            nombre_loc = loc_info["nombre"]
            lat = loc_info["latitud"]
            lon = loc_info["longitud"]
            objeto_loc = Localidad(nombre_loc, lat, lon)
            objeto_mun.agregar_localidad(objeto_loc)

        lista_municipios.append(objeto_mun)

    return lista_municipios
    
def generar_reporte_carga(lista_municipios):
    
    print("\n=== REPORTE DE CARGA DE LOCALIDADES ===\n")

    for mun in lista_municipios:
        total = len(mun)
        con_coord = mun.contar_con_coordenadas()
        sin_coord = mun.contar_sin_coordenadas()
        porcentaje = mun.porcentaje_con_coordenadas()

        print(f"Municipio: {mun.nombre}")
        print(f"  - Cantidad de localidades cargadas: {total}")
        print(f"  - Con coordenadas geográficas: {con_coord}")
        print(f"  - Sin coordenadas geográficas: {sin_coord}")
        print(f"  - Porcentaje con coordenadas: {porcentaje:.2f}%")
        print("-----------------------------------------------------")
