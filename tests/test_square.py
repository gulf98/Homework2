import pytest

from src.Square import Square


def test_name_check():
    square = Square(3)
    assert square.name == "Square"


@pytest.mark.parametrize("side_a", [2.5, 10])
def test_perimeter_check(side_a):
    square = Square(side_a)
    expected_perimeter = 4 * side_a
    assert square.perimeter == expected_perimeter


@pytest.mark.parametrize("side_a", [2.5, 10])
def test_area_check(side_a):
    square = Square(side_a)
    expected_area = side_a ** 2
    assert square.area == expected_area


@pytest.mark.parametrize("side_a", [-1, 0, "2", None, "", " "])
def test_invalid_sides(side_a):
    with pytest.raises(ValueError):
        Square(side_a)
