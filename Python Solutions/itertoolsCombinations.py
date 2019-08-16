# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
given = list(map(str, input().split()))
string = given[0]
size = int(given[1])
final = list()
for j in range(1,size+1):
    temp = list()
    for i in combinations(string,j):
        iss = ""
        ij = sorted(i, key=str.upper)
        for j in range(len(ij)):
            iss += ij[j]
        temp.append(iss)
        temp = sorted(temp, key=str.upper)
    final.append(temp)
for i in final:
    for j in range(len(i)):
        print(i[j])