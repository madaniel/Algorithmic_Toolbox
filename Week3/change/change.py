# Uses python2
import sys


def get_change(m):
    coins = [10, 5, 1]
    count = 0
    num = int(m)

    while num > 0:
        for coin in coins:
            # num matches the coin exactly
            if num % coin == 0:
                count += (num / coin)
                num -= num
            # num matches the coin but with change
            if num / coin > 0:
                count += (num / coin)
                num -= (num / coin) * coin
            # num > coin

    return count

if __name__ == "__main__":
    m = raw_input()
    print get_change(m)
