import textwrap

def wrap(string, max_width):
    list = textwrap.wrap(string,width=max_width)
    final = ""
    for i in range(len(list)):
        if i > 0:
            final += "\n"
        final += list[i]
    return final

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)