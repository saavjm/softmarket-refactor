# Guía de contribución

## 1. Modelo de ramas (GitFlow simplificado sobre GitHub)

- `main` y `develop` son **ramas protegidas**: no se hace push directo, solo Pull Request (PR).
- Nombres de ramas: `feature/<modulo>-<descripcion>`, `release/<X.Y.Z>`, `hotfix/<X.Y.Z>-<descripcion>`, `docs/<tema>`.
- Las ramas viven poco tiempo (máx. 3 días de trabajo) para reducir conflictos.

## 2. Convención de commits (Conventional Commits)

```
<tipo>(<alcance>): <descripción en imperativo, máx. 72 caracteres>

[cuerpo opcional: qué y por qué]

[pie opcional: Closes #12]
```

Tipos: `feat`, `fix`, `refactor`, `test`, `docs`, `style`, `chore`, `ci`.

## 3. Pull Requests

1. Mínimo **1 aprobación** (2 hacia `main`) de alguien distinto al autor.
2. Pruebas pasando y cobertura >= 80 % en código nuevo.
3. Se completa la plantilla del PR (qué cambia, cómo se probó, riesgos).
4. Merge con `--no-ff` desde `feature/*`, `release/*` y `hotfix/*` para conservar el historial.

## 4. Conflictos

- Antes de abrir el PR: `git fetch && git rebase origin/develop` en la rama de trabajo.
- Si hay conflicto: resolver localmente, ejecutar pruebas y subir con `git push --force-with-lease`.
- Nunca resolver conflictos "aceptando todo" de un lado sin hablar con el autor del otro cambio.
