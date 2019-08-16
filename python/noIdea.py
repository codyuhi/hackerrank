# Enter your code here. Read input from STDIN. Print output to STDOUT
given = list(map(int, input().split()))
n = int(given[0])
m = int(given[1])
arr = list(map(int,input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
happiness = int(0)
for i in range(len(arr)):
    tempSet = set([arr[i]])
    if tempSet & A:
        # print("DETECTED IN A ARRAY",arr[i])
        happiness += 1
    if tempSet & B:
        # print("DETECTED IN B ARRAY",arr[i])
        happiness -= 1
print(happiness)
