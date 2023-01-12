import math


class MyFirstClass:

    def __init__(self, x, y):
        self.move(x, y)

    def reset(self):
        self.move(0, 0)

    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def calculate(self, other: "MyFirstClass") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)


a = MyFirstClass(4, 7)
b = MyFirstClass(8, 9)
print(a.x)
a.reset()
b.move(5, 0)
print(b.calculate(a))
assert b.calculate(a) == a.calculate(b)
a.move(3, 4)
print(a.calculate(b))
