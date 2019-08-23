# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
valid = False
for i in range(n):
    string = input()
    if re.search(r'{',string):
        valid = True
        continue
    if re.search(r'}',string):
        valid = False
        continue
    if not valid:
        continue
    m = re.findall(r'#([0123456789abcdefABCDEF]{6}|[0123456789abcdefABCDEF]{3})',string)
    try:
        for j in m:
            print('#'+str(j))
    except:
        continue