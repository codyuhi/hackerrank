# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(n):
    m = int(input())
    # print("m is",m)
    given = list(map(int, input().split()))
    # print("given is",given)
    out = list()
    bottom = 0
    top = m - 1
    for j in range(m):
        yeet = 0
        # print("Processing",j)
        if given[bottom] > given[top]:
            # print(given[bottom],"is greater than",given[top])
            if out == []:
                # print("Out is an empty set. Appending",given[bottom])
                out.append(given[bottom])
                bottom += 1
                # print("Bottom is now",bottom)
            elif given[bottom] <= out[len(out) - 1]:
                # print(given[bottom], "is less than/equal to", out[len(out) - 1])
                # print("Appending", given[bottom])
                out.append(given[bottom])
                bottom += 1
                # print("Bottom is now", bottom)
            else:
                # print("Yeet is true")
                yeet = 1
                print("No")
                break
        elif given[bottom] < given[top]:
            # print(given[bottom], "is less than", given[top])
            if out == []:
                # print("Out is an empty set. Appending", given[top])
                out.append(given[top])
                top -= 1
                # print("Top is now", top)
            elif given[top] <= out[len(out) - 1]:
                # print(given[top], "is less than/equal to", out[len(out) - 1])
                # print("Appending", given[top])
                out.append(given[top])
                top -= 1
                # print("Top is now", top)
            else:
                # print("Yeet is true")
                yeet == True
                print("No")
                break
        elif given[bottom] == given[top]:
            # print(given[bottom], "is equal to", given[top])
            if out == []:
                # print("Out is an empty set. Appending", given[bottom])
                out.append(given[bottom])
                bottom += 1
                # print("Bottom is now", bottom)
            elif given[bottom] <= out[len(out) - 1]:
                # print(given[bottom], "is less than/equal to", out[len(out) - 1])
                # print("Appending",given[bottom])
                out.append(given[bottom])
                bottom += 1
                # print("Bottom is now", bottom)
            else:
                # print("Yeet is true")
                yeet = 1
                print("No")
                break
        # print("WHAT IS YEET? YEET IS",yeet)
        if bottom > top:
            # print("Out is",out)
            print("Yes")
            break
        elif yeet == 1:
            # print("Out is", out)
            # print("No")
            break
        # print("Out is",out)
