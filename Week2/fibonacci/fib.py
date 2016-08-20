# Uses python2
import timeit

"""
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)
"""
def calc_fib(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    result = 2

    fib = [1, 1, 2]

    for i in xrange(2, n):
        fib.append(fib[i] + fib[i-1])

    return fib[n]

n = int(input())
print calc_fib(n)


"""
def test():
    print calc_fib_2(45)
"""



#n = int(raw_input())

#print timeit.timeit(test, number=1)


