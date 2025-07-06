### bot_inventario.py
def main():
    inventario = {
        'Manzanas': {'cantidad': 50, 'precio': 1.50},
        'Leche': {'cantidad': 20, 'precio': 2.75},
        'Pan': {'cantidad': 10, 'precio': 3.00}
    }

    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Añadir Producto")
        print("2. Actualizar Stock")
        print("3. Eliminar Producto")
        print("4. Ver Inventario")
        print("5. Buscar Producto")
        print("6. Resumen de Inventario")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            anadir_producto(inventario)
        elif opcion == '2':
            actualizar_stock(inventario)
        elif opcion == '3':
            eliminar_producto(inventario)
        elif opcion == '4':
            ver_inventario(inventario)
        elif opcion == '5':
            buscar_producto(inventario)
        elif opcion == '6':
            resumen_inventario(inventario)
        elif opcion == '7':
            print("Saliendo del programa. Hasta pronto!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

def anadir_producto(inventario):
    print("\n--- Añadir Nuevo Producto ---")
    nombre = input("Ingrese el nombre del producto: ").strip().capitalize()
    if nombre in inventario:
        print(f"Error: El producto '{nombre}' ya existe en el inventario.")
        return

    cantidad = obtener_entero("Ingrese la cantidad inicial: ", minimo=0)
    precio = obtener_flotante("Ingrese el precio unitario: ", minimo=0)

    inventario[nombre] = {'cantidad': cantidad, 'precio': precio}
    print(f"Producto '{nombre}' añadido exitosamente.")

def actualizar_stock(inventario):
    print("\n--- Actualizar Stock de Producto ---")
    nombre = input("Ingrese el nombre del producto a actualizar: ").strip().capitalize()
    if nombre not in inventario:
        print(f"Error: El producto '{nombre}' no se encuentra en el inventario.")
        return

    print(f"Producto '{nombre}' encontrado. Cantidad actual: {inventario[nombre]['cantidad']}")
    nueva_cantidad = obtener_entero(f"Ingrese la nueva cantidad para '{nombre}': ", minimo=0)

    inventario[nombre]['cantidad'] = nueva_cantidad
    print(f"Stock de '{nombre}' actualizado a {nueva_cantidad}.")

def eliminar_producto(inventario):
    print("\n--- Eliminar Producto ---")
    nombre = input("Ingrese el nombre del producto a eliminar: ").strip().capitalize()
    if nombre not in inventario:
        print(f"Error: El producto '{nombre}' no se encuentra en el inventario.")
        return

    confirmacion = input(f"¿Está seguro que desea eliminar '{nombre}'? (s/n): ").lower()
    if confirmacion == 's':
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado exitosamente.")
    else:
        print("Eliminación cancelada.")

def ver_inventario(inventario):
    print("\n--- Inventario Actual ---")
    if not inventario:
        print("El inventario está vacío.")
        return

    for nombre, detalles in inventario.items():
        print(f"Nombre: {nombre}, Cantidad: {detalles['cantidad']}, Precio: ${detalles['precio']:.2f}")

def buscar_producto(inventario):
    print("\n--- Buscar Producto ---")
    termino = input("Ingrese el nombre o parte del nombre del producto a buscar: ").strip().lower()
    resultados = [(n, d) for n, d in inventario.items() if termino in n.lower()]

    if resultados:
        print("\n--- Resultados de la Búsqueda ---")
        for nombre, detalles in resultados:
            print(f"Nombre: {nombre}, Cantidad: {detalles['cantidad']}, Precio: ${detalles['precio']:.2f}")
    else:
        print(f"No se encontraron productos que coincidan con '{termino}'.")

def resumen_inventario(inventario):
    print("\n--- Resumen de Inventario ---")

    valor_total = sum(detalles['cantidad'] * detalles['precio'] for detalles in inventario.values())
    print(f"Valor Total del Inventario: ${valor_total:.2f}")

    umbral = 5
    bajo_stock = [n for n, d in inventario.items() if d['cantidad'] < umbral]

    if bajo_stock:
        print(f"Productos con bajo stock (cantidad < {umbral}):")
        for nombre in bajo_stock:
            print(f"- {nombre} (Cantidad: {inventario[nombre]['cantidad']})")
    else:
        print("No hay productos con bajo stock.")

    if any(detalles['cantidad'] == 0 for detalles in inventario.values()):
        print("Advertencia: Hay productos agotados en el inventario.")
    else:
        print("No hay productos agotados.")

def obtener_entero(mensaje, minimo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"El valor no puede ser menor que {minimo}. Intente de nuevo.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

def obtener_flotante(mensaje, minimo=None):
    while True:
        try:
            valor = float(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"El valor no puede ser menor que {minimo}. Intente de nuevo.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

if __name__ == "__main__":
    main()
