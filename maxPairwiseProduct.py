# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0
cont = 0
x = 0
y = 0

for i in range(0, n):
    if a[i] >= x:
        x = a[i]
        cont = i

for i in range(0, n):
    if a[i] >= y and i != cont:
        y = a[i]

result = x * y

print(result)
