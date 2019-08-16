if __name__ == '__main__':
    s = input()
    first = False
    second = False
    third = False
    fourth = False
    fifth = False
    for i in range(len(s)):
        if first == False and s[i].isalnum():
            first = True
        if second == False and s[i].isalpha():
            second = True
        if third == False and s[i].isdigit():
            third = True
        if fourth == False and s[i].islower():
            fourth = True
        if fifth == False and s[i].isupper():
            fifth = True
        if first and second and third and fourth and fifth:
            break
    print(first)
    print(second)
    print(third)
    print(fourth)
    print(fifth)



    

