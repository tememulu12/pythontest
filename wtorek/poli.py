class Car:

    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        self.__predkosc = 0

    def gaz(self):
        self.__predkosc += 10
        self.__zmien_bieg()

    def hamuj(self):
        self.__predkosc -= 10

    def licznik(self):
        print(self.__predkosc)

    def __zmien_bieg(self):
        print("Zmiana biegu!")


c = Car('BMW', 2000, 'BLACK')
c.gaz()
c.gaz()
c.gaz()
c.gaz()
c.licznik()
c.hamuj()
c.hamuj()
c.hamuj()
c.hamuj()
c.hamuj()
c.licznik()
