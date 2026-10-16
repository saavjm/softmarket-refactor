"""Entidades del dominio. Solo datos y reglas propias (SRP)."""
from dataclasses import dataclass, field
from decimal import Decimal
from typing import List


@dataclass(frozen=True)
class Cliente:
    nombre: str
    correo: str
    categoria: str = "REGULAR"  # REGULAR, VIP, MAYORISTA, EMPLEADO


@dataclass(frozen=True)
class LineaFactura:
    descripcion: str
    precio_unitario: Decimal
    cantidad: int

    def __post_init__(self):
        if self.cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")
        if self.precio_unitario < 0:
            raise ValueError("El precio no puede ser negativo")

    @property
    def subtotal(self) -> Decimal:
        return self.precio_unitario * self.cantidad


@dataclass
class Factura:
    cliente: Cliente
    lineas: List[LineaFactura] = field(default_factory=list)
    descuento: Decimal = Decimal("0")
    impuesto: Decimal = Decimal("0")

    @property
    def subtotal(self) -> Decimal:
        return sum((l.subtotal for l in self.lineas), Decimal("0"))

    @property
    def total(self) -> Decimal:
        return self.subtotal - self.descuento + self.impuesto
