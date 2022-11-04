import pytest

from src.Circle import Circle
from src.Figure import Figure
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


@pytest.mark.parametrize("figure1, figure2", [
    (Circle(5), Circle(10)),
    (Circle(5), Rectangle(10, 20)),
    (Circle(5), Square(10)),
    (Circle(5), Triangle(10, 12, 13)),
    (Circle(5), Figure()),
    (Rectangle(10, 20), Circle(10)),
    (Rectangle(10, 20), Rectangle(10, 20)),
    (Rectangle(10, 20), Square(10)),
    (Rectangle(10, 20), Triangle(10, 12, 13)),
    (Rectangle(10, 20), Figure()),
    (Square(10), Circle(10)),
    (Square(10), Rectangle(10, 20)),
    (Square(10), Square(10)),
    (Square(10), Triangle(10, 12, 13)),
    (Square(10), Figure()),
    (Triangle(10, 12, 13), Circle(10)),
    (Triangle(10, 12, 13), Rectangle(10, 20)),
    (Triangle(10, 12, 13), Square(10)),
    (Triangle(10, 12, 13), Triangle(10, 12, 13)),
    (Triangle(10, 12, 13), Figure()),
    (Figure(), Circle(10)),
    (Figure(), Rectangle(10, 20)),
    (Figure(), Square(10)),
    (Figure(), Triangle(10, 12, 13)),
    (Figure(), Figure()),
])
def test_figure_with_figure(figure1, figure2):
    actual_value = figure1.add_area(figure2)
    expected_value = figure1.area + figure2.area
    assert actual_value == expected_value


@pytest.mark.parametrize("figure, invalid_object", [
    (Circle(5), 10),
    (Rectangle(10, 20), "10"),
    (Square(10), None),
    (Triangle(10, 12, 13), ""),
    (Figure(), object),
])
def test_figure_with_invalid_object(figure, invalid_object):
    with pytest.raises(ValueError):
        figure.add_area(invalid_object)
