#include <iostream>
using namespace std;

template <typename T>
T absoluteValue(T num) {
    return (num < 0) ? -num : num;
}

int main() {
    cout << "Absolute value of -5: " << absoluteValue(-5) << endl; // Example usage
    cout << "Absolute value of 3.14: " << absoluteValue(3.14) << endl; // Example usage
    return 0;
}