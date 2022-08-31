def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if len(sub_string) > 0 and len(sub_string) + i <= len(string) and string[i] == sub_string[0]:
            match = True
            for j in range(len(sub_string)):
                if string[i+j] != sub_string[j]:
                    match = False
                    break
            if match:
                count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)