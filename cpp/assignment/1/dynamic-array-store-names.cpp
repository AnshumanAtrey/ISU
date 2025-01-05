#include <iostream>
#include <string>
using namespace std;

int main() {
    int numStudents;

    // Ask the user for the number of students
    cout << "Enter the number of students: ";
    cin >> numStudents;

    // Create a dynamic array to store student names
    string* studentNames = new string[numStudents];

    // Input student names
    for (int i = 0; i < numStudents; ++i) {
        cout << "Enter name of student " << (i + 1) << ": ";
        cin >> studentNames[i];
    }

    // Display the student names
    cout << "\nList of student names:\n";
    for (int i = 0; i < numStudents; ++i) {
        cout << "Student " << (i + 1) << ": " << studentNames[i] << endl;
    }

    // Free the dynamically allocated memory
    delete[] studentNames;

    return 0;
}