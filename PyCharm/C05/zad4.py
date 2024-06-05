def isprime(x):
    if x < 2:
        return False
    for i in range(2, x-1):
        if x % i == 0:
            return False
    return True


def primegenerator(n):
    i = 0
    number = 2
    while i < n:
        isprime(number)
        while not isprime(number):
            number += 1
        yield number
        number += 1
        i += 1


n = 4
primegen = primegenerator(n)
for i in range(n):
    print(next(primegen))
