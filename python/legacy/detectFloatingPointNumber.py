n = int(input())
for i in range(n):
    string = input()
    try:
        float(string)
        if string == '0':
            print(False)
        else:
            print(True)
    except:
        print(False)