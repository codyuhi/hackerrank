# Enter your code here. Read input from STDIN. Print output to STDOUT
_,li = input(),list(map(int,input().split()))
print(all((i > 0) for i in li) & any(str(i) == str(i)[::-1] for i in li ))
