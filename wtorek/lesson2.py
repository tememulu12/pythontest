import functools
import operator
from operator import mul

print(functools.reduce(operator.mul, range(1,5)))
print(lambda a,b: a*b)

print(mul(mul(mul(1,2),3),4))