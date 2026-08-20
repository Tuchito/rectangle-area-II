"""
Tests del skill setup-production-project.

Cada test está ligado a un criterio de "hecho" definido en tasks.md.
Cobertura objetivo: >90% (criterio de validación del curso).
"""

from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

from implementation import (
    GITIGNORE_TEMPLATE,
    MERGE_MARKER,
    crear_estructura,
    generar_gitignore,
    generar_texto_resumen,
    inicializar_git,
    orquestar,
    verificar_estado,
)


# ---------------------------------------------------------------------------
# Tarea 1: verificar_estado()
# ---------------------------------------------------------------------------

def test_verificar_estado_proyecto_vacio(tmp_path: Path) -> None:
    estado = verificar_estado(tmp_path)
    assert not estado.existe_openspec
    assert not estado.existe_src
    assert not estado.existe_tests
    assert not estado.existe_git
    assert not estado.existe_gitignore


def test_verificar_estado_con_openspec_ya_creado(tmp_path: Path) -> None:
    (tmp_path / "openspec").mkdir()
    estado = verificar_estado(tmp_path)
    assert estado.existe_openspec
    assert not estado.existe_src


def test_verificar_estado_con_git_ya_inicializado(tmp_path: Path) -> None:
    subprocess.run(["git", "init", "-b", "main"], cwd=tmp_path, check=True, capture_output=True)
    estado = verificar_estado(tmp_path)
    assert estado.existe_git
    assert estado.existe_rama_main


# ---------------------------------------------------------------------------
# Tarea 2: crear_estructura()
# ---------------------------------------------------------------------------

def test_crear_estructura_en_proyecto_vacio(tmp_path: Path) -> None:
    estado = verificar_estado(tmp_path)
    reporte = _reporte_vacio()
    crear_estructura(tmp_path, estado, reporte)
    assert (tmp_path / "src").exists()
    assert (tmp_path / "tests").exists()


def test_crear_estructura_es_idempotente(tmp_path: Path) -> None:
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "marcador.txt").write_text("no borrar")

    estado = verificar_estado(tmp_path)
    reporte = _reporte_vacio()
    crear_estructura(tmp_path, estado, reporte)

    assert (tmp_path / "src" / "marcador.txt").exists()  # no se borró el contenido
    assert "ya existía" in reporte.texto()


def test_crear_estructura_no_toca_openspec_existente(tmp_path: Path) -> None:
    (tmp_path / "openspec").mkdir()
    (tmp_path / "openspec" / "changes.txt").write_text("contenido original")

    estado = verificar_estado(tmp_path)
    reporte = _reporte_vacio()
    crear_estructura(tmp_path, estado, reporte)

    assert (tmp_path / "openspec" / "changes.txt").read_text() == "contenido original"


# ---------------------------------------------------------------------------
# Tarea 3: inicializar_git()
# ---------------------------------------------------------------------------

def test_inicializar_git_desde_cero(tmp_path: Path) -> None:
    estado = verificar_estado(tmp_path)
    reporte = _reporte_vacio()
    inicializar_git(tmp_path, estado, reporte)
    assert (tmp_path / ".git").exists()


def test_inicializar_git_es_idempotente(tmp_path: Path) -> None:
    subprocess.run(["git", "init", "-b", "main"], cwd=tmp_path, check=True, capture_output=True)
    estado = verificar_estado(tmp_path)
    reporte = _reporte_vacio()
    inicializar_git(tmp_path, estado, reporte)  # no debe fallar
    assert "ya existían" in reporte.texto()


# ---------------------------------------------------------------------------
# Tarea 4: generar_gitignore() con merge inteligente
# ---------------------------------------------------------------------------

def test_generar_gitignore_sin_archivo_previo(tmp_path: Path) -> None:
    estado = verificar_estado(tmp_path)
    reporte = _reporte_vacio()
    generar_gitignore(tmp_path, estado, reporte)

    contenido = (tmp_path / ".gitignore").read_text()
    assert contenido == GITIGNORE_TEMPLATE
    assert "generado" in reporte.texto()


def test_generar_gitignore_hace_merge_de_reglas_faltantes(tmp_path: Path) -> None:
    (tmp_path / ".gitignore").write_text("venv/\n.env\n")  # parcial, faltan reglas

    estado = verificar_estado(tmp_path)
    reporte = _reporte_vacio()
    generar_gitignore(tmp_path, estado, reporte)

    contenido = (tmp_path / ".gitignore").read_text()
    assert "venv/" in contenido  # regla original respetada
    assert MERGE_MARKER in contenido
    assert "__pycache__/" in contenido  # regla nueva agregada
    assert "reglas nuevas agregadas" in reporte.texto()


def test_generar_gitignore_no_modifica_si_ya_esta_completo(tmp_path: Path) -> None:
    (tmp_path / ".gitignore").write_text(GITIGNORE_TEMPLATE)

    estado = verificar_estado(tmp_path)
    reporte = _reporte_vacio()
    generar_gitignore(tmp_path, estado, reporte)

    contenido = (tmp_path / ".gitignore").read_text()
    assert contenido == GITIGNORE_TEMPLATE  # sin cambios, sin bloque de merge
    assert "sin cambios" in reporte.texto()


# ---------------------------------------------------------------------------
# Tarea 5: orquestar() — idempotencia end-to-end
# ---------------------------------------------------------------------------

def test_orquestar_end_to_end_sobre_proyecto_vacio(tmp_path: Path) -> None:
    reporte = orquestar(tmp_path)
    assert (tmp_path / "src").exists()
    assert (tmp_path / "tests").exists()
    assert (tmp_path / ".git").exists()
    assert (tmp_path / ".gitignore").exists()
    assert "✔" in reporte.texto()


def test_orquestar_segunda_ejecucion_no_produce_cambios_adicionales(
    tmp_path: Path,
) -> None:
    orquestar(tmp_path)  # primera ejecución: crea todo
    gitignore_despues_de_primera = (tmp_path / ".gitignore").read_text()

    reporte_segunda = orquestar(tmp_path)  # segunda ejecución: no debe alterar nada

    gitignore_despues_de_segunda = (tmp_path / ".gitignore").read_text()
    assert gitignore_despues_de_primera == gitignore_despues_de_segunda
    assert "✔" not in reporte_segunda.texto()  # nada nuevo se creó
    assert all(
        ("ya exist" in linea) or ("ya conten" in linea)
        for linea in reporte_segunda.acciones
    )


def test_orquestar_respeta_openspec_inicializado_manualmente(tmp_path: Path) -> None:
    (tmp_path / "openspec").mkdir()
    (tmp_path / "openspec" / "project.md").write_text("config original")

    orquestar(tmp_path)

    assert (tmp_path / "openspec" / "project.md").read_text() == "config original"


# ---------------------------------------------------------------------------
# Tarea 6: reporte de ejecución
# ---------------------------------------------------------------------------

def test_generar_texto_resumen_incluye_encabezado(tmp_path: Path) -> None:
    reporte = orquestar(tmp_path)
    texto = generar_texto_resumen(reporte)
    assert texto.startswith("Resumen de ejecución:")
    assert "src/" in texto


def _reporte_vacio():
    from implementation import ReporteEjecucion

    return ReporteEjecucion()