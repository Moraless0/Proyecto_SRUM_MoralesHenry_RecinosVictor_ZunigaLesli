from persistence import load_json, save_json
from validators import non_empty, non_negative_float, positive_int, unique_code

FILE = "productos.json"

def cargar():
    return load_json(FILE, [])

def guardar(data):
    save_json(FILE, data)

def registrar():
    data = cargar()
    print("\n=== Registrar Producto Final ===")


    while True:
        codigo = non_empty("Código: ")
        if unique_code(codigo, data, "codigo"):
            break
        print("⚠ Código repetido.")

    nombre = non_empty("Nombre: ")
    descripcion = non_empty("Descripción: ")
    precio = non_negative_float("Precio de venta: ")
    stock = positive_int("Stock inicial: ")

    item = {
        "codigo": codigo,
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": precio,
        "stock": stock
    }