# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
mSet = set(map(int, input().split()))
n = int(input())
nSet = set(map(int, input().split()))
mList = mSet.difference(nSet)
nList = nSet.difference(mSet)
finalList = sorted(list(mSet.difference(nSet).union(nSet.difference(mSet))))
for i in range(len(finalList)):
    print(finalList[i])
