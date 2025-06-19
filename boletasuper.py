import os

productos = []
boleta_info = {"cantidad_productos": 0, "subtotal": 0, "iva": 0, "total": 0}

productos_disponibles = {
    "1": {"nombre": "Mantequilla", "precio": 3290},
    "2": {"nombre": "Pan de molde", "precio": 2000},
    "3": {"nombre": "Galletas", "precio": 750},
    "4": {"nombre": "Fideos", "precio": 990},
    "5": {"nombre": "Arroz", "precio": 1550},
    "6": {"nombre": "Salchichas", "precio": 3390}
}

def clear_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\nPresiona Enter para continuar...")

def mostrar_mensaje(mensaje):
    print(f"\n📢 {mensaje}")

def pedir_productos():
    while True:
        clear_pantalla()
        print("=== SELECCIONA UN PRODUCTO ===")
        for key, prod in productos_disponibles.items():
            print(f"{key}. {prod['nombre']} - ${prod['precio']}")
        print("0. Volver al menú")

        opcion = input("\n¿Qué producto deseas llevar? Ingresa su número: ").strip()

        if opcion == "0":
            break

        if opcion in productos_disponibles:
            producto = productos_disponibles[opcion]
            try:
                cantidad = int(input(f"¿Cuántas unidades de '{producto['nombre']}' deseas llevar?: "))
                if cantidad <= 0:
                    mostrar_mensaje("La cantidad debe ser mayor a cero.")
                    pausar()
                    continue
            except ValueError:
                mostrar_mensaje("Debes ingresar un número válido.")
                pausar()
                continue

            for _ in range(cantidad):
                productos.append({"nombre": producto["nombre"], "precio": producto["precio"]})
                boleta_info["cantidad_productos"] += 1
                boleta_info["subtotal"] += producto["precio"]

            mostrar_mensaje(f"Añadido {cantidad} x {producto['nombre']} por ${producto['precio']} cada uno.")
        else:
            mostrar_mensaje("Opción inválida.")
        pausar()

def calcular_iva_y_total():
    try:
        boleta_info["iva"] = boleta_info["subtotal"] * 0.19
        boleta_info["total"] = boleta_info["subtotal"] + boleta_info["iva"]
    except Exception:
        boleta_info["iva"] = 0
        boleta_info["total"] = boleta_info["subtotal"]

def mostrar_productos():
    while True:
        clear_pantalla()
        print("=== PRODUCTOS COMPRADOS ===")
        if not productos:
            print("🛒 No hay productos en la lista.")
        else:
            conteo_productos = {}
            for prod in productos:
                nombre = prod['nombre']
                conteo_productos[nombre] = conteo_productos.get(nombre, 0) + 1
            
            for i, (nombre, cantidad) in enumerate(sorted(conteo_productos.items()), start=1):
                precio_unitario = next(p['precio'] for p in productos if p['nombre'] == nombre)
                print(f"{i}. {nombre} x{cantidad} {precio_unitario}")
            
            calcular_iva_y_total()

            print(f"\nSubtotal: ${round(boleta_info['subtotal'])}")
            print(f"IVA (19%): ${round(boleta_info['iva'], 2)}")
            print(f"Total a pagar: ${round(boleta_info['total'])}")

        respuesta = input("\nPresiona 0 para volver al menú o escribe 'eliminar' para quitar el último producto: ").strip()
        if respuesta == "eliminar" and productos:
            eliminado = productos.pop()
            boleta_info["cantidad_productos"] -= 1
            boleta_info["subtotal"] -= eliminado["precio"]
            mostrar_mensaje(f"Producto eliminado: {eliminado['nombre']}")
            pausar()
        elif respuesta == "0":
            break

def pagar():
    while True:
        clear_pantalla()
        print("=== MÉTODO DE PAGO ===")
        print("1. Débito")
        print("2. Crédito")
        print("3. Efectivo")
        metodo = input("Selecciona una opción (1-3): ")
        if metodo in ("1", "2", "3"):
            mostrar_mensaje("Procesando su pago...")
            pausar()
            break
        else:
            mostrar_mensaje("Opción inválida.")
            pausar()

def ver_total():
    calcular_iva_y_total()
    clear_pantalla()
    print(f"\n💰 Total a pagar: ${round(boleta_info['total'])}")
    pausar()

def menu_principal():
    while True:
        clear_pantalla()
        print("=== MENÚ PRINCIPAL ===")
        print("1. Añadir producto")
        print("2. Mostrar productos")
        print("3. Ver total a pagar y pagar")
        print("4. Salir")

        opcion = input("\nSelecciona una opción (1-4): ")

        if opcion == "1":
            pedir_productos()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            ver_total()
            pagar()
            break
        elif opcion == "4":
            clear_pantalla()
            print("¡Que tengas un buen día! 👋")
            break
        elif opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4":
            mostrar_mensaje("Opción inválida.")
            pausar()

# Ejecutar programa
menu_principal()











