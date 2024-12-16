#include <iostream>
using namespace std;

// Function to swap two numbers using reference variables
void swap(int& a, int& b) {
    int temp = a; // Store the value of a in a temporary variable
    a = b;        // Assign the value of b to a
    b = temp;     // Assign the stored value to b
}

int main() {
    int x, y;
    cout << "Enter two numbers: ";
    cin >> x >> y; // Input two numbers from the user

    cout << "Before swapping: x = " << x << ", y = " << y << endl; // Display values before swapping
    swap(x, y); // Call the swap function with x and y
    cout << "After swapping: x = " << x << ", y = " << y << endl; // Display values after swapping

    return 0;
}