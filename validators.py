import re

def non_empty(msg):
    while True:
        v = input(msg).strip()
        if v:
            return v
        print("⚠ No puede estar vacío.")

def positive_int(msg):
    while True:
        v = input(msg).strip()
        if v.isdigit() and int(v) > 0:
            return int(v)
        print("⚠ Ingrese un entero positivo.")

def non_negative_float(msg):
    while True:
        try:
            v = float(input(msg).strip())
            if v >= 0:
                return v
        except:
            pass
        print("⚠ Ingrese un número válido.")

def email(msg):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    while True:
        v = input(msg).strip()
        if re.match(pattern, v):
            return v
        print("⚠ Correo inválido.")

def phone(msg):
    pattern = r"^[0-9\-\+\s]{7,15}$"
    while True:
        v = input(msg).strip()
        if re.match(pattern, v):
            return v
        print("⚠ Teléfono inválido.")

def unique_code(code, items, key):
    return not any(i[key] == code for i in items)