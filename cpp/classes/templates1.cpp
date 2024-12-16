// Include the iostream library for input and output operations
#include <iostream>
// Include the string library to use string data type
#include <string>

// Use the standard namespace to avoid prefixing std:: before standard functions and types
using namespace std;

// Define a template function that can accept any data type T
template<class T>
void display(T x) {
    // Output the value of x to the console, prefixed with "Template Display :"
    cout << "Template Display :" << x << "\n";
}

// Overloaded function specifically for integers
void display(int x) {
    // Output the integer value to the console, prefixed with "Explicit Display :"
    cout << "Explicit Display :" << x << "\n";
}

// The main function where the program execution starts
int main() {
    // Call the template display function with an integer argument
    display(100); // This will call the overloaded display(int) function

    // Call the template display function with a double argument
    display(12.35); // This will call the template display<double>(double) function

    // Call the template display function with a char argument
    display('c'); // This will call the template display<char>(char) function

    // Return 0 to indicate that the program finished successfully
    return 0;
}