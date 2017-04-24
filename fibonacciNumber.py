# python3
def fibonacci(n):
    a = 0
    b = 1
    result = 0

    if n == 0:
        return result
    elif n == 1:
        result = 1
        return result
    else:
        result = 1
        for x in range(2, n):
            a = b
            b = result
            result = a+b
        return result

n = int(input())
r = fibonacci(n)
print(r)
