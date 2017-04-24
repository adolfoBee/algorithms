# Uses python3

def optimal_weight(W, w):

    n = len(w)
    matrix = [[0 for x in range(W+1)] for y in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, W+1):
            matrix[i][j] = matrix[i-1][j]
            if w[i-1] <= j:
                val = w[i-1] + matrix[i-1][j-w[i-1]]
                if matrix[i][j] < val:
                    matrix[i][j] = val

    return matrix[n][W]

W, n = map(int, input().split())
w = list(map(int, input().split()))

print(optimal_weight(W, w))