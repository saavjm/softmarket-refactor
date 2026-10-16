# ADR-001: Usar el patrón Strategy para los descuentos

- **Estado:** Aceptada
- **Fecha:** 2026-10-16

## Contexto
El módulo legado calculaba descuentos con una cadena `if/elif` por tipo de cliente.
Cada nuevo tipo obligaba a modificar la función de facturación y ya causó errores en producción.

## Decisión
Definir la interfaz `PoliticaDescuento` y una clase por política. El servicio recibe el diccionario
de políticas por inyección de dependencias.

## Consecuencias
- (+) Agregar un descuento = agregar una clase (Open/Closed).
- (+) Cada política se prueba de forma aislada.
- (–) Más archivos y clases para un caso simple; se compensa con la claridad y la extensibilidad.
