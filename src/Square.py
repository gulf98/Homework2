from src.Figure import Figure


class Square(Figure):
    def __init__(self, side_a):
        super().__init__()
        Figure.value_validator(side_a)
        self._name = "Square"
        self._side_a = side_a

    @property
    def perimeter(self):
        return 4 * self._side_a

    @property
    def area(self):
        return self._side_a ** 2
