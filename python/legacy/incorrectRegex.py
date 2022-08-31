# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
for i in range(n):
    string = input()
    try:
        valid = re.compile(string)
        print("True")
    except:
        print("False")