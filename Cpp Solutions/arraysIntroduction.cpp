#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    unsigned int size;
    cin >> size;
    int arr[size];
    int temp;
    for(unsigned int i; i < size; i++){
        cin >> temp;
        arr[i] = temp;
    }
    for (unsigned int i; i < size; i++) {
      if(i > 0){
          cout << " ";
      }
      if(i == size)
      cout << arr[size - i];
      else
      cout << arr[size-i-1];
    }
    return 0;
}
