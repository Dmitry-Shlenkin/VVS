size = 3


def draw(a, b, c, d, e, f, g):
    if a == 1:
        print(' ' + '*' * size + ' ')
    else:
        print()

    if f == 1 and b == 1:
        for i in range(size):
            print('*' + ' ' * size + '*')
    elif b == 1:
        for i in range(size):
            print(' ' + ' ' * size + '*')
    elif f == 1:
        for i in range(size):
            print('*' + ' ' * size + ' ')

    if g == 1:
        print(' ' + '*' * size + ' ')
    else:
        print()

    if e == 1 and c == 1:
        for i in range(size):
            print('*' + ' ' * size + '*')
    elif c == 1:
        for i in range(size):
            print(' ' + ' ' * size + '*')
    elif e == 1:
        for i in range(size):
            print('*' + ' ' * size + ' ')

    if d == 1:
        print(' ' + '*' * size + ' ')
    else:
        print()


def get(n):
    # a = ((n % 2) * (n % 3) * (n % 5) * (n % 6) * (n % 7) * (n % 8) * (n % 9))
    # b = ((n % 1) * (n % 2) * (n % 3) * (n % 4) * (n % 7) * (n % 8) * (n % 9))
    # c = ((n % 1) * (n % 3) * (n % 4) * (n % 5) * (n % 6) * (n % 7) * (n % 8) * (n % 9))
    # d = ((n % 2) * (n % 3) * (n % 5) * (n % 6) * (n % 8) * (n % 9))
    # e = ((n % 2) * (n % 6) * (n % 8))
    # f = ((n % 4) * (n % 5) * (n % 6) * (n % 8) * (n % 9))
    # g = ((n % 2) * (n % 3) * (n % 4) * (n % 5) * (n % 6) * (n % 8) * (n % 9))
    a = 1 - ((n % 1) * (n % 4))
    b = 1 - ((n % 5) * (n % 6))
    c = 1 - (n % 2)
    d = 1 - ((n % 1) * (n % 4) * (n % 7))
    e = 1 - ((n % 1) * (n % 3) * (n % 4) * (n % 5) * (n % 7) * (n % 9))
    f = 1 - ((n % 1) * (n % 2) * (n % 3) * (n % 7))
    g = 1 - ((n % 1) * (n % 7))
    print(a, b, c, d, e, f, g)
    return a, b, c, d, e, f, g


if __name__ == '__main__':
    for i in range(10):
        print(str(i) + ':')
        (a, b, c, d, e, f, g) = get(i)
        draw(a, b, c, d, e, f, g)
        print()

# draw(0, 1, 1, 0, 0, 0, 0)
# print()
# draw(1, 1, 0, 1, 1, 0, 1)
