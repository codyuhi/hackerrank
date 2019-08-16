#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    char ch;
    char s[100];
    char sen[100];
    scanf("%c", &ch);
    scanf("%s", s);
    scanf("\n");
    scanf("%[^\n]%*c", sen);
    /*
    In order to take a line as input, 
    you can use scanf("%[^\n]%*c", s); 
    where s is defined as char s[MAX_LEN]
     */
    printf("%c\n", ch);
    printf("%s\n", s);
    printf("%s", sen);
    return 0;
    /*
    After inputting the character and the string, 
    inputting the sentence by the above mentioned statement won't work. 
    This is because, at the end of each line,
     a new line character (\n) is present. 
     So, the statement: scanf("%[^\n]%*c", s); 
     will not work because the last statement will read a newline 
     character from the previous line. 
     This can be handled in a variety of ways and one of them being: 
    scanf("\n"); before the last statement.
     */
}
