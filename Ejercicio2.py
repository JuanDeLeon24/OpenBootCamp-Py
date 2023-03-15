agenda = {}

while True:
    print("¿Qué acción deseas realizar?")
    print("1 - Añadir una persona")
    print("2 - Buscar el teléfono de una persona")
    print("0 - Salir")
    opcion = input()

    if opcion == "1":
        nombre = input("Introduce el nombre de la persona: ")
        telefono = input("Introduce el teléfono de la persona: ")
        agenda[nombre] = telefono
        print("Se ha añadido a", nombre, "con el teléfono", telefono)
    elif opcion == "2":
        busqueda = input("Introduce el nombre de la persona que quieres buscar: ")
        encontrados = []
        for nombre, telefono in agenda.items():
            if nombre.startswith(busqueda):
                encontrados.append((nombre, telefono))
        if len(encontrados) == 0:
            print("No se ha encontrado ninguna persona que coincida con la búsqueda.")
        elif len(encontrados) == 1:
            print("El teléfono de", encontrados[0][0], "es", encontrados[0][1])
        else:
            print("Se han encontrado las siguientes personas:")
            for nombre, telefono in encontrados:
                print(nombre, telefono)
    elif opcion == "0":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")
