"""Canary fixture module — used by Grove v2 end-to-end canary tests.

This module intentionally contains a deliberate bug that v2 must fix in
order for the canary CI run to succeed.  The fix is trivial; the point of
the canary is to prove the *delivery loop* end-to-end (issue created →
v2 dispatched → role agent edited a file → PR opened → tests green).

DO NOT "fix" this file in this repo's main branch.  The bug is the test.
"""
from __future__ import annotations


def add(a: int, b: int) -> int:
    """Return the sum of a and b.

    Intentionally buggy implementation — should be ``a + b``.
    """
    return a - b  # bug: should be a + b
