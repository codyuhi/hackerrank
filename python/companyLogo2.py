# Enter your code here. Read input from STDIN. # print output to STDOUT
from itertools import groupby
s = input()
groups = []
uniquekeys = []
for k, g in groupby(s):
    groups.append(list(g))
    uniquekeys.append(k)
final = list()
string = ""
biggest = (0, "{")
second = (0, "{")
third = (0, "{")

for i in groups:
    # print("Processing",i)
    # print("Checking if",len(i),"is greater than",third[0])
    if len(i) > third[0]:
        # print(len(i),"is greater than",third[0])
        # print("Checking if", len(i), "is greater than", second[0])
        if len(i) > second[0]:
            # print(len(i), "is greater than", second[0])
            # print("Checking if", len(i), "is greater than", biggest[0])
            if len(i) > biggest[0]:
                # print(len(i), "is greater than", biggest[0])
                third = second
                # print("Third is now", third)
                second = biggest
                # print("Second is now",second)
                biggest = (len(i), i[0])
                # print("Biggest is now", biggest)
            elif len(i) == biggest[0]:
                # print(len(i), "is equal to", biggest[0])
                # print("Checking if", i[0], "comes before", biggest[1][0])
                if i[0] < biggest[1][0]:
                    # print(i[0], "comes before", biggest[1][0])
                    third = second
                    # print("Third is now",third)
                    second = biggest
                    # print("Second is now",second)
                    biggest = (len(i), i[0])
                    # print("Biggest is now", biggest)
                else:
                    # print(biggest[1][0], "comes before", i[0])
                    # print("Checking if",i[0],"comes before",second[1][0])
                    if i[0] < second[1][0]:
                        # print(i[0], "comes before", second[1][0])
                        third = second
                        # print("Third is now", third)
                        second = (len(i), i)
                        # print("Second is now", second)
                    else:
                        # print(i[0], "comes after", second[1][0])
                        # print("Checking if",i[0],"comes before",third[1][0])
                        if i[0] < third[1][0]:
                            # print(i[0], "comes before", third[1][0])
                            third = (len(i),i)
                            # print("Third is now",third)
                        else:
                            # print(i[0], "comes after", third[1][0])
                            # print("Nothing added")
                            temp = 0
            else:
                # print(len(i), "is less than", biggest[0])
                third = second
                # print("Third is now",third)
                second = (len(i), i)
                # print("Second is now", second)
        elif len(i) == second[0]:
            # print(len(i), "is equal to", second[0])
            # print("Checking if",len(i),"is equal to",biggest[0])
            if len(i) == biggest[0]:
                # print(len(i),"is equal to",biggest[0])
                # print("Checking if",i[0],"comes before",biggest[1][0])
                if i[0] < biggest[1][0]:
                    # print(i[0],"comes before",biggest[1][0])
                    third = second
                    # print("Third is now",third)
                    second = biggest
                    # print("Second is now",second)
                    biggest = (len(i),i[0])
                    # print("Biggest is now",biggest)
                else:
                    # print(i[0],"comes after",biggest[1][0])
                    third = second
                    # print("Third is now",third)
                    second = (len(i),i[0])
                    # print("Second is now",second)
            else:
                # print("Checking if", i[0], "comes before", second[1][0])
                if i[0] < second[1][0]:
                    # print(i[0], "comes before", second[1][0])
                    third = second
                    # print("Third is now",third)
                    second = (len(i), i[0])
                    # print("Second is now", second)
                else:
                    # print(i[0], "comes after", second[1][0])
                    third = (len(i), i[0])
                    # print("Third is now", third)
        else:
            # print(len(i), "is less than", second[0])
            third = (len(i), i[0])
            # print("Third is now", third)
    elif len(i) == third[0]:
        # print(len(i),"is equal to",third[0])
        # print("Checking if",len(i),"is equal to",second[0])
        if len(i) == second[0]:
            # print(len(i), "is equal to", second[0])
            # print("Checking if",len(i),"is equal to",biggest[0])
            if len(i) == biggest[0]:
                # print(len(i),"is equal to",biggest[0])
                # print("Checking if",i[0],"comes before",biggest[1][0])
                if i[0] < biggest[1][0]:
                    # print(i[0],"comes before",biggest[1][0])
                    third = second
                    # print("Third is now",third)
                    second = biggest
                    # print("Second is now",second)
                    biggest = (len(i),i[0])
                    # print("Biggest is now",biggest)
                else:
                    # print(i[0],"comes after",biggest[1][0])
                    # print("Checking if",i[0],"comes before",second[1][0])
                    if i[0] < second[1][0]:
                        # print(i[0],"comes before",second[1][0])
                        third = second
                        # print("Third is now", third)
                        second = (len(i), i[0])
                        # print("Second is now", second)
                    else:
                        temp = 0
                        # print(i[0],"comes after",second[1][0])
                        # print("Checking if",i[0],"comes before",third[1][0])
                        if i[0] < third[1][0]:
                            # print(i[0], "comes before", third[1][0])
                            third = (len(i), i[0])
                            # print("Third is now", third)
                        else:
                            temp = 0
                            # print(i[0], "comes after", third[1][0])
                            # print("Nothing added")

            else:
                temp = 0
                # print(len(i),"is not equal to",biggest[0])
                # print("Checking if",i[0],"comes before",second[1][0])
                if i[0] < second[1][0]:
                    # print(i[0],"comes before",second[1][0])
                    third = second
                    # print("Third is now",third)
                    second = (len(i),i[0])
                    # print("Second is now",second)
                else:
                    # print(i[0], "comes after", second[1][0])
                    third = (len(i),i[0])
                    # print("Third is now",third)
        else:
            # print(len(i),"is not equal to",second[0])
            # print("Checking if",i[0],"comes before",third[1][0])
            temp = 0
            if i[0] < third[1][0]:
                # print(i[0],"comes before",third[1][0])
                third = (len(i),i[0])
                # print("Third is now",third)
            else:
                # print(i[0],"comes after",third[1][0])
                temp = 0
    else:
        # print(len(i),"is less than",third[0])
        temp = 0

        
# print(groups)

print(biggest[1][0], biggest[0])
print(second[1][0], second[0])
print(third[1][0], third[0])

# qwertyuiopasdfghjklzxcvbnm

# a 1
# b 1
# c 1
