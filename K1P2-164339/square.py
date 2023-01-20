from Parallelogram import Parallelogram


class Square(Parallelogram):
    __color: str

    def __init__(self, side: float, color: str, side_1: float, side_2: float, angle: float):
        super().__init__(side_1, side_2, angle)
        if side > 100:
            print("złe parametry")
        if side < 0:
            print("złe parametry")
        self.__color = color
        self.__side = side

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, value: str) -> None:
        self.__color = value

    @property
    def side(self) -> float:
        return self.__side

    @side.setter
    def side(self, value: float) -> None:
        self.__side = value

    def generete_squares(self, other):
        pass

    def __repr__(self):
        return "długosc boku = " + str(self.side) + ", kolor = " + str(self.color) + ", obwod = " \
               + str(self.parimeter(self.side, self.side))
