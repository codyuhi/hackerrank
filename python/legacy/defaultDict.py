# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
d = defaultdict(list)
given = list(map(int, input().split()))
n = given[0]
m = given[1]
for i in range(n):
    d["n"].append(input())
for i in range(m):
    d["m"].append(input())
st = ""
k = 0
for i in range(m):
    for j in range(n):
        if d["m"][i] == d["n"][j]:
            if k > 0:
                st += ' '
            st += str(j+1)
            k += 1
    if k == 0:
        st += "-1"
    k = 0
    st += '\n'
print(st)
