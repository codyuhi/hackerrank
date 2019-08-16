#include <iostream>
#include <cstdio>
using namespace std;

string processInt(int input) {
  switch (input) {
  case 1:
    return "one";
    break;
  case 2:
    return "two";
    break;
  case 3:
    return "three";
    break;
  case 4:
    return "four";
    break;
  case 5:
    return "five";
    break;
  case 6:
    return "six";
    break;
  case 7:
    return "seven";
    break;
  case 8:
    return "eight";
    break;
  case 9:
    return "nine";
    break;
  default:
    if(input % 2 == 0){
        return "even";
    }
    else{
        return "odd";
    }
    break;
  }
}

int main() {
    // Complete the code.
    int input1;
    int input2;
    cin >> input1 >> input2;
    int difference = input2 - input1;
    for(int i = 0; i < difference + 1; i++){
        if(i > 0){
            cout << endl;
        }
        cout << processInt(input1+i);
    }
    return 0;
}

