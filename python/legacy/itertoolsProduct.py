# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

given = list(map(str,input().split()))
#print(given)
given[1] = int(given[1])
#print(type(given[1]))
#print(list(permutations(given[0],given[1])))
permuts = list(permutations(given[0], given[1]))
compiled = list()
for i in range(len(permuts)):
    string = ""
    for j in range(len(permuts[i])):
    #print(permuts[i])
        string += (permuts[i][j])
    compiled.append(string)
    string = ""
    #print(compiled[i])
final = sorted(compiled, key=str.lower)
for i in range(len(final)):
    print(final[i])
