# Uses python2


def get_fibonacci_last_digit(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    fib = [0, 1, 1]

    for i in xrange(2, n):
        fib.append((fib[i] + fib[i-1]) % 10)

    return fib[n]

"""
def test():
    print get_fibonacci_last_digit(327305)
"""


if __name__ == u'__main__':
    n = int(input())
    print get_fibonacci_last_digit(n)
    #print timeit.timeit(test, number=1)


