if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    myList = list(integer_list)
    t = tuple()
    #print(n)
    for i in range(n):
        x = myList[i]
        t += (x,)
    print(hash(t))


