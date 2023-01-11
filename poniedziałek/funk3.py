def generator_2():
    i =1
    while True:
        yield i*i
        i += 1

for num in generator_2():
    if num > 100:
        break
    print(num)

def fibo():
    a,b = 0,1
    while True:
        yield b
        a,b = b,a + b

fib = fibo()
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print("cos .....")
print(next(fib))
print(next(fib))
print("cos ....")