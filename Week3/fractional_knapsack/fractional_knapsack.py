# Uses python2


def get_optimal_value(capacity, weights, values):
    value = 0.
    #print "cap = " + str(capacity)
    #print "wei = " + str(weights)
    #print "val = " + str(values)

    cur_cap = capacity
    val_per_wei = [None]*weights.__len__()

    # calc val/wei for each item
    for i in xrange(len(values)):
        val_per_wei[i] = float(values[i]) / weights[i]

    # set the input as a double list: wei & (val / wei)
    data = zip(val_per_wei, values, weights)

    # sort the dict based on val / wei
    data.sort(key=lambda pair: pair[0], reverse=True)

    #print "vfw = " + str(val_per_wei)
    #print data

    for vpw, src_val, src_cap in data:
        # item can enter the bag as a whole
        if src_cap <= cur_cap:
            cur_cap -= src_cap
            value += src_val

        # item can enter the bag as a fraction
        elif cur_cap > 0:
            value += (cur_cap / float(src_cap)) * src_val
            cur_cap = 0

    return value


if __name__ == "__main__":
    #data = list(map(int, sys.stdin.read().split()))
    #n, capacity = data[0:2]
    #values = data[2:(2 * n + 2):2]
    #weights = data[3:(2 * n + 2):2]
    values = []
    weights = []

    n, capacity = list(map(int, raw_input().split()))
    for i in xrange(n):
        val, wei = list(map(int, raw_input().split()))
        values.append(val)
        weights.append(wei)

    opt_value = get_optimal_value(capacity, weights, values)
    #opt_value = get_optimal_value(50, [20, 50, 30], [60, 100, 120])
    print "{:.10f}".format(opt_value)
