from abc import ABC, abstractmethod


class Counter(ABC):
    def __init__(self, value=0):
        self._value = value

    def increment(self, by=1):
        self._value += by

    @staticmethod
    def format_string():
        return "%d"

    @classmethod
    def from_other(cls, counter):
        return cls(counter._value)

    @abstractmethod
    def drukuj(self):
        print("Drukuje....")


class BoundedCounter(Counter):
    MAX = 100

    def __init__(self, value=0):
        if value > self.MAX:
            raise ValueError("Wartośc nie może przekroczyć MAX")
        super(BoundedCounter, self).__init__(value)

    def increment(self, by=1):
        super(BoundedCounter, self).increment(by)
        self._value = min(self._value, self.MAX)

    def drukuj(self):
        print("Drukuje....")

    @classmethod
    def from_other(cls, counter):
        value = min(counter._value, cls.MAX)
        return cls(value)


# c = Counter()
# c.increment(4)
# Counter.format_string()
# Counter().format_string()
b = BoundedCounter()
b.increment(10)
BoundedCounter.from_other(b)
