from persistence import load_json, save_json
from validators import non_empty, email, phone, unique_code

FILE = "clientes.json"

def cargar():
    return load_json(FILE, [])

def guardar(data):
    save_json(FILE, data)
