import pickle
from dataclasses import dataclass


@dataclass
class Person:
    first_name: str
    last_name: str
    id: int

    def greet(self):
        print(f"Witam, jestem {self.first_name} {self.last_name}, moje ID to {self.id}")

people = [
    Person('pawel', 'michalik', 2),
    Person('mulu', 'fent', 3)
]
with open('data.pickle', 'wb') as stream:
    pickle.dump(people, stream)


