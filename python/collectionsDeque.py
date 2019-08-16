# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
n = int(input())
for i in range(n):
    given = list(map(str,input().split()))
    if given[0] == "append":
        d.append(given[1])
    elif given[0] == "appendleft":
        d.appendleft(given[1])
    elif given[0] == "pop":
        d.pop()
    elif given[0] == "popleft":
        d.popleft()
c = int(0)
string = ""
for i in d:
    if c > 0:
        string += " "
    string += i
    c += 1
print(string)