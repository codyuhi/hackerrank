#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int Q;
    int type;
    int given;
    set<int>mySet;
    cin >> Q;
    for(int i = 0; i < Q; i++){
        cin >> type;
        cin >> given;
        switch(type){
            case 1:
                mySet.insert(given);
                break;
            case 2:
                mySet.erase(given);
                break;
            case 3:
                set<int>::iterator itr = mySet.find(given);
                if(itr != mySet.end()){
                    cout << "Yes" << endl;
                }
                else{
                    cout << "No" << endl;
                }
                break;
        }
    }
    return 0;
}
