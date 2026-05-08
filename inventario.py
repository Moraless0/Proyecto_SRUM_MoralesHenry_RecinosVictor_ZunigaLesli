from persistence import load_json, save_json

FILE = "inventario.json"

def cargar():
    return load_json(FILE, {"materias": {}, "productos": {}})

def guardar(data):
    save_json(FILE, data)

def sumar_materia(codigo, cantidad):
    inv = cargar()
    inv["materias"][codigo] = inv["materias"].get(codigo, 0) + cantidad
    guardar(inv)

def sumar_producto(codigo, cantidad):
    inv = cargar()
    inv["productos"][codigo] = inv["productos"].get(codigo, 0) + cantidad
    guardar(inv)

def mostrar():
    inv = cargar()
    print("\n=== Inventario ===")
    print("Materias primas:")
    for k, v in inv["materias"].items():
        print(f"{k}: {v}")
    print("\nProductos finales:")
    for k, v in inv["productos"].items():
        print(f"{k}: {v}")