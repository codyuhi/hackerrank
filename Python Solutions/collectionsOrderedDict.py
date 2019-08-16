# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
numOfItems = int(input())
ordDict = OrderedDict()
for i in range(numOfItems):
    totalString = list(map(str, input().split()))
    price = int(totalString[len(totalString) - 1])
    itemName = ""
    for j in range(len(totalString) - 1):
        if j > 0:
            itemName += " "
        itemName += totalString[j]
    try:
        ordDict[itemName] += price
    except:
        ordDict[itemName] = price
for key,value in ordDict.items():
    print(key,value)
