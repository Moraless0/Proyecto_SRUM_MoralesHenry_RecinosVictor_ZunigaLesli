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