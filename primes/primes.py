"""Return count number of prime numbers, starting at 2.

For example::

    >>> primes(0)
    []

    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]

"""

def is_prime(number):
    """Returns true or false if a number is prime"""

    mid = (number + number % 2) / 2

    for n in range(2, mid + 1):
        if not number % n:
            return False

    return True


def primes(count):
    """Return count number of prime numbers, starting at 2."""

    primes = []

    if count < 1:
        return primes

    num = 2

    while len(primes) < count:
        if is_prime(num):
            primes.append(num)
        num += 1

    return primes



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT WORK!\n"
