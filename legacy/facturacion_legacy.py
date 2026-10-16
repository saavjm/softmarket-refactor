# CÓDIGO LEGADO DE SOFTMARKET (ejemplo del "caos")
# Un solo módulo hace TODO: validar, calcular, guardar, notificar e imprimir.
# Problemas: viola SRP/OCP/DIP, duplicación, números mágicos, sin pruebas.

import sqlite3


def generar_factura(cliente, items, tipo_cliente, correo):
    # items = [(nombre, precio, cantidad), ...]
    total = 0
    for i in items:
        total = total + i[1] * i[2]

    # descuentos (cada nuevo tipo de cliente obliga a modificar este if)
    if tipo_cliente == "VIP":
        total = total - total * 0.15
    elif tipo_cliente == "MAYORISTA":
        total = total - total * 0.25
    elif tipo_cliente == "EMPLEADO":
        total = total - total * 0.30

    # impuesto "quemado" en el código
    total = total + total * 0.19

    # acceso a base de datos mezclado con la lógica de negocio
    con = sqlite3.connect("softmarket.db")
    cur = con.cursor()
    cur.execute("INSERT INTO facturas (cliente, total) VALUES ('" + cliente + "', " + str(total) + ")")
    con.commit()
    con.close()

    # envío de correo mezclado también (y duplicado en otros módulos)
    print("Enviando correo a " + correo + " con total " + str(total))

    # impresión
    print("FACTURA para " + cliente)
    for i in items:
        print(i[0], i[1], i[2])
    print("TOTAL:", total)
    return total
