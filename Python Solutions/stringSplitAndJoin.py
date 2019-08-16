def split_and_join(line):
    # write your code here
    line = line.split(" ")
    result = ""
    for i in range(len(line)):
        if i > 0:
            result += "-"
        result += line[i]
    #print(result)
    return result
        

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)