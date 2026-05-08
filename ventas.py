from persistence import load_json, save_json
from validators import non_empty, positive_int, unique_code
import clientes
import productos
import inventario

FILE = "ventas.json"

def cargar():
    return load_json(FILE, [])

def guardar(data):
    save_json(FILE, data)

def registrar():
    data = cargar()
    cli = clientes.cargar()
    prods = productos.cargar()

    print("\n=== Registrar Orden de Venta ===")

    while True:
        codigo = non_empty("Código: ")
        if unique_code(codigo, data, "codigo"):
            break
        print("⚠ Código repetido.")

    print("\nClientes disponibles:")
    for c in cli:
        print(f"{c['codigo']} - {c['empresa']}")

    cod_cli = non_empty("Código cliente: ")
    cliente = next((c for c in cli if c["codigo"] == cod_cli), None)
    if not cliente:
        print("⚠ Cliente no encontrado.")
        return

    print("\nProductos disponibles:")
    for p in prods:
        print(f"{p['codigo']} - {p['nombre']} (Stock: {p['stock']})")

    items = []
    total = 0

    print("\nIngrese productos (vacío para terminar):")
    while True:
        cod_prod = input("Código producto: ").strip()
        if cod_prod == "":
            break
        prod = next((p for p in prods if p["codigo"] == cod_prod), None)
        if not prod:
            print("⚠ No existe.")
            continue
        cant = positive_int("Cantidad: ")
        subtotal = cant * prod["precio"]
        total += subtotal
        items.append({"codigo": cod_prod, "cantidad": cant, "subtotal": subtotal})

    orden = {
        "codigo": codigo,
        "cliente": cod_cli,
        "items": items,
        "total": total,
        "estado": "Pendiente"
    }

    data.append(orden)
    guardar(data)
    print(f"✅ Orden registrada. Total: Q{total}")