#include <iostream>
using namespace std;

// Base class
class Base {
public:
    // Virtual function
    virtual void show() {
        cout << "Base class show function called." << endl;
    }
};

// Derived class
class Derived : public Base {
public:
    // Overriding the base class function
    void show() override {
        cout << "Derived class show function called." << endl;
    }
};

int main() {
    Base *b; // Base class pointer
    Derived d; // Derived class object
    b = &d; // Pointing to derived class object

    // Call the show function
    b->show(); // Calls the derived class function due to virtual function

    return 0;
} 