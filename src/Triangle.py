from math import sqrt

from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        super().__init__()
        Figure.value_validator(side_a)
        Figure.value_validator(side_b)
        Figure.value_validator(side_c)
        if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
            raise ValueError("Triangle with given sides does not exist")
        self._name = "Triangle"
        self._side_a = side_a
        self._side_b = side_b
        self._side_c = side_c

    @property
    def perimeter(self):
        return self._side_a + self._side_b + self._side_c

    @property
    def area(self):
        p = self.perimeter / 2
        return sqrt(p * (p - self._side_a) * (p - self._side_b) * (p - self._side_c))
