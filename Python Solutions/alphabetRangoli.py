def print_rangoli(size):
    # your code goes here
    out = ""
    placeholder = 2 * size
    for i in range(size):
        for j in range((placeholder) - (2*(i+1))):
            #print("j is", j)
            out+="-"
        for j in range(i+1):
            if j > 0:
                out+="-"
            out +=chr((96+size)-j)
        for j in range(i):
            out+="-"
            out +=chr((96+size)-(i-j)+1)
        for j in range((placeholder) - (2*(i+1))):
            #print("j is", j)
            out+="-"
        print(out)
        out = ""
    for i in range(size - 1):
        for j in range((i+1)*2):
            out += "-"
        for j in range(size-i-1):
            if j > 0:
                out+="-"
            out +=chr((96+size)-j)
        for j in range(size-i-2):
            out+="-"
            out += chr(96+i+j+3)
        for j in range((i+1)*2):
            out += "-"
        print(out)
        out = ""

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)