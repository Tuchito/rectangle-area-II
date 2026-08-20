"""
Skill: setup-virtual-environment

Crea un entorno virtual `.venv/` en la raíz del proyecto e instala el set
base de herramientas de calidad (pytest, pytest-cov, mypy, black, isort),
instalando únicamente las que falten.

Limitación de sistema operativo (ver proposal.md): un script no puede
activar el entorno en la shell del usuario que lo invocó. El reporte final
siempre incluye el comando manual de activación.

Nota de diseño: `instalar_dependencias()` recibe la función que ejecuta
`pip install` como parámetro inyectable (`ejecutar_pip`). Esto separa la
lógica de negocio (qué instalar y cuándo) del efecto secundario externo
(llamar a pip por red), permitiendo testear la decisión sin depender de
una conexión a internet real en cada corrida de tests.
"""

from __future__ import annotations

import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

HERRAMIENTAS_BASE: frozenset[str] = frozenset(
    {"pytest", "pytest-cov", "mypy", "black", "isort"}
)

VENV_DIRNAME = ".venv"


class EntornoVirtualError(Exception):
    """Error claro cuando no se puede crear el entorno virtual (p. ej. módulo venv ausente)."""


@dataclass
class EstadoEntornoVirtual:
    """Estado detectado del entorno virtual antes de ejecutar el skill (solo lectura)."""

    existe_venv: bool
    herramientas_instaladas: set[str] = field(default_factory=set)


@dataclass
class ReporteEjecucion:
    """Resumen legible de qué hizo (o no) el skill en esta ejecución."""

    acciones: list[str] = field(default_factory=list)

    def agregar(self, mensaje: str) -> None:
        self.acciones.append(mensaje)

    def texto(self) -> str:
        return "\n".join(self.acciones)


def _ruta_pip(raiz: Path) -> Path:
    """Función privada auxiliar: ruta al ejecutable pip dentro del venv (Unix)."""
    return raiz / VENV_DIRNAME / "bin" / "pip"


def _ruta_python_venv(raiz: Path) -> Path:
    """Función privada auxiliar: ruta al intérprete Python dentro del venv (Unix)."""
    return raiz / VENV_DIRNAME / "bin" / "python"


def verificar_estado(raiz: Path) -> EstadoEntornoVirtual:
    """Tarea 1: detecta si .venv/ existe y qué herramientas del set base ya están instaladas."""
    existe = _ruta_python_venv(raiz).exists()
    if not existe:
        return EstadoEntornoVirtual(existe_venv=False, herramientas_instaladas=set())

    instaladas = _listar_paquetes_instalados(raiz)
    return EstadoEntornoVirtual(existe_venv=True, herramientas_instaladas=instaladas)


def _listar_paquetes_instalados(raiz: Path) -> set[str]:
    """Función privada auxiliar de verificar_estado(). Consulta `pip list --format=freeze`."""
    resultado = subprocess.run(
        [str(_ruta_pip(raiz)), "list", "--format=freeze"],
        capture_output=True,
        text=True,
        check=False,
    )
    paquetes: set[str] = set()
    for linea in resultado.stdout.splitlines():
        nombre = linea.split("==")[0].strip().lower()
        if nombre:
            paquetes.add(nombre)
    return paquetes


def crear_entorno_virtual(
    raiz: Path, estado: EstadoEntornoVirtual, reporte: ReporteEjecucion
) -> None:
    """Tarea 2: crea .venv/ usando el módulo venv del sistema, solo si falta."""
    if estado.existe_venv:
        reporte.agregar("– .venv/ ya existía, sin cambios")
        return

    resultado = subprocess.run(
        [sys.executable, "-m", "venv", str(raiz / VENV_DIRNAME)],
        capture_output=True,
        text=True,
        check=False,
    )
    if resultado.returncode != 0:
        raise EntornoVirtualError(
            "No se pudo crear el entorno virtual. Verificá que el módulo "
            f"'venv' esté disponible en tu instalación de Python. Detalle: {resultado.stderr.strip()}"
        )
    reporte.agregar("✔ .venv/ creado")


def instalar_dependencias(
    raiz: Path,
    estado: EstadoEntornoVirtual,
    reporte: ReporteEjecucion,
    ejecutar_pip: Callable[[Path, str], None] | None = None,
) -> None:
    """
    Tarea 3: instala, vía pip del venv, únicamente las herramientas del set
    base que verificar_estado() reportó como faltantes.
    """
    if ejecutar_pip is None:
        ejecutar_pip = _pip_install_real

    faltantes = sorted(HERRAMIENTAS_BASE - estado.herramientas_instaladas)

    if not faltantes:
        reporte.agregar("– herramientas de calidad ya estaban instaladas, sin cambios")
        return

    for herramienta in faltantes:
        ejecutar_pip(raiz, herramienta)
        reporte.agregar(f"✔ {herramienta} instalado")


def _pip_install_real(raiz: Path, paquete: str) -> None:
    """Función privada auxiliar: implementación real de instalación vía pip (efecto de red)."""
    subprocess.run(
        [str(_ruta_pip(raiz)), "install", paquete],
        check=True,
        capture_output=True,
    )


def orquestar(
    raiz: Path,
    ejecutar_pip: Callable[[Path, str], None] | None = None,
) -> ReporteEjecucion:
    """
    Tarea 4: punto de entrada del skill.

    Verifica el estado una sola vez y decide, en base a ese resultado, si
    crea el entorno virtual y/o instala dependencias. Ninguna de las dos
    funciones vuelve a verificar por su cuenta (ver design.md, sección 4).
    """
    reporte = ReporteEjecucion()
    estado = verificar_estado(raiz)
    crear_entorno_virtual(raiz, estado, reporte)
    instalar_dependencias(raiz, estado, reporte, ejecutar_pip=ejecutar_pip)
    return reporte


def generar_texto_resumen(reporte: ReporteEjecucion) -> str:
    """
    Tarea 5: formatea el reporte de ejecución, incluyendo siempre el
    comando de activación manual (limitación de sistema operativo).
    """
    lineas = ["Resumen de ejecución:", reporte.texto()]
    lineas.append("")
    lineas.append("Para activar el entorno en tu terminal, ejecutá:")
    lineas.append(f"  source {VENV_DIRNAME}/bin/activate")
    return "\n".join(lineas)


if __name__ == "__main__":
    proyecto_raiz = Path.cwd()
    reporte_final = orquestar(proyecto_raiz)
    print(generar_texto_resumen(reporte_final))