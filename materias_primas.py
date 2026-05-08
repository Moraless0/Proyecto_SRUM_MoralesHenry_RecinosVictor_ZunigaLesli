from persistence import load_json, save_json
from validators import non_empty, positive_int, non_negative_float, unique_code

FILE = "materias_primas.json"

def cargar():
    return load_json(FILE, [])

def guardar(data):
    save_json(FILE, data)

def registrar():
    data = cargar()
    print("\n=== Registrar Materia Prima ===")

    while True:
        codigo = non_empty("Código: ")
        if unique_code(codigo, data, "codigo"):
            break
        print("⚠ Código repetido.")

    nombre = non_empty("Nombre: ")
    descripcion = non_empty("Descripción: ")
    proveedor = non_empty("Proveedor: ")
    stock = positive_int("Cantidad en stock: ")
    precio = non_negative_float("Precio por unidad: ")

    item = {
        "codigo": codigo,
        "nombre": nombre,
        "descripcion": descripcion,
        "proveedor": proveedor,
        "stock": stock,
        "precio": precio
    }

    data.append(item)
    guardar(data)
    print("✅ Registrado.")

def listar():
    data = cargar()
    print("\n=== Materias Primas ===")
    if not data:
        print("No hay registros.")
        return
    for m in data:
        print(f"{m['codigo']} - {m['nombre']} (Stock: {m['stock']})")