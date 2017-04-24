# Uses python3

def get_change(m):
    count = 0
    while m > 0:
        if m >= 10:
            count += 1
            m -= 10
        elif m >= 5:
            count += 1
            m -= 5
        elif m >= 1:
            count += 1
            m -= 1
    return count

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
