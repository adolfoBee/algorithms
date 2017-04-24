# Uses python3

def optimal_sequence(n):
    solution = [0]*(n+1)
    sequence = [0]*(n+1)
    for j in range(2, n+1):
        solution[j] = solution[j-1] + 1
        sequence[j] = 1
        if j % 3 == 0:
            if j == 3:
                solution[j] = 1
                sequence[j] = 3
            else:
                if 1 + solution[(j // 3)] <= solution[j]:
                    sequence[j] = 3
                else:
                    sequence[j] = 1
                solution[j] = min(1 + solution[j // 3], solution[j])
        elif j % 2 == 0:
            if j == 2:
                solution[j] = 1
                sequence[j] = 2
            else:
                if 1 + solution[(j // 2)] <= solution[j]:
                    sequence[j] = 2
                else:
                    sequence[j] = 1
                solution[j] = min(1 + solution[(j // 2)], solution[j])

    print(solution[len(solution)-1])
    final = []
    m = n
    y = n
    final.append(m)
    while y >= 1:
        if sequence[y] == 1:
            final.insert(0, m - 1)
            y -= 1
            m -= 1
        elif sequence[y] == 2:
            final.insert(0, m // 2)
            m = m // 2
            y = m
        elif sequence[y] == 3:
            final.insert(0, m // 3)
            m = m // 3
            y = m
        else:
            y -= 1
    for x in final:
        print(x, end=' ')
    print("\n")

n = int(input())
optimal_sequence(n)
