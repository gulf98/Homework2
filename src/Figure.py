class Figure:

    def __init__(self):
        self._name = "Figure"

    @staticmethod
    def value_validator(value):
        if type(value) != int and type(value) != float:
            raise ValueError("Переданный параметр должен быть числом")
        if value <= 0:
            raise ValueError("Переданный параметр должен быть больше нуля")

    @property
    def name(self):
        return self._name

    @property
    def perimeter(self):
        return 0

    @property
    def area(self):
        return 0

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("Переданный объект должен быть геометрической фигурой")
        return self.area + figure.area
