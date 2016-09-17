# Uses python3


def optimal_weight(W, w):
    # Init result
    result = [0] * W
    last = [0] * W

    # Looping over bars
    for bar in w:
        # Looping over the weights
        for idx, wei in enumerate(result):
            if idx >= bar:
                result[idx] = max(wei, bar + (last[idx-bar]))
        last = result[:]



    return result[-1]






if __name__ == '__main__':
    input1 = input()
    input2 = input()
    input = "".join([input1, " ", input2])

    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))

    #print(optimal_weight(10, [1, 4, 8]))
