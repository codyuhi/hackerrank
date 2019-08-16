if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        given = input()
        givenArr = given.split()
        if(givenArr[0] == "insert"):
            arr.insert(int(givenArr[1]),int(givenArr[2]))
        elif(givenArr[0] == "print"):
            print(arr)
        elif(givenArr[0] == "remove"):
            arr.remove(int(givenArr[1]))
        elif(givenArr[0] == "append"):
            arr.append(int(givenArr[1]))
        elif(givenArr[0] == "sort"):
            arr.sort()
        elif(givenArr[0] == "pop"):
            arr.pop()
        elif(givenArr[0] == "reverse"):
            arr.reverse()