import os
import sys
import unittest
from decimal import Decimal

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from softmarket.facturacion.descuentos import DescuentoPorcentual, PoliticaDescuento
from softmarket.facturacion.impuestos import IVA
from softmarket.facturacion.infraestructura import ExportadorTexto, RepositorioMemoria
from softmarket.facturacion.modelos import Cliente, LineaFactura
from softmarket.facturacion.puertos import Notificador
from softmarket.facturacion.servicio import ServicioFacturacion


class NotificadorFalso(Notificador):
    """Doble de prueba: gracias a DIP no se envían correos reales."""

    def __init__(self):
        self.enviados = 0

    def notificar(self, factura):
        self.enviados += 1


def lineas():
    return [LineaFactura("Licencia", Decimal("100"), 2), LineaFactura("Soporte", Decimal("50"), 1)]


class PruebasFacturacion(unittest.TestCase):
    def setUp(self):
        self.repo = RepositorioMemoria()
        self.notif = NotificadorFalso()
        self.servicio = ServicioFacturacion(self.repo, self.notif, IVA())

    def test_cliente_regular_sin_descuento(self):
        f = self.servicio.emitir(Cliente("Ana", "ana@x.co"), lineas())
        self.assertEqual(f.subtotal, Decimal("250"))
        self.assertEqual(f.descuento, Decimal("0"))
        self.assertEqual(f.total, Decimal("297.50"))

    def test_cliente_vip_descuento_15(self):
        f = self.servicio.emitir(Cliente("Luis", "l@x.co", "VIP"), lineas())
        self.assertEqual(f.descuento, Decimal("37.50"))

    def test_se_guarda_y_notifica(self):
        self.servicio.emitir(Cliente("Ana", "ana@x.co"), lineas())
        self.assertEqual(len(self.repo.facturas), 1)
        self.assertEqual(self.notif.enviados, 1)

    def test_factura_sin_lineas_falla(self):
        with self.assertRaises(ValueError):
            self.servicio.emitir(Cliente("Ana", "ana@x.co"), [])

    def test_cantidad_invalida(self):
        with self.assertRaises(ValueError):
            LineaFactura("X", Decimal("10"), 0)

    def test_ocp_nueva_politica_sin_modificar_servicio(self):
        class Black(PoliticaDescuento):
            def calcular(self, subtotal):
                return subtotal * Decimal("0.5")

        servicio = ServicioFacturacion(self.repo, self.notif, IVA(), {"BLACK": Black()})
        f = servicio.emitir(Cliente("Eva", "e@x.co", "BLACK"), lineas())
        self.assertEqual(f.descuento, Decimal("125"))

    def test_exportador_texto(self):
        f = self.servicio.emitir(Cliente("Ana", "ana@x.co"), lineas())
        self.assertIn("TOTAL: 297.50", ExportadorTexto().exportar(f))


if __name__ == "__main__":
    unittest.main()
