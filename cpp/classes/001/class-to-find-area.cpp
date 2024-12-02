#include <iostream>
using namespace std;

const float pi = 3.14159265358979323846;

class Shape {
public:
    float triangle(int h, int b) {
        return (0.5 * h * b); // Area of triangle
    }

    float rectangle(int l, int b) {
        return (l * b); // Area of rectangle
    }

    float square(int l) {
        return (l * l); // Area of square
    }

    float circle(int r) {
        return (pi * r * r); // Area of circle
    }
};

int main() {
    Shape area;
    cout << "Area of triangle (h=5, b=10): " << area.triangle(5, 10) << endl;
    cout << "Area of rectangle (l=5, b=10): " << area.rectangle(5, 10) << endl;
    cout << "Area of square (l=5): " << area.square(5) << endl;
    cout << "Area of circle (r=5): " << area.circle(5) << endl;

    return 0;
}