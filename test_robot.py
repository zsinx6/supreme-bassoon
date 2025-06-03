from unittest import mock

import pytest

from robot import STANDARD, SPECIAL, REJECTED, _is_bulky, _is_heavy, sort


def test_string_values():
    assert STANDARD == "STANDARD"
    assert SPECIAL == "SPECIAL"
    assert REJECTED == "REJECTED"


@pytest.mark.parametrize(
    "width, height, length, is_bulky",
    [
        (1, 1, 1, False),
        (1, 1, 150, True),
        (150, 1, 1, True),
        (1, 150, 1, True),
        (100, 100, 100, True),
        (99.9999, 100, 100, False),
    ],
)
def test__is_bulky(width, height, length, is_bulky):
    assert _is_bulky(width, height, length) == is_bulky


@pytest.mark.parametrize(
    "mass, is_heavy",
    [
        (1, False),
        (19, False),
        (19.9, False),
        (20, True),
        (100, True),
    ],
)
def test__is_heavy(mass, is_heavy):
    assert _is_heavy(mass) == is_heavy


@pytest.mark.parametrize(
    "width, height, length, mass, stack_name",
    [
        (1, 1, 1, 1, STANDARD),
        (1, 1, 150, 1, SPECIAL),
        (1, 1, 1, 20, SPECIAL),
        (1, 1, 200, 20, REJECTED),
    ],
)
def test_sort_with_values(width, height, length, mass, stack_name):
    assert sort(width, height, length, mass) == stack_name


@pytest.mark.parametrize(
    "is_bulky_return, is_heavy_return, expected",
    [
        (False, False, STANDARD),
        (True, False, SPECIAL),
        (False, True, SPECIAL),
        (True, True, REJECTED),
    ],
)
def test_sort_rules(is_bulky_return, is_heavy_return, expected):
    with mock.patch("robot._is_bulky", return_value=is_bulky_return):
        with mock.patch("robot._is_heavy", return_value=is_heavy_return):
            assert sort(None, None, None, None) == expected
