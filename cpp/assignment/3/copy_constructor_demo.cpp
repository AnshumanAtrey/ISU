#include <iostream>
using namespace std;

class CopyDemo {
private:
    int value;

public:
    // Parameterized constructor
    CopyDemo(int v) : value(v) {
        cout << "Parameterized constructor called, value: " << value << endl;
    }

    // Copy constructor
    CopyDemo(const CopyDemo &obj) {
        value = obj.value;
        cout << "Copy constructor called, value: " << value << endl;
    }

    // Method to display value
    void display() {
        cout << "Value: " << value << endl;
    }
};

int main() {
    CopyDemo obj1(10); // Calls parameterized constructor
    CopyDemo obj2 = obj1; // Calls copy constructor

    obj1.display();
    obj2.display();

    return 0;
} 