import re
n, string = int(input()), ""
for _ in range(n):
    string = input()
    if len(string) != 10:
        print("NO")
        continue
    if re.match(r'^[7-9]\d{9}',string):
        print("YES")
    else:
        print("NO")
    