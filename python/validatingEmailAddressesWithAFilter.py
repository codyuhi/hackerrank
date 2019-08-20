import re

def fun(s):
    # return True if s is a valid email, else return False
    if re.match(r"^([a-z|0-9|\-|_])+@[a-z|0-9]+\.[a-z]{1,3}$",s):
        return True
    return False