"""Cálculo de impuestos como abstracción intercambiable."""
from abc import ABC, abstractmethod
from decimal import Decimal, ROUND_HALF_UP


class CalculadorImpuesto(ABC):
    @abstractmethod
    def calcular(self, base: Decimal) -> Decimal:
        """Devuelve el valor del impuesto sobre la base gravable."""


class IVA(CalculadorImpuesto):
    def __init__(self, tarifa: Decimal = Decimal("0.19")):
        self._tarifa = tarifa

    def calcular(self, base: Decimal) -> Decimal:
        return (base * self._tarifa).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
