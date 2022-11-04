import math
import pytest

from src.Circle import Circle


def test_name_check():
    circle = Circle(4)
    assert circle.name == "Circle"


@pytest.mark.parametrize("radius", [2.5, 10])
def test_perimeter_check(radius):
    circle = Circle(radius)
    expected_perimeter = 2 * math.pi * radius
    assert circle.perimeter == expected_perimeter


@pytest.mark.parametrize("radius", [2.5, 10])
def test_area_check(radius):
    circle = Circle(radius)
    expected_area = math.pi * radius ** 2
    assert circle.area == expected_area


@pytest.mark.parametrize("radius", [-1, 0, "10", None, "", " "])
def test_invalid_radius(radius):
    with pytest.raises(ValueError):
        Circle(radius)
