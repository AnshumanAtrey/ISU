#include <iostream>
using namespace std;

class Student {
private:
    string name;
    int roll_no;
    float marks;

public:
    // Method to set data
    void setData(string n, int r, float m) {
        name = n;
        roll_no = r;
        marks = m;
    }

    // Method to print data
    void printData() {
        cout << "Name: " << name << ", Roll No: " << roll_no << ", Marks: " << marks << endl;
    }
};

int main() {
    Student student;
    string name;
    int roll_no;
    float marks;

    cout << "Enter name of the student: ";
    cin >> name;
    cout << "Enter roll number: ";
    cin >> roll_no;
    cout << "Enter marks: ";
    cin >> marks;

    student.setData(name, roll_no, marks);
    student.printData();

    return 0;
} 