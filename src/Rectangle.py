from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        super().__init__()
        Figure.value_validator(side_a)
        Figure.value_validator(side_b)
        self._name = "Rectangle"
        self._side_a = side_a
        self._side_b = side_b

    @property
    def perimeter(self):
        return 2 * (self._side_a + self._side_b)

    @property
    def area(self):
        return self._side_a * self._side_b
