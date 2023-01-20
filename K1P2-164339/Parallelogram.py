from math import sin


class Parallelogram:
    __side_1: float
    __side_2: float
    __angle: float

    def __init__(self, side_1: float, side_2: float, angle: float) -> None:
        if side_1 > 100:
            print("złe parametry")
        if side_1 < 0:
            print("złe parametry")
        if side_2 > 100:
            print("złe parametry")
        if side_1 < 0:
            print("złe parametry")
        self.__side_1 = side_1
        self.__side_2 = side_2
        self.__angle = angle

    def area(self, side_1, side_2, angle) -> float:
        area = sin(angle)*side_1*side_2
        return area

    def parimeter(self, side_1, side_2) -> float:
        parimeter = 2*side_1 + 2*side_2
        return parimeter

    def duplicate_with_scale(self, side_1, side_2, angle):
        scale: int
        if scale > 10:
            print("złe parametry")
            return -2
        if scale < 0:
            print("złe parametry")
            return -2
        dup_scale = Parallelogram(scale*side_1, scale * side_2, angle)
        return dup_scale

    def __repr__(self) -> str:
        return str(self.__side_1) + " " + str(self.__side_2) + " " + str(self.__angle)

    def __add__(self, other):
        if self.__angle > other.__angle:
            new_angle = self.__angle
        new_angle = other.__angle
        new = Parallelogram(self.__side_1 + other.__side_1, self.__side_2 + other.__side_2, new_angle)
        return new
