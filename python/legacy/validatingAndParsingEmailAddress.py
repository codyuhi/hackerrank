import email.utils
import re
for i in range(int(input())):
    string = list(map(str,input().split()))
    string[1] = string[1][1:-1]
    if not re.match(r'^[a-zA-Z][\w\-\.]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$',string[1]):
        # print(string[1],"matches regex")
        continue
    try:
        print(email.utils.formataddr((string[0],string[1])))
    except:
        continue