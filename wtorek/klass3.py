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
                f'{self.name!r}, {self.email!r})')


class Supplier(Contact):
    def order(self, order: "Order"):
        print(f"{order} zamówiono od {self.name}")


c_1 = Contact("Adam", 'tomasz@wp.pl')
c_2 = Contact("Andrzej", 'jakub@wp.pl')
c = Contact("Tomasz", 'tomasz@wp.pl')
s = Supplier("Jakub", 'jakub@wp.pl')
print(c.name, c.email, s.name, s.email)

pprint(c.all_contacts)
s.order('kawa raz!')
l = LongNameDict()
l['mulu'] = 200
l['pawel'] = 400
l['dax'] = 10
print(l.longest_key())
