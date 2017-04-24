# Uses python3
import random


def partition3(a, l, h):
    key = a[l]
    m1 = l
    i = l
    m2 = h
    while i <= m2:
        if a[i] < key:
            a[m1], a[i] = a[i], a[m1]
            m1 += 1
            i += 1
        elif a[i] > key:
            a[m2], a[i] = a[i], a[m2]
            m2 -= 1
        else:
            i += 1

    return m1, m2


def randomized_quick_sort(a, l, h):
    if l >= h:
        return
    k = random.randint(l, h)
    a[l], a[k] = a[k], a[l]
    m1, m2 = partition3(a, l, h)
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1, h)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
