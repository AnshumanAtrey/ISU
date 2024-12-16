#include <iostream>
using namespace std;

void swap(int* a, int* b) {
    int temp = *a; // Store the value at pointer a
    *a = *b;       // Assign the value at pointer b to pointer a
    *b = temp;     // Assign the stored value to pointer b
}

int main() {
    int x, y;
    cout << "Enter two numbers: ";
    cin >> x >> y;

    cout << "Before swapping: x = " << x << ", y = " << y << endl;
    swap(&x, &y); // Pass the addresses of x and y
    cout << "After swapping: x = " << x << ", y = " << y << endl;

    return 0;
}
