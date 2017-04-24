# Uses python3
import math

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    m = right/2
    b = get_majority_element(a, left, m)
    c = get_majority_element(a, m, right)

    return -1

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(get_majority_element(a, 0, n))
