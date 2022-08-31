# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections
n = int(input())
myDict = collections.OrderedDict()
for i in range(n):
    string = str(input())
    if string in myDict:
        myDict[string] += 1
    else:
        myDict[string] = 1
print(len(myDict))
s = ""
for i in myDict:
    s += str(myDict[i]) + " "
print(s)