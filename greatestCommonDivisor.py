# python3
def euclidGCD(a, b):
    if b == 0:
        return a
    else:
        return euclidGCD(b, (a % b))

a, b = map(int, input().split())
print(euclidGCD(a, b))
