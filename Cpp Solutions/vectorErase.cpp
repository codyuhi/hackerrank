#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int count;
    cin >> count;
    vector<int> vec;
    for(int i = 0; i < count; i++){
        int temp;
        cin >> temp;
        vec.push_back(temp);
    }
    cin >> count;
    vec.erase(vec.begin()+count-1);
    cin >> count;
    int temp;
    cin >> temp;
    vec.erase(vec.begin()+count-1,vec.begin()+temp-1);
    cout << vec.size() << endl;
    for(int i = 0; i < vec.size(); i++){
        if(i > 0){
            cout << " ";
        }
        cout << vec[i];
    }   
    return 0;
}
