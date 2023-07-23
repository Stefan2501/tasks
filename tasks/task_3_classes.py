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
    BASE_UNIT = "m"

    def __init__(self, value):
        self._value = value

    def to_base_units(self):
        return self._value * self._factor

    def __str__(self):
        return f"{self._value} {self.__class__.__name__}"

    def __eq__(self, other):
        if isinstance(other, LengthUnits):
            other = other.to_base_units()
        elif isinstance(other, (int, float)):
            other = other * self._factor
        else:
            return NotImplemented

        return self.to_base_units() == other

    def __lt__(self, other):
        if isinstance(other, LengthUnits):
            other = other.to_base_units()
        elif isinstance(other, (int, float)):
            other = other * self._factor
        else:
            raise ValueError("Cannot compare different types of length units")

        return self.to_base_units() < other

    def __add__(self, other):
        if isinstance(other, LengthUnits):
            other = other.to_base_units()
        elif isinstance(other, (int, float)):
            other = other * self._factor
        else:
            return NotImplemented

        result = self.to_base_units() + other
        return self.__class__(result / self._factor)

    def __iadd__(self, other):
        if isinstance(other, LengthUnits):
            other = other.to_base_units()
        elif isinstance(other, (int, float)):
            other = other * self._factor
        else:
            return NotImplemented

        self._value += other / self._factor
        return self

    def __sub__(self, other):
        if isinstance(other, LengthUnits):
            other = other.to_base_units()
        elif isinstance(other, (int, float)):
            other = other * self._factor
        else:
            return NotImplemented

        result = self.to_base_units() - other
        return self.__class__(result / self._factor)

    def __isub__(self, other):
        if isinstance(other, LengthUnits):
            other = other.to_base_units()
        elif isinstance(other, (int, float)):
            other = other * self._factor
        else:
            return NotImplemented

        self._value -= other / self._factor
        return self

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = self._value * other
            return self.__class__(result)
        else:
            return NotImplemented

    def __imul__(self, other):
        if isinstance(other, (int, float)):
            self._value *= other
            return self
        else:
            return NotImplemented

    def __div__(self, other):
        if isinstance(other, (int, float)):
            result = self._value / other
            return self.__class__(result)
        elif isinstance(other, LengthUnits):
            result = self._value / (other.to_base_units() / self._factor)
            return result
        else:
            return NotImplemented

    def __idiv__(self, other):
        if isinstance(other, (int, float)):
            self._value /= other
            return self
        elif isinstance(other, LengthUnits):
            self._value /= other.to_base_units() / self._factor
            return self
        else:
            return NotImplemented


class Millimeters(LengthUnits):
    _factor = 0.001


class Centimeters(LengthUnits):
    _factor = 0.01


class Meters(LengthUnits):
    _factor = 1


class Kilometers(LengthUnits):
    _factor = 1000


class Inches(LengthUnits):
    _factor = 0.0254


class Feets(LengthUnits):
    _factor = 0.3048


class Yards(LengthUnits):
    _factor = 0.9144


class Miles(LengthUnits):
    _factor = 1609.34


class Fen(LengthUnits):
    _factor = 0.1


class Chi(LengthUnits):
    _factor = 0.33


class In(LengthUnits):
    _factor = 0.0254
