t = int(input())
for i in range(t):
    _,a = input(),set(map(int,input().split()))
    _,b = input(),set(map(int,input().split()))
    print(a <= b)