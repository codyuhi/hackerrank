#include <iostream>
#include <string>
using namespace std;

int main() {
	// Complete the program
    string one = "";
    string two = "";
    cin >> one >> two;
    cout << one.length() << " " << two.length() << endl;
    cout << one + two << endl;
    char first = one[0];
    one[0] = two[0];
    two[0] = first;
    cout << one << " " << two;
    return 0;
}

