import pickle
from k7 import Person

with open('data.pickle', 'rb') as stream:
    p = pickle.load(stream)

for person in p:
    person.greet()