#include <iostream>
#include <iomanip> 
using namespace std;

int main() {
	int T; cin >> T;
	cout << setiosflags(ios::uppercase);
	cout << setw(0xf) << internal;
	while(T--) {
		double A; cin >> A;
		double B; cin >> B;
		double C; cin >> C;

		/* Enter your code here */
        cout << setprecision(0) << A << endl;
		cout << setprecision(0) << A << endl;
		cout << setprecision(9) << showpoint <<  C << endl;
	}
	return 0;

}