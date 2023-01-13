from __future__ import annotations
from pprint import pprint


class ContactList(list['Contact']):
    def search(self, name):
        matching_contacts = []
        for c in self:
            if name in c.name:
                matching_contacts.append(c)
        return matching_contacts


class LongNameDict(dict[str, int]):
    def longest_key(self):
        longest = None
        for key in self:
            if longest is None or len(key) > len(longest):
                longest = key
        return longest


class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.name!r}, {self.email!r},)')


class Supplier(Contact):
    def order(self, order: "Order"):
        print(f"{order} zamówiono od {self.name}")


class Friend(Supplier, Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.name!r}, {self.email!r} +48 {self.phone!r})')


c_1 = Contact("Adam", 'tomasz@wp.pl')
c_2 = Contact("Andrzej", 'jakub@wp.pl')
c = Contact("Tomasz", 'tomasz@wp.pl')
s = Supplier("Jakub", 'jakub@wp.pl')
f = Friend("Jarek", "jarek@wp.pl", '56325987')
print(c.name, c.email, s.name, s.email)

pprint(c.all_contacts)
s.order('kawa raz!')
print([c.name for c in Contact.all_contacts.search('Tomasz')])

artykuly = LongNameDict()
artykuly['tomasz'] = 12
artykuly['Abraham'] = 212
artykuly['tom'] = 2
print(artykuly.longest_key())
print(Friend.__mro__)
