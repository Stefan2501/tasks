'''
Задание 3.
Классы. Наследование, волшебные методы.
'''


# Необходимо реализовать семейство классов, обеспечивающих прозрачную работу с такими единицами
# измерения, как миллиметры, сантиметры, метры, километры, дюймы, футы, ярды, фэнь, чи и инь.
# Требуется реализовать метод __str__, который будет возвращать текущее значение и единицу измерения,
# например "1 км", "2.35 мили" и т. д.
# Требуется реализовать методы __eq__ и __lt__ для сравнения любых единиц измерения между собой.
# Требуется реализовать методы __add__, __iadd__, __sub__ и __isub__, принимающие в качестве
# аргумента любой класс единиц, а также просто число. Если в качестве аргумента выступает число,
# то оно трактуется, как количество текущих единиц измерения.
# Требуется реализовать методы __mul__ и __imul__, принимающие числовое значение в качестве аргумента.
# Требуется реализовать методы __div__ и __idiv__, принимающие как числовое значение, так и любой класс
# единиц измерения. В случае, если в качестве аргумента выступает числовое значение, то результат
# возвращается в тех же единицах измерения, что и текущая. В остальных случаях возвращается число.
# Требуется добавить способ конвертации из одной системы единиц в другую (желательно с использованием
# __init__.
# Необходимо выбрать базовую единицу измерения, к которой во время выполнения операций будут
# приводиться все значения. Ее же использовать и в базовом классе. Практически вся функциональность
# реализуется в базовом классе. Иерархию наследования можно сделать двухуровневой, задача подходит
# для этого.


class LengthUnits:
    _BASE_UNIT = "m"
    _FACTOR = 1

    def __init__(self, value):
        if isinstance(value, LengthUnits):
            self._value = value._to_base_units()
        elif isinstance(value, (int, float)):
            self._value = value
        else:
            raise ValueError("Invalid value type")

    def _to_base_units(self):
        return self._value * self._FACTOR

    def __str__(self):
        return f"{self._value / self._FACTOR} {self._BASE_UNIT}"

    def __eq__(self, other):
        if isinstance(other, LengthUnits):
            other = other._value
        elif isinstance(other, (int, float)):
            other *= self._FACTOR
        else:
            raise TypeError("Unsupported operand type for equality comparison")

        return self._value == other

    def __lt__(self, other):
        if isinstance(other, LengthUnits):
            other = other._value
        elif isinstance(other, (int, float)):
            other *= self._FACTOR
        else:
            raise TypeError("Unsupported operand type for less than comparison")

        return self._value < other

    def __add__(self, other):
        if isinstance(other, LengthUnits):
            other = other._value
        elif isinstance(other, (int, float)):
            other *= self._FACTOR
        else:
            raise TypeError("Unsupported operand type for addition")

        result = self._value + other
        return self.__class__(result / self._FACTOR)

    def __iadd__(self, other):
        if isinstance(other, LengthUnits):
            other = other._value
        elif isinstance(other, (int, float)):
            other *= self._FACTOR
        else:
            raise TypeError("Unsupported operand type for addition")

        self._value += other
        return self._value == other

    def __sub__(self, other):
        if isinstance(other, LengthUnits):
            other = other._value
        elif isinstance(other, (int, float)):
            other *= self._FACTOR
        else:
            raise TypeError("Unsupported operand type for subtraction")

        return self.__class__((self._value - other) / self._FACTOR)

    def __isub__(self, other):
        if isinstance(other, LengthUnits):
            other = other._value
        elif isinstance(other, (int, float)):
            other *= self._FACTOR
        else:
            raise TypeError("Unsupported operand type for in-place subtraction")

        self._value -= other
        return self

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(self._value * other)
        raise TypeError("Unsupported operand type for multiplication")

    def __imul__(self, other):
        if isinstance(other, (int, float)):
            self._value *= other
            return self
        raise TypeError("Unsupported operand type for multiplication")

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            result = self._value / other
            return self.__class__(result)
        raise TypeError("Unsupported operand type for division")

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            self._value /= other
            return self
        raise TypeError("Unsupported operand type for division")


class Millimeters(LengthUnits):
    _FACTOR = 0.001


class Centimeters(LengthUnits):
    _FACTOR = 0.01


class Meters(LengthUnits):
    _FACTOR = 1


class Kilometers(LengthUnits):
    _FACTOR = 1000


class Inches(LengthUnits):
    _FACTOR = 0.0254


class Feets(LengthUnits):
    _FACTOR = 0.3048


class Yards(LengthUnits):
    _FACTOR = 0.9144


class Miles(LengthUnits):
    _FACTOR = 1609.34


class Fen(LengthUnits):
    _FACTOR = 0.1


class Chi(LengthUnits):
    _FACTOR = 0.33


class In(LengthUnits):
    _FACTOR = 0.0254
