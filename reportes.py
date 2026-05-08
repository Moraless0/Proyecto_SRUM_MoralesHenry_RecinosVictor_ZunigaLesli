import materias_primas
import proveedores
import productos
import clientes
import inventario

def menu():
    while True:
        print("\n=== Reportes ===")
        print("1. Materias primas")
        print("2. Proveedores")
        print("3. Productos finales")
        print("4. Clientes")
        print("5. Inventario")
        print("0. Volver")

        op = input("Opción: ").strip()

        if op == "1": materias_primas.listar()
        elif op == "2": proveedores.listar()
        elif op == "3": productos.listar()
        elif op == "4": clientes.listar()
        elif op == "5": inventario.mostrar()
        elif op == "0": break
        else: print("⚠ Opción inválida.")