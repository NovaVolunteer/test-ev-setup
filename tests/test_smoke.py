"""Smoke test: proves the package is importable from the test runner.

If this fails, the editable install or the interpreter selection is wrong --
see references/troubleshooting.md rather than adding sys.path hacks.
"""

import test_ev_setup


def test_package_imports():
    assert test_ev_setup.__version__
