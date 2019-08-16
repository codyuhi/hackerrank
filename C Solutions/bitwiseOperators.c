#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.


void calculate_the_maximum(int n, int k) {
  //Write your code here.
  //k is the a max
  //n is the b max
  int arr[3] = {0,0,0};
  for(int i = 0; i < k; i++){
      int a = i + 1;
      int b;
      for(int j = i + 1; j < n; j++){
          b = j + 1;
          //printf("a = %d, b = %d\n", a, b);
          int anb = a & b;
          int aob = a | b;
          int axob = a ^ b;
          if(anb < k && anb > arr[0]){
              arr[0] = anb;
          }
          if(aob < k && aob > arr[1]){
              arr[1] = aob;
          }
          if(axob < k && axob > arr[2]){
              arr[2] = axob;
          }
      }
      
  }
  for(int i = 0; i < 3; i++){
      printf("%d\n",arr[i]);
  }
}

int main() {
    int n, k;
  
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}
