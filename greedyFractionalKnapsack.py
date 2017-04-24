# Uses python3

def get_optimal_value(n, capacity, values, weights):
    value = 0.
    maxV = 0
    realvalue = []

    for i in range(0, n):
        v = values[i]/weights[i]
        realvalue.append(v)

    while capacity > 0 and realvalue:
        for y in range(0, len(realvalue)):
            if realvalue[y] > maxV:
                maxV = realvalue[y]

        for x in range(0, n):

            val = values[x]/weights[x]
            if val == maxV:
                if weights[x] > capacity:
                    p = capacity/weights[x]
                    value += values[x]*p
                    capacity -= weights[x]*p
                else:
                    value += values[x]
                    capacity -= weights[x]

        realvalue.remove(maxV)
        maxV = 0
    return value


if __name__ == "__main__":
    n, W = map(int, input().split())
    v = []  # Vector of values
    w = []  # Vector of weights

    for k in range(0, n):
        x, y = map(int, input().split())
        v.append(x)
        w.append(y)

    print(get_optimal_value(n, W, v, w))
