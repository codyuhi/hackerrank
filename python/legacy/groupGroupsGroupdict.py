import re
m = re.search(r'([a-zA-Z0-9])\1+',input())
try:
    print(m.group(1))
except:
    print(-1)