#include <iostream>
using namespace std;

const float pi = 3.14159265358979323846;

float triangle(int h, int b) {
    return (0.5 * h * b); // Area of triangle
}

float rect(int l, int b) {
    return (l * b); // Area of rectangle
}

float sq(int l) {
    return (l * l); // Area of square
}

float cir(int r) {
    return (pi * r * r); // Area of circle
}

int main() {
    // Example usage of the functions
    cout << "Area of triangle (h=5, b=10): " << triangle(5, 10) << endl;
    cout << "Area of rectangle (l=5, b=10): " << rect(5, 10) << endl;
    cout << "Area of square (l=5): " << sq(5) << endl;
    cout << "Area of circle (r=5): " << cir(5) << endl;

    return 0;
}