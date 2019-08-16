n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    given = list(map(str,input().split()))
    if given[0] == "pop":
        # print("Popped")
        s.pop()
    elif given[0] == "remove":
        # print("Removing " + given[1])
        s.remove(int(given[1]))
    elif given[0] == "discard":
        # print("Discarding " + given[1])
        s.discard(int(given[1]))
total = 0
for i in s:
    total += i
print(total)