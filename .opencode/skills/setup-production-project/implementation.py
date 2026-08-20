"""
Skill: setup-production-project (versión acotada para práctica de skills)

Automatiza el setup inicial de un proyecto de práctica algorítmica:
- Estructura de carpetas mínima (src/, tests/), respetando openspec/ existente.
- Inicialización de Git local con rama `main`.
- Generación de `.gitignore`, con merge inteligente si ya existe.

Explícitamente fuera de alcance (permanecen manuales, ver proposal.md):
AGENTS.md, entorno virtual, creación/push de repositorio remoto.

Diseño: ver design.md — idempotente, con verificación de estado centralizada
en `orquestar()`. Ninguna otra función decide "si ya existe o no" por su cuenta.
"""

from __future__ import annotations

import subprocess
from dataclasses import dataclass, field
from pathlib import Path

GITIGNORE_TEMPLATE = """# Entornos virtuales
venv/
.venv/
env/

# Cachés de Python
__pycache__/
*.py[cod]
*.egg-info/

# Cobertura y testing
.coverage
.pytest_cache/
htmlcov/

# mypy
.mypy_cache/

# Configuración de editor / IDE
.vscode/
.idea/
.cursor/

# Archivos del sistema operativo
.DS_Store
Thumbs.db

# LeetCode / práctica algorítmica
*.pyc
__pycache__/
.pytest_cache/
.coverage
htmlcov/
*.log
.DS_Store

# Variables de entorno sensibles
.env
"""

MERGE_MARKER = "# Agregado por setup-production-project"


@dataclass
class EstadoProyecto:
    """Estado detectado del proyecto antes de ejecutar el skill (solo lectura)."""

    existe_openspec: bool
    existe_src: bool
    existe_tests: bool
    existe_git: bool
    existe_rama_main: bool
    existe_gitignore: bool
    contenido_gitignore: str = ""


@dataclass
class ReporteEjecucion:
    """Resumen legible de qué hizo (o no) el skill en esta ejecución."""

    acciones: list[str] = field(default_factory=list)

    def agregar(self, mensaje: str) -> None:
        self.acciones.append(mensaje)

    def texto(self) -> str:
        return "\n".join(self.acciones)


def verificar_estado(raiz: Path) -> EstadoProyecto:
    """Tarea 1: detecta el estado actual del proyecto sin modificar nada."""
    gitignore_path = raiz / ".gitignore"
    contenido = (
        gitignore_path.read_text(encoding="utf-8") if gitignore_path.exists() else ""
    )
    return EstadoProyecto(
        existe_openspec=(raiz / "openspec").exists(),
        existe_src=(raiz / "src").exists(),
        existe_tests=(raiz / "tests").exists(),
        existe_git=(raiz / ".git").exists(),
        existe_rama_main=_existe_rama_main(raiz),
        existe_gitignore=gitignore_path.exists(),
        contenido_gitignore=contenido,
    )


def _existe_rama_main(raiz: Path) -> bool:
    """
    Función privada auxiliar de verificar_estado(). No se invoca fuera de acá.

    Nota de diseño: `git branch --list` no detecta una rama sin commits
    (git init -b main "nombra" la rama pero no crea su referencia hasta el
    primer commit). Se usa `git symbolic-ref` porque sí resuelve el nombre
    de la rama actual incluso en un repositorio recién inicializado.
    """
    if not (raiz / ".git").exists():
        return False
    resultado = subprocess.run(
        ["git", "symbolic-ref", "--short", "HEAD"],
        cwd=raiz,
        capture_output=True,
        text=True,
        check=False,
    )
    return resultado.stdout.strip() == "main"


def crear_estructura(
    raiz: Path, estado: EstadoProyecto, reporte: ReporteEjecucion
) -> None:
    """Tarea 2: crea src/ y tests/ solo si faltan. No toca openspec/."""
    if not estado.existe_src:
        (raiz / "src").mkdir(parents=True, exist_ok=True)
        reporte.agregar("✔ src/ creada")
    else:
        reporte.agregar("– src/ ya existía, sin cambios")

    if not estado.existe_tests:
        (raiz / "tests").mkdir(parents=True, exist_ok=True)
        reporte.agregar("✔ tests/ creada")
    else:
        reporte.agregar("– tests/ ya existía, sin cambios")

    if estado.existe_openspec:
        reporte.agregar("– openspec/ ya existía, sin cambios")


def inicializar_git(
    raiz: Path, estado: EstadoProyecto, reporte: ReporteEjecucion
) -> None:
    """Tarea 3: inicializa Git y crea la rama main solo si faltan."""
    if not estado.existe_git:
        subprocess.run(
            ["git", "init", "-b", "main"], cwd=raiz, check=True, capture_output=True
        )
        reporte.agregar("✔ Git inicializado, rama main creada")
        return

    if not estado.existe_rama_main:
        subprocess.run(
            ["git", "checkout", "-b", "main"],
            cwd=raiz,
            check=True,
            capture_output=True,
        )
        reporte.agregar("✔ Rama main creada sobre repositorio existente")
    else:
        reporte.agregar("– Git y rama main ya existían, sin cambios")


def generar_gitignore(
    raiz: Path, estado: EstadoProyecto, reporte: ReporteEjecucion
) -> None:
    """Tarea 4: genera .gitignore, o hace merge inteligente si ya existe."""
    gitignore_path = raiz / ".gitignore"

    if not estado.existe_gitignore:
        gitignore_path.write_text(GITIGNORE_TEMPLATE, encoding="utf-8")
        reporte.agregar("✔ .gitignore generado")
        return

    lineas_existentes = set(_lineas_normalizadas(estado.contenido_gitignore))
    lineas_plantilla = _lineas_normalizadas(GITIGNORE_TEMPLATE)
    faltantes = [
        linea
        for linea in lineas_plantilla
        if linea and linea not in lineas_existentes
    ]

    if not faltantes:
        reporte.agregar("– .gitignore ya contenía todas las reglas, sin cambios")
        return

    bloque_nuevo = "\n" + MERGE_MARKER + "\n" + "\n".join(faltantes) + "\n"
    with gitignore_path.open("a", encoding="utf-8") as f:
        f.write(bloque_nuevo)
    reporte.agregar(
        f"✔ .gitignore actualizado ({len(faltantes)} reglas nuevas agregadas, "
        f"{len(lineas_existentes)} ya existentes respetadas)"
    )


def _lineas_normalizadas(contenido: str) -> list[str]:
    """Función privada auxiliar: extrae líneas de reglas, ignorando comentarios."""
    return [
        linea.strip()
        for linea in contenido.splitlines()
        if linea.strip() and not linea.strip().startswith("#")
    ]


def orquestar(raiz: Path) -> ReporteEjecucion:
    """
    Tarea 5: punto de entrada del skill.

    Verifica el estado una sola vez y decide, en base a ese resultado, qué
    pasos ejecutar. Las funciones llamadas no vuelven a verificar por su
    cuenta — la decisión vive únicamente acá (ver design.md, sección 4).
    """
    reporte = ReporteEjecucion()
    estado = verificar_estado(raiz)
    crear_estructura(raiz, estado, reporte)
    inicializar_git(raiz, estado, reporte)
    generar_gitignore(raiz, estado, reporte)
    return reporte


def generar_texto_resumen(reporte: ReporteEjecucion) -> str:
    """Tarea 6: formatea el reporte de ejecución para el desarrollador."""
    return "Resumen de ejecución:\n" + reporte.texto()


if __name__ == "__main__":
    proyecto_raiz = Path.cwd()
    reporte_final = orquestar(proyecto_raiz)
    print(generar_texto_resumen(reporte_final))