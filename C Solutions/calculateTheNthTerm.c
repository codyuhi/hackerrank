#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.

int find_nth_term(int m, int n, int a, int b, int c)
{
    //Write your code here.
    m++;
    //printf("Now processing m=%d, n=%d, a=%d, b=%d, c=%d\n", m, n, a, b, c);
    if (n == m)
    {
        return c;
    }
    else
    {
        return find_nth_term(m, n, b, c, a + b + c);
    }
}

int main()
{
    int m, n, a, b, c;
    m = 2;

    scanf("%d %d %d %d", &n, &a, &b, &c);
    int ans = find_nth_term(m, n, a, b, c);

    printf("%d", ans);
    return 0;
}

