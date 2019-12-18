#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int professorCount = 1;
int studentCount = 1;

class Person {
    protected:
        string name;
        int age;
    public:
        virtual void getdata(){}
        virtual void putdata(){}
};

class Professor: public Person {
    protected:
        int publications;
        int cur_id;
        int pCount;
    public:
        void getdata(){
            cin >> name;
            cin >> age;
            cin >> publications;
            pCount = professorCount;
            professorCount++;
        }
        void putdata(){
            cout << name << " " << age << " " << publications << " " << pCount << endl;
        }
};

class Student:public Person {
    protected:
        int marks[6];
        int cur_id;
        int totalMarks;
        int sCount;
    public:
        void getdata(){
            sCount = studentCount;
            totalMarks = 0;
            cin >> name;
            cin >> age;
            for(int i = 0; i < 6; i++){
                cin >> marks[i];
                totalMarks += marks[i];
            }
            studentCount++;
        }
        void putdata(){
            cout << name << " " << age << " " << totalMarks << " " << sCount << endl;
        }
};

int main(){

    int n, val;
    cin>>n; //The number of objects that is going to be created.
    Person *per[n];

    for(int i = 0;i < n;i++){

        cin>>val;
        if(val == 1){
            // If val is 1 current object is of type Professor
            per[i] = new Professor;

        }
        else per[i] = new Student; // Else the current object is of type Student

        per[i]->getdata(); // Get the data from the user.

    }

    for(int i=0;i<n;i++)
        per[i]->putdata(); // Print the required output for each object.

    return 0;

}
