import pytest

from src.Rectangle import Rectangle


def test_name_check():
    rectangle = Rectangle(1, 2)
    assert rectangle.name == "Rectangle"


@pytest.mark.parametrize("side_a, side_b", [
    (2.5, 3.5),
    (10, 20),
    (2.5, 10)
])
def test_perimeter_check(side_a, side_b):
    rectangle = Rectangle(side_a, side_b)
    expected_perimeter = 2 * (side_a + side_b)
    assert rectangle.perimeter == expected_perimeter


@pytest.mark.parametrize("side_a, side_b", [
    (2.5, 3.5),
    (10, 20),
    (2.5, 10)
])
def test_area_check(side_a, side_b):
    rectangle = Rectangle(side_a, side_b)
    expected_area = side_a * side_b
    assert rectangle.area == expected_area


@pytest.mark.parametrize("side_a, side_b", [
    (-1, 2),
    (2, 0),
    (2, None),
    ("10", 2),
    (2, ""),
    (" ", 2)
])
def test_invalid_sides(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)
