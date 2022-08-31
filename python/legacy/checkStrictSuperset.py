A = set(map(int,input().split()))
n = int(input())
result = True
for i in range(n):
    B = set(map(int,input().split()))
    if A.issuperset(B):
        pass
    else:
        result = False
        break
print(result)