#include <iostream>

using namespace std;

// Class definition for Calculator
class Calculator {
public:
    // Method to add two numbers
    double add(double a, double b) {
        return a + b; // Return the sum of a and b
    }
};

int main() {
    // Create an object of the Calculator class
    Calculator calc;

    // Variables to hold user input
    double num1, num2;

    // Prompt user for input
    cout << "Enter first number: ";
    cin >> num1;
    cout << "Enter second number: ";
    cin >> num2;
    // Call the add method and display the result
    double result = calc.add(num1, num2);
    cout << "The sum of " << num1 << " and " << num2 << " is: " << result << endl;

    return 0;
}