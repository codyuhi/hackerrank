def wrapper(f):
    def fun(l):
        # complete the function
        l = sorted(l)
        for i in range(len(l)):
            if len(l[i]) == 10:
                # print("+91 " + str(i)[:5] + " " + str(i)[5:])
                l[i] = "+91 " + l[i][:5] + " " + l[i][5:]
            elif len(l[i]) == 11:
                # print("+91 " + str(i)[1:6] + " " + str(i)[6:])
                l[i] = "+91 " + l[i][1:6] + " " + l[i][6:]
            elif len(l[i]) == 12:
                # print("+" + str(i)[:2] + " " + str(i)[2:7] + " " + str(i)[7:])
                l[i] = "+" + l[i][:2] + " " + l[i][2:7] + " " + l[i][7:]
            else:
                # print(str(i)[:3] + " " + str(i)[3:8] + " " + str(i)[8:])
                l[i] = l[i][:3] + " " + l[i][3:8] + " " + l[i][8:]
        l = sorted(l)
        print(*l, sep="\n")
        return 0
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
