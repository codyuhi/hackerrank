#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    int q;
    cin >> n;
    cin >> q;
    vector<vector<int>> ruleArr;
    for(int i = 0; i < n; i++){
      int size;
      cin >> size;
      vector<int> tempArr;
      for (int j = 0; j < size; j++) {
        int temp;
        cin >> temp;
        tempArr.push_back(temp);
        }
        ruleArr.push_back(tempArr);
    }
    for(int i = 0; i < q; i++){
        if(i > 0){
            cout << endl;
        }
            int arrNum;
            int val;
            cin >> arrNum;
            cin >> val;
            cout << ruleArr[arrNum][val];
    }

    return 0;
}

