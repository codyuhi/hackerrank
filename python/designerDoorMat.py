# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n, m = [int(x) for x in input().split()]
    #print("n is",n,"and m is",m)
    vertMid = int((n/2)+.5)
    horMid = int((m/2)+.5)
    list = list()
    for i in range(vertMid-1):
        string = ""
        y = i*(-3) + (horMid - 2)
        for j in range(y):
            string+='-'
        string += '.'
        for j in range(i):
            string += "|.."
        string += '|'
        for j in range(i):
            string += "..|"
        string += '.'
        for j in range(y):
            string+='-'
        print(string)
    string = ""
    for i in range(int((m-7)/2)):
        string += "-"
    string += "WELCOME"
    for i in range(int((m-7)/2)):
        string += "-"
    print(string)
    for i in range(vertMid-1):
        string = ""
        y = i*(3) + 3
        for j in range(y):
            string+='-'
        string += '.'
        for j in range(vertMid - 2 - i):
            string += "|.."
        string += '|'
        for j in range(vertMid -2-i):
            string += "..|"
        string += '.'
        for j in range(y):
            string+='-'
        print(string)