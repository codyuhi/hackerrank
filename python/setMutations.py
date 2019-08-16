# Enter your code here. Read input from STDIN. Print output to STDOUT
_,A,N = input(),set(map(int,input().split())),int(input())
for i in range(N):
    op = input().split()[0]
    given = set(map(int,input().split()))
    if op == "update":
        A |= given
    elif op == "intersection_update":
        A &= given
    elif op == "difference_update":
        A -= given
    elif op == "symmetric_difference_update":
        A ^= given
print(sum(A))