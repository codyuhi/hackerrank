#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    cin >> n;
    vector<int> v;
    for(int i = 0; i < n; i++){
        int temp;
        cin >> temp;
        v.push_back(temp);
    } 
    int q;
    cin >> q;
    //vector<int> qv;
    for(int i = 0; i < q; i++){
        int temp;
        cin >> temp;
        std::vector<int>::iterator low = std::lower_bound(v.begin(), v.end(), temp);
        if(binary_search(v.begin(), v.end(), temp)){
            cout << "Yes ";
        }else{
            cout << "No ";
        }
        cout << (low-v.begin()) + 1 << '\n';
    }  
    return 0;
}
