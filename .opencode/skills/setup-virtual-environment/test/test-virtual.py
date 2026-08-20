"""
Tests del skill setup-virtual-environment.

Cada test está ligado a un criterio de "hecho" definido en tasks.md.
`instalar_dependencias()` y `orquestar()` se testean con un `ejecutar_pip`
falso (no se golpea la red en cada corrida) — la creación real de `.venv/`
sí se ejecuta, porque no requiere red y es rápida.
"""

from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import pytest

from implementation import (
    HERRAMIENTAS_BASE,
    EntornoVirtualError,
    ReporteEjecucion,
    crear_entorno_virtual,
    generar_texto_resumen,
    instalar_dependencias,
    orquestar,
    verificar_estado,
)


def _reporte_vacio() -> ReporteEjecucion:
    return ReporteEjecucion()


def _pip_fake(llamadas: list[tuple[Path, str]]):
    """Fábrica de un ejecutar_pip falso que solo registra las llamadas recibidas."""

    def _fn(raiz: Path, paquete: str) -> None:
        llamadas.append((raiz, paquete))

    return _fn


# ---------------------------------------------------------------------------
# Tarea 1: verificar_estado()
# ---------------------------------------------------------------------------

def test_verificar_estado_sin_venv(tmp_path: Path) -> None:
    estado = verificar_estado(tmp_path)
    assert not estado.existe_venv
    assert estado.herramientas_instaladas == set()


def test_verificar_estado_con_venv_recien_creado(tmp_path: Path) -> None:
    reporte = _reporte_vacio()
    estado_previo = verificar_estado(tmp_path)
    crear_entorno_virtual(tmp_path, estado_previo, reporte)

    estado = verificar_estado(tmp_path)
    assert estado.existe_venv
    # Un venv recién creado no tiene ninguna de nuestras herramientas instaladas.
    assert estado.herramientas_instaladas.isdisjoint(HERRAMIENTAS_BASE)


# ---------------------------------------------------------------------------
# Tarea 2: crear_entorno_virtual()
# ---------------------------------------------------------------------------

def test_crear_entorno_virtual_desde_cero(tmp_path: Path) -> None:
    reporte = _reporte_vacio()
    estado = verificar_estado(tmp_path)
    crear_entorno_virtual(tmp_path, estado, reporte)

    assert (tmp_path / ".venv" / "bin" / "python").exists()
    assert "creado" in reporte.texto()


def test_crear_entorno_virtual_es_idempotente(tmp_path: Path) -> None:
    reporte1 = _reporte_vacio()
    estado1 = verificar_estado(tmp_path)
    crear_entorno_virtual(tmp_path, estado1, reporte1)

    reporte2 = _reporte_vacio()
    estado2 = verificar_estado(tmp_path)  # ahora ya existe
    crear_entorno_virtual(tmp_path, estado2, reporte2)  # no debe recrear ni fallar

    assert "ya existía" in reporte2.texto()


def test_crear_entorno_virtual_reporta_error_claro_si_falla(tmp_path: Path) -> None:
    estado = verificar_estado(tmp_path)
    reporte = _reporte_vacio()

    with patch("implementation.subprocess.run") as mock_run:
        mock_run.return_value.returncode = 1
        mock_run.return_value.stderr = "No module named venv"

        with pytest.raises(EntornoVirtualError, match="módulo 'venv'"):
            crear_entorno_virtual(tmp_path, estado, reporte)


# ---------------------------------------------------------------------------
# Tarea 3: instalar_dependencias()
# ---------------------------------------------------------------------------

def test_instalar_dependencias_instala_solo_faltantes(tmp_path: Path) -> None:
    from implementation import EstadoEntornoVirtual

    estado = EstadoEntornoVirtual(
        existe_venv=True, herramientas_instaladas={"pytest", "black"}
    )
    reporte = _reporte_vacio()
    llamadas: list[tuple[Path, str]] = []

    instalar_dependencias(tmp_path, estado, reporte, ejecutar_pip=_pip_fake(llamadas))

    paquetes_instalados = {paquete for _, paquete in llamadas}
    assert paquetes_instalados == {"pytest-cov", "mypy", "isort"}
    assert "pytest-cov instalado" in reporte.texto()
    assert "pytest" not in [l.split(" ")[1] for l in reporte.acciones if "✔" in l]


def test_instalar_dependencias_no_hace_nada_si_ya_estan_todas(tmp_path: Path) -> None:
    from implementation import EstadoEntornoVirtual

    estado = EstadoEntornoVirtual(
        existe_venv=True, herramientas_instaladas=set(HERRAMIENTAS_BASE)
    )
    reporte = _reporte_vacio()
    llamadas: list[tuple[Path, str]] = []

    instalar_dependencias(tmp_path, estado, reporte, ejecutar_pip=_pip_fake(llamadas))

    assert llamadas == []
    assert "sin cambios" in reporte.texto()


# ---------------------------------------------------------------------------
# Tarea 4: orquestar() — idempotencia end-to-end
# ---------------------------------------------------------------------------

def test_orquestar_end_to_end_sobre_proyecto_vacio(tmp_path: Path) -> None:
    llamadas: list[tuple[Path, str]] = []
    reporte = orquestar(tmp_path, ejecutar_pip=_pip_fake(llamadas))

    assert (tmp_path / ".venv").exists()
    assert len(llamadas) == len(HERRAMIENTAS_BASE)
    assert "✔ .venv/ creado" in reporte.texto()


def test_orquestar_segunda_ejecucion_no_recrea_venv(tmp_path: Path) -> None:
    llamadas_primera: list[tuple[Path, str]] = []
    orquestar(tmp_path, ejecutar_pip=_pip_fake(llamadas_primera))

    llamadas_segunda: list[tuple[Path, str]] = []
    reporte_segunda = orquestar(tmp_path, ejecutar_pip=_pip_fake(llamadas_segunda))

    assert "ya existía" in reporte_segunda.texto()
    # La segunda vez, verificar_estado() no puede ver instaladas las
    # herramientas (se instalaron sobre un pip falso, no uno real), así que
    # el fake se sigue llamando — lo relevante es que .venv/ no se recreó.
    assert (tmp_path / ".venv" / "bin" / "python").exists()


# ---------------------------------------------------------------------------
# Tarea 5: reporte de ejecución con instrucción de activación
# ---------------------------------------------------------------------------

def test_generar_texto_resumen_incluye_comando_de_activacion(tmp_path: Path) -> None:
    llamadas: list[tuple[Path, str]] = []
    reporte = orquestar(tmp_path, ejecutar_pip=_pip_fake(llamadas))
    texto = generar_texto_resumen(reporte)

    assert "source .venv/bin/activate" in texto


def test_generar_texto_resumen_incluye_activacion_aunque_no_haya_cambios(
    tmp_path: Path,
) -> None:
    from implementation import EstadoEntornoVirtual

    estado = EstadoEntornoVirtual(
        existe_venv=True, herramientas_instaladas=set(HERRAMIENTAS_BASE)
    )
    reporte = _reporte_vacio()
    instalar_dependencias(tmp_path, estado, reporte, ejecutar_pip=_pip_fake([]))
    texto = generar_texto_resumen(reporte)

    assert "source .venv/bin/activate" in texto