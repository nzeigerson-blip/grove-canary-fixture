"""Canary fixture tests — pytest entrypoint."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from canary import add  # noqa: E402


def test_add_simple() -> None:
    assert add(1, 2) == 3


def test_add_negative() -> None:
    assert add(-1, -1) == -2


def test_add_zero() -> None:
    assert add(0, 0) == 0
