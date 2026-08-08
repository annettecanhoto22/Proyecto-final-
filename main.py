def main():
    
    while True:
        print("\n=== SISTEMA METEOROLÓGICO CARACAS ===\n")
        print("1. Consultar clima por Municipio / Localidad")
        print("2. Búsqueda directa por Localidad")
        print("3. Ver Estadísticas de la Sesión")
        print("4. Consulta Histórica Meteorológica")
        print("5. Salir del programa")

        opcion = input("\nSeleccione una opción (1-5): ").strip()

        if opcion == "1":
            consultar_por_municipio(lista_municipios, historial_consultas)
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            pass
        elif opcion == "5":
            print("\n¡Gracias por utilizar MeteoCaracas! Hasta luego.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()
