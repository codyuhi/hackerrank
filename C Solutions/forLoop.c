#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int a, b;
    scanf("%d\n%d", &a, &b);
    // Complete the code.
    for(int i = a; i < b+1; i++){
        if(i > a){
            printf("\n");
        }
        if(i > 9){
            if((i%2)!=0){
                printf("odd");
            }else{
                printf("even");
            }
        }else{
            if(i == 1){
                printf("one");
            }
            else if(i == 2){
                printf("two");
            }
            else if (i == 3)
            {
                printf("three");
            }
            else if (i == 4)
            {
                printf("four");
            }
            else if (i == 5)
            {
                printf("five");
            }
            else if (i == 6)
            {
                printf("six");
            }
            else if (i == 7)
            {
                printf("seven");
            }
            else if (i == 8)
            {
                printf("eight");
            }
            else if (i == 9)
            {
                printf("nine");
            }
        }
    }
    return 0;
}
