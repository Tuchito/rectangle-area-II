---
name: setup-virtual-environment
description: Crea el entorno virtual .venv/ en la raíz del proyecto e instala el set base de herramientas de calidad (pytest, pytest-cov, mypy, black, isort), instalando únicamente las que falten. Uso cuando el usuario quiere preparar o completar el entorno de desarrollo de un proyecto.
allowed-tools: Bash(python:*), Bash(pip:*)
license: MIT
compatibility: Requiere Python 3.10+ con el módulo venv disponible. Asume rutas de estilo Unix (.venv/bin/). No activa el entorno en la shell del usuario (limitación de sistema operativo) — el reporte final indica el comando manual de activación.
metadata:
  author: curso-ai-skill-architect
  version: "1.0"
  generatedBy: "practica-rectangle-area-ii"
  status: borrador — pendiente de confirmación al archivar openspec/changes/create-setup-virtual-environment
---

# setup-virtual-environment

## Qué hace

1. Crea `.venv/` en la raíz del proyecto si no existe.
2. Instala, dentro de ese entorno, únicamente las herramientas del set
   base que falten: `pytest`, `pytest-cov`, `mypy`, `black`, `isort`.
3. Informa siempre el comando de activación manual, ya que un script no
   puede activar el entorno en la terminal del usuario.

## Qué NO hace

- No selecciona una versión de Python distinta a la del sistema.
- No activa el entorno automáticamente (limitación de sistema operativo,
  ver `proposal.md`).

## Idempotencia

Ejecutarlo varias veces sobre el mismo proyecto no recrea `.venv/` ni
reinstala herramientas ya presentes. Solo actúa sobre lo que falta.

## Cómo se invoca

Desde OpenCode, vía el comando delegado `/setup-virtual-environment`
(ver `.opencode/commands/setup-virtual-environment.md`), o directamente:

```bash
python .opencode/skills/setup-virtual-environment/implementation.py
```

## Salida esperada

```
Resumen de ejecución:
✔ .venv/ creado
✔ pytest instalado
✔ pytest-cov instalado
✔ mypy instalado
✔ black instalado
✔ isort instalado

Para activar el entorno en tu terminal, ejecutá:
  source .venv/bin/activate
```

## Especificación de origen

`openspec/changes/create-setup-virtual-environment/{proposal,design,tasks,delta}.md`

## Tests

`tests/test_implementation.py` — 11 tests, 93% de cobertura. La instalación
real vía pip (`_pip_install_real`) se inyecta como dependencia y no se
ejecuta en los tests, para no depender de la red en cada corrida:

```bash
python -m pytest .opencode/skills/setup-virtual-environment/tests/ --cov=implementation
```