"""Caso de uso: emitir una factura.

SRP: orquesta; no calcula descuentos, no guarda, no envía correos por sí mismo.
DIP: recibe sus dependencias por constructor (inyección de dependencias).
"""
from typing import Dict, List

from .descuentos import POLITICAS_POR_CATEGORIA, PoliticaDescuento, SinDescuento
from .impuestos import CalculadorImpuesto
from .modelos import Cliente, Factura, LineaFactura
from .puertos import Notificador, RepositorioFacturas


class ServicioFacturacion:
    def __init__(
        self,
        repositorio: RepositorioFacturas,
        notificador: Notificador,
        impuesto: CalculadorImpuesto,
        politicas: Dict[str, PoliticaDescuento] = None,
    ):
        self._repositorio = repositorio
        self._notificador = notificador
        self._impuesto = impuesto
        self._politicas = politicas or POLITICAS_POR_CATEGORIA

    def emitir(self, cliente: Cliente, lineas: List[LineaFactura]) -> Factura:
        if not lineas:
            raise ValueError("Una factura requiere al menos una línea")

        factura = Factura(cliente=cliente, lineas=list(lineas))
        politica = self._politicas.get(cliente.categoria, SinDescuento())
        factura.descuento = politica.calcular(factura.subtotal)
        factura.impuesto = self._impuesto.calcular(factura.subtotal - factura.descuento)

        self._repositorio.guardar(factura)
        self._notificador.notificar(factura)
        return factura
