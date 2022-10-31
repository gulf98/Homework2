from math import sqrt

import pytest

from src.Triangle import Triangle


def test_name_check():
    rectangle = Triangle(10, 13, 15)
    assert rectangle.name == "Triangle"


@pytest.mark.parametrize("side_a, side_b, side_c", [
    (10, 12, 13),
    (2.5, 3.5, 4.1)
])
def test_perimeter_check(side_a, side_b, side_c):
    rectangle = Triangle(side_a, side_b, side_c)
    expected_perimeter = side_a + side_b + side_c
    assert rectangle.perimeter == expected_perimeter


@pytest.mark.parametrize("side_a, side_b, side_c", [
    (10, 12, 13),
    (2.5, 3.5, 4.1)
])
def test_area_check(side_a, side_b, side_c):
    rectangle = Triangle(side_a, side_b, side_c)
    p = (side_a + side_b + side_c) / 2
    expected_area = sqrt(p * (p - side_a) * (p - side_b) * (p - side_c))
    assert rectangle.area == expected_area


@pytest.mark.parametrize("side_a, side_b, side_c", [
    (-10, 12, 13),
    (10, 0, 13),
    (10, 12, None),
    ("10", 12, 13),
    (10, "", 13),
    (10, 12, " "),
    (1000, 12, 13)
])
def test_invalid_sides(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)
