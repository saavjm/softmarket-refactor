"""Interfaces (puertos) pequeñas y específicas.

ISP: cada interfaz tiene un solo método; quien solo notifica no depende de guardar.
DIP: el servicio de negocio depende de estas abstracciones, no de SQLite, SMTP ni print.
"""
from abc import ABC, abstractmethod

from .modelos import Factura


class RepositorioFacturas(ABC):
    @abstractmethod
    def guardar(self, factura: Factura) -> None: ...


class Notificador(ABC):
    @abstractmethod
    def notificar(self, factura: Factura) -> None: ...


class Exportador(ABC):
    @abstractmethod
    def exportar(self, factura: Factura) -> str: ...
