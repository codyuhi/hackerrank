# Enter your code here. Read input from STDIN. Print output to STDOUT
x,total = list(map(int,input().split()))[1],[]
for i in range(x):
    total += [input().split()]
for i in zip(*total):
    avg = float(0)
    for j in i:
        avg += float(j)
    print(avg / len(i))