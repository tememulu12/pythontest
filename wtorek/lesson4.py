import operator
import itertools

miesiace = [10, 8, 5, 7, 12, 10, 5, 8, 15, 3, 4, 2]
print(list(itertools.accumulate(miesiace, operator.add)))

a = range(3)
b = range(5)
c = [a, b]
print(list(itertools.chain(a, b)))
print(list(itertools.chain.from_iterable(c)))
print(list(itertools.compress(range(1000), [0, 1, 1, 1, 0, 1])))

primes = [0, 0, 1, 1, 0, 1, 0, 1]
numbers = ['zero', 'jeden', 'dwa', 'trzy', 'cztery', 'pięć']

print(list(itertools.compress(numbers, primes)))

print(list(itertools.islice(itertools.count(), 10)))
print(list(itertools.islice(itertools.count(), 5, 10, 2)))
print(list(itertools.islice(itertools.count(10, 2.5), 5)))

words = ['aa', 'ab', 'ba', 'bb', 'ca', 'cb', 'cc']
getter = operator.itemgetter(0)
for group, items in itertools.groupby(words, key=getter):
    print(f'group:{group}, items:{list(items)}')
