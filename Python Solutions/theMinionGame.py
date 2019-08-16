def minion_game(string):
    # your code goes here
    Stuart = int(0)
    Kevin = int(0)
    for i in range(len(string)):
        if string[i] in ('A','E','I','O','U'):
            Kevin += len(string)-i
        else:
            Stuart += len(string)-i
    if Stuart > Kevin:
        print("Stuart",Stuart)
    elif Kevin > Stuart:
        print("Kevin",Kevin)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)