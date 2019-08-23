regex_pattern='(?:M|MM|MMM)?(?:C|CC|CCC|CD|D|DC|DCC|DCCC|CM)?(?:X|XX|XXX|XL|L|LX|LXX|LXXX|XC)?(?:I|II|III|IV|V|VI|VII|VIII|IX)?$'    # Do not delete 'r'.
import re
print(str(bool(re.match(regex_pattern, input()))))