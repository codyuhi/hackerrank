#include <iostream>
#include <cstdio>
using namespace std;

/*
Add `int max_of_four(int a, int b, int c, int d)` here.
*/
int max_of_two(int first, int second){
    if(first > second){
        return first;
    }else{
        return second;
    }
}

int max_of_four(int a, int b, int c, int d){
    int first = max_of_two(a,b);
    int second = max_of_two(c,d);
    first = max_of_two(first,second);
    return first;
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}

