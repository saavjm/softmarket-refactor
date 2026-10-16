# Arquitectura del módulo de facturación

```
ServicioFacturacion  ──usa──►  PoliticaDescuento (ABC)  ◄── SinDescuento, DescuentoPorcentual
        │               └────►  CalculadorImpuesto (ABC) ◄── IVA
        │               └────►  RepositorioFacturas (ABC) ◄── RepositorioSQLite, RepositorioMemoria
        │               └────►  Notificador (ABC)         ◄── NotificadorConsola
Exportador (ABC) ◄── ExportadorTexto
```

Las flechas de dependencia apuntan siempre hacia abstracciones (Dependency Inversion).
