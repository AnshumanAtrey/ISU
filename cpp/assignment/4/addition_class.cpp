#include <iostream>
using namespace std;

class AdditionClass {
private:
    int num1;
    int num2;
    int result;

public:
    // Method to read numbers
    void read() {
        cout << "Enter first number: ";
        cin >> num1;
        cout << "Enter second number: ";
        cin >> num2;
    }

    // Method to calculate sum
    void sum() {
        result = num1 + num2;
    }

    // Method to print result
    void print() {
        cout << "Sum: " << result << endl;
    }
};

int main() {
    AdditionClass obj1, obj2;

    obj1.read();
    obj1.sum();
    obj1.print();

    obj2.read();
    obj2.sum();
    obj2.print();

    return 0;
} 