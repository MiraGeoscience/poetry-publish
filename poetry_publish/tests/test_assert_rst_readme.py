"""
    :created: 1.2.2020 by Jens Diemer
    :copyleft: 2020 by the poetry-publish team
    :license: GNU GPL v3 or above, see LICENSE for more details.
"""

from pathlib import Path

import pytest

import poetry_publish


try:
    from creole.setup_utils import assert_rst_readme
except ModuleNotFoundError:
    pytest.skip("skipping: creole is not installed", allow_module_level=True)


PACKAGE_ROOT = Path(poetry_publish.__file__).parent.parent


def test_update_rst_readme(capsys):
    rest_readme_path = update_rst_readme(
        package_root=PACKAGE_ROOT, filename='README.creole'
    )
    captured = capsys.readouterr()
    assert captured.out == 'Generate README.rst from README.creole...nothing changed, ok.\n'
    assert captured.err == ''
    assert isinstance(rest_readme_path, Path)
    assert str(rest_readme_path).endswith('/README.rst')
