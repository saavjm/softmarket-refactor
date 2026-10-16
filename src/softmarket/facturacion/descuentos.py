"""Políticas de descuento (patrón Strategy).

OCP: para un nuevo tipo de cliente se agrega una clase nueva y se registra;
no se modifica el servicio ni las demás estrategias.
LSP: toda estrategia devuelve un Decimal >= 0 y <= subtotal.
"""
from abc import ABC, abstractmethod
from decimal import Decimal


class PoliticaDescuento(ABC):
    @abstractmethod
    def calcular(self, subtotal: Decimal) -> Decimal:
        """Devuelve el valor a descontar (no el total)."""


class SinDescuento(PoliticaDescuento):
    def calcular(self, subtotal: Decimal) -> Decimal:
        return Decimal("0")


class DescuentoPorcentual(PoliticaDescuento):
    def __init__(self, porcentaje: Decimal):
        if not Decimal("0") <= porcentaje <= Decimal("1"):
            raise ValueError("El porcentaje debe estar entre 0 y 1")
        self._porcentaje = porcentaje

    def calcular(self, subtotal: Decimal) -> Decimal:
        return subtotal * self._porcentaje


# Registro de políticas por categoría de cliente (configuración, no lógica)
POLITICAS_POR_CATEGORIA = {
    "REGULAR": SinDescuento(),
    "VIP": DescuentoPorcentual(Decimal("0.15")),
    "MAYORISTA": DescuentoPorcentual(Decimal("0.25")),
    "EMPLEADO": DescuentoPorcentual(Decimal("0.30")),
}
