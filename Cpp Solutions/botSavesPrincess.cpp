#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void displayPathtoPrincess(int n, vector <string> grid){
    //your logic here
    int ym, xm;
    int yp, xp;

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(grid[i][j] == 'm'){
                ym = i;
                xm = j;
            }
            if(grid[i][j] == 'p'){
                yp = i;
                xp = j;
            }
        }
    }
    int x = xp - xm;
    int y = yp - ym;
    while(x != 0){
        if(x>0){
            cout << "RIGHT" << endl;
            if(y>0){
                cout << "DOWN" << endl;
                y = abs(y) - 1;
            }else if(y == 0){
                continue;
            }else{
                cout << "UP" << endl;
                y++;
            }
            x--;
        }else{
            cout << "LEFT" << endl;
            if(y > 0){
                cout << "DOWN" << endl;
                y = abs(y) - 1;
            }else if(y == 0){
                continue;
            }else{
                cout << "UP" << endl;
                y++;
            }
            x++;
        }
    }
    return;
}

int main(void) {

    int m;
    vector <string> grid;

    cin >> m;

    for(int i=0; i<m; i++) {
        string s; cin >> s;
        grid.push_back(s);
    }

    displayPathtoPrincess(m,grid);

    return 0;
}