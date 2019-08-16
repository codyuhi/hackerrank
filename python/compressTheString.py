# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
s = input()
# print(s)
groups = []
uniquekeys = []
for k, g in groupby(s,int):
    groups.append(list(g))
    uniquekeys.append(k)
# print(groups)
# print(uniquekeys)
final = list()
string = ""
for i in groups:
    if string != "":
        string += " "
    string += "(" + str(len(i)) + ", " + i[0] + ")"
#     final.append((len(i),i[0]))
# print(final)
print(string)