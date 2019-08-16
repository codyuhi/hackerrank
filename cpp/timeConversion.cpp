#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the timeConversion function below.
 */
string timeConversion(string s) {
    /*
     * Write your code here.
     */
    
    if(s.substr(8,10) == "PM"){
        int hours = stoi(s.substr(0,2));
        if(hours != 12){
            hours += 12;
        }
        s[0] = to_string(hours)[0];
        s[1] = to_string(hours)[1];
        return s.substr(0,8);
    }else if(s.substr(0,2) == "12"){
        return "00" + s.substr(2,6);
    }else{
        return s.substr(0,8);
    }
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = timeConversion(s);

    fout << result << "\n";

    fout.close();

    return 0;
}