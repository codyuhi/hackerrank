if __name__ == '__main__':
    L1 = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        L2 = [name, score]
        L1.append(L2)
    lowest = -1000.0
    secLowest = -1000.0
    for i in range(len(L1)):
        if i == 0:
            lowest = L1[i][1]
        elif i == 1:
            if lowest < L1[i][1]:
                secLowest = L1[i][1]
            elif lowest > L1[i][1]:
                secLowest = lowest
                lowest = L1[i][1]   
        elif lowest > L1[i][1]:
            secLowest = lowest
            lowest = L1[i][1]
        elif secLowest > L1[i][1] and L1[i][1] != lowest:
            secLowest = L1[i][1]
        elif secLowest == -1000.0 and lowest != L1[i][1]:
            secLowest = L1[i][1]L2 = []
    for i in range(len(L1)):
        if secLowest == L1[i][1]:
            L2.append(L1[i][0])
    if len(L2) > 1:
        L2.sort()
    for i in range(len(L2)):
        print(L2[i])

    
            