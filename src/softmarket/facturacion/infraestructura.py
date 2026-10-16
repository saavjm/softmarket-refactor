"""Implementaciones concretas de los puertos (detalles intercambiables)."""
import sqlite3

from .modelos import Factura
from .puertos import Exportador, Notificador, RepositorioFacturas


class RepositorioMemoria(RepositorioFacturas):
    """Útil para pruebas: no requiere base de datos."""

    def __init__(self):
        self.facturas = []

    def guardar(self, factura: Factura) -> None:
        self.facturas.append(factura)


class RepositorioSQLite(RepositorioFacturas):
    def __init__(self, ruta: str):
        self._ruta = ruta

    def guardar(self, factura: Factura) -> None:
        # Consulta parametrizada: elimina la inyección SQL del código legado
        with sqlite3.connect(self._ruta) as con:
            con.execute(
                "INSERT INTO facturas (cliente, total) VALUES (?, ?)",
                (factura.cliente.nombre, str(factura.total)),
            )


class NotificadorConsola(Notificador):
    def notificar(self, factura: Factura) -> None:
        print(f"Correo a {factura.cliente.correo}: total {factura.total}")


class ExportadorTexto(Exportador):
    def exportar(self, factura: Factura) -> str:
        filas = [f"FACTURA para {factura.cliente.nombre}"]
        for l in factura.lineas:
            filas.append(f"{l.descripcion} x{l.cantidad} @ {l.precio_unitario} = {l.subtotal}")
        filas.append(f"TOTAL: {factura.total}")
        return "\n".join(filas)
