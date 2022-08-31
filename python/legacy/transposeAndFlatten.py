import numpy

given = list(input().split())
n = int(given[0])
m = int(given[1])

finalList = list()

for i in range(n):
    finalList.append(list(map(int, input().split())))

print(numpy.array(finalList).transpose())
print(numpy.array(finalList).flatten())