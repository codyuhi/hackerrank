# Enter your code here. Read input from STDIN. Print output to STDOUT
_,a,_,b = input(),set(map(int,input().split())),input(),set(map(int,input().split()))
print(len(a^b))