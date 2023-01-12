import json
import functools
import collections
import operator


def tree():
    return collections.defaultdict(tree)


def lookup(tree, path):
    path = path.split('.')
    return functools.reduce(operator.getitem, path, tree)


drzewo = tree()
imiona = drzewo['T']['K']['N']
imiona['Tomasz']['Krzysztof']['Natalia'] = ['23', '44', '54']
# print(json.dumps(drzewo, indent=4))


path = 'T.K.N.Tomasz.Krzysztof'
print(dict(lookup(drzewo, path)))
print(lookup(drzewo, path).keys())
