from math import sqrt


def is_prime(func):
    def wrapper(*args):
        n = func(*args)
        prime = True
        if n < 2:
            prime = False
        else:
            for i in range(2, int(sqrt(n)) + 1):
                if n % i == 0:
                    prime = False
                    break
        if prime:
            print("Простое")
        else:
            print("Составное")
        return n

    return wrapper


@is_prime
def sum_three(*numbers):
    total = 0
    for x in numbers:
        total += x
    return total


result = sum_three(2, 3, 6)
print(result)
