# Enter your code here. Read input from STDIN. Print output to STDOUT
string = input()
lower = ""
upper = ""
oddNumber = ""
evenNumber = ""
for i in string:
    if i.islower():
        lower += i
    if i.isupper():
        upper += i
    if i.isdigit():
        if int(i) % 2 == 0:
            evenNumber += i
        else:
            oddNumber += i
lower = ''.join(str(i) for i in sorted(lower))
upper = ''.join(str(i) for i in sorted(upper))
number = ''.join(str(i) for i in sorted(oddNumber)) + ''.join(str(i) for i in sorted(evenNumber))
print(lower + upper + number,end="",flush=True)