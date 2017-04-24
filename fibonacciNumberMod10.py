# python3
def fibonacci(n):
    a = 0
    b = 1
    result = 1

    if n <= 1:
        return n
    else:
        for x in range(2, n):
            a = b
            b = result
            result = (a + b) % 10
        return result

n = int(input())
r = fibonacci(n)
print(r)

