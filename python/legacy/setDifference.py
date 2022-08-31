# Enter your code here. Read input from STDIN. Print output to STDOUT
a, aList, b, bList = input(),set(map(int,input().split())),input(),set(map(int,input().split()))
print(len(aList-bList))