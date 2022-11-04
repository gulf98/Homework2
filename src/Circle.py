import math

from src.Figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        Figure.value_validator(radius)
        self._name = "Circle"
        self._radius = radius

    @property
    def perimeter(self):
        return 2 * math.pi * self._radius

    @property
    def area(self):
        return math.pi * self._radius ** 2
