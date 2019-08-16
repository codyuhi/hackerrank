# Enter your code here. Read input from STDIN. Print output to STDOUT
a,b = int(input()), int(input())
# print(a,b)
print(str(divmod(a,b)[0])+"\n"+str(divmod(a,b)[1])+"\n"+str(divmod(a,b)))