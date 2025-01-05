#include <iostream>
using namespace std;

class Rectangle {
private:
    double length;
    double width;

public:
    // Method to set dimensions
    void setDimensions(double l, double w) {
        length = l;
        width = w;
    }

    // Method to calculate area
    double calculateArea() {
        return length * width;
    }

    // Method to display dimensions
    void displayDimensions() {
        cout << "Length: " << length << ", Width: " << width << endl;
    }
};

int main() {
    Rectangle rect;
    double length, width;

    cout << "Enter length of the rectangle: ";
    cin >> length;
    cout << "Enter width of the rectangle: ";
    cin >> width;

    rect.setDimensions(length, width);
    rect.displayDimensions();
    cout << "Area of the rectangle: " << rect.calculateArea() << endl;

    return 0;
} 