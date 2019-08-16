# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
import math

st = input().split()
x = ""
y = ""
found = False
for i in st[0]:
    if found == True and i != 'j':
        y += i
    if ((i != '+' and i != '-') and found == False) or (x == "" and i == '-'):
        x += i
    else:
        if i == '-':
            y += '-'
        found = True
x = int(x)
y = int(y)

print(math.sqrt(x**2 + y**2))
print(cmath.phase(complex(x,y)))
