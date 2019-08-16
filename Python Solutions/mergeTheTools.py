'''
def merge_the_tools(string, k):
    # your code goes here
    arr = list(list())
    word = ""
    duplicate = False
    for l in range(k):
        for i in range(k):
            for j in range(len(word)):
                if word[j] == string[i + (l*k)]:
                    duplicate = True
            if duplicate == False:
                word += string[i + (l*k)]
            duplicate = False
        print(word)
        word = ""
'''
def merge_the_tools(string, k):
    # your code goes here
    #S, N = input(), int(input())
    for part in zip(*[iter(string)] * k):
        d = dict()
        print(''.join([d.setdefault(c, c) for c in part if c not in d]))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
