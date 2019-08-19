cube = lambda x: x * x * x

def fibonacci(n):
    # return a list of fibonacci numbers
    l = []
    for i in range(n):
        if i != 1 and i != 0:
            l.append(l[len(l) - 2] + l[len(l)-1])
        elif i == 0:
            l.append(0)
        elif i == 1:
            l.append(1)
    return l


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))