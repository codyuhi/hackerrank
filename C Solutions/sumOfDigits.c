#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{

    int n;
    scanf("%d", &n);
    //Complete the code to calculate the sum of the five digits on n.
    int array[5];
    int total = 0;
    int asset = 10;
    for(int i = 0; i < 5; i++){
        total += n % asset;
        n -= (n % asset);
        n /= asset;
    }
    printf("%d", total);
    return 0;
}