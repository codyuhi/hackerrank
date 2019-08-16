def swap_case(s):
    t = ""
    for i in range(len(s)):
        if s[i].isupper():
            t += s[i].lower()
        elif s[i].islower():
            t += s[i].upper()
        else:
            t += s[i]
    return t

if __name__ == '__main__':