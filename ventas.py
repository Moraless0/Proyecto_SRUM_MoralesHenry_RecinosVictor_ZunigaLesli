def cambiar_estado():
    data = cargar()
    codigo = non_empty("Código de orden: ")
    orden = next((o for o in data if o["codigo"] == codigo), None)

    if not orden:
        print("⚠ No existe.")
        return

    print("Estados: Pendiente / En Proceso / Enviado / Entregado / Cancelado")
    nuevo = non_empty("Nuevo estado: ")

    # Si se envía o entrega, descontar inventario
    if orden["estado"] not in ["Enviado", "Entregado"] and nuevo in ["Enviado", "Entregado"]:
        for item in orden["items"]:
            inventario.sumar_producto(item["codigo"], -item["cantidad"])

    orden["estado"] = nuevo
    guardar(data)
    print("✅ Estado actualizado.")