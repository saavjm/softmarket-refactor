# SoftMarket – Repositorio simulado de la propuesta de buenas prácticas

Repositorio de ejemplo que acompaña el informe técnico *"Refactorizando el Caos en SoftMarket"*.
Muestra el modelo de ramas, las convenciones de commits y la refactorización SOLID del módulo de **facturación**.

## Estructura

```
legacy/            Código original (antes del refactor)
src/softmarket/    Código refactorizado aplicando SOLID
tests/             Pruebas unitarias (unittest)
docs/              Documentación técnica y ADRs
CONTRIBUTING.md    Flujo de trabajo Git y reglas de contribución
```

## Ejecutar las pruebas

```bash
python -m unittest discover -s tests -v
```

## Ramas

| Rama | Propósito |
|------|-----------|
| `main` | Código en producción, siempre estable y etiquetado (`vX.Y.Z`) |
| `develop` | Integración de funcionalidades terminadas |
| `feature/*` | Nuevas funcionalidades (nacen de `develop`) |
| `release/*` | Preparación de una versión (nacen de `develop`) |
| `hotfix/*` | Corrección urgente en producción (nace de `main`) |
| `docs/*` | Cambios solo de documentación |

Ver `CONTRIBUTING.md` para el detalle.
