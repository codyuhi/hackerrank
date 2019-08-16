def average(array):
    # your code goes here
    s = set(array)
    nlist = list(s)
    total = float()
    for i in range(len(nlist)):
        total += nlist[i]
    format(total, '.3f')
    total /= len(nlist)
    return total
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)