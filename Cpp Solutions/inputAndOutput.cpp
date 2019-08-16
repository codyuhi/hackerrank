#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int total = 0;
    int temp;
    for(int i = 0; i < 3; i++){
        cin >> temp;
        total += temp;
    }
    cout << total;
    return 0;
}
