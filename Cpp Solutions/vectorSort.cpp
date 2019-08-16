#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int size = 0;
    cin >> size;
    vector<int> vec;
    for (int i = 0; i < size; i++){
        int temp;
        cin >> temp;
        vec.push_back(temp);
    }
    sort(vec.begin(), vec.end());
    for(int i = 0; i < size; i++){
        if(i > 0){
            cout << " ";
        }
        cout << vec[i];
    }
    
    return 0;
}
