#include <iostream>
using namespace std;

class Demo {
public:
    // Constructor
    Demo() {
        cout << "Constructor called!" << endl;
    }
    // Destructor
    ~Demo() {
        cout << "Destructor called!" << endl;
    }
};

int main() {
    cout << "Creating an object of Demo class." << endl;
    Demo obj; // Object created, constructor is called

    cout << "Exiting main function." << endl;
    // Destructor will be called automatically when obj goes out of scope

    return 0;
} 