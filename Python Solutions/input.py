x,string = list(map(str,input().split())),input()
string = string.replace('x',str(x[0]))
if int(x[1]) == int(eval(string)):
    print(True)
else:
    print(False)