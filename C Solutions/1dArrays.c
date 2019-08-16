#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    int count = 0;
    scanf("%d",&count);
    int *arr = (int*)malloc(count * sizeof(int));
    int total = 0;
    int why = 0;
    for(int i = 0; i < count; i++){
        // scanf("%d", &arr[i]);
        // total += arr[i];
        scanf("%d", &why);
        total += why;
    }
    printf("%d",total);
    return 0;
}

