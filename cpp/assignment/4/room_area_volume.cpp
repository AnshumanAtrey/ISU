#include <iostream>
using namespace std;

class Room {
private:
    double length;
    double width;
    double height;

public:
    // Method to set dimensions
    void setDimensions(double l, double w, double h) {
        length = l;
        width = w;
        height = h;
    }

    // Method to calculate area
    double calculateArea() {
        return length * width;
    }

    // Method to calculate volume
    double calculateVolume() {
        return length * width * height;
    }
};

int main() {
    Room room;
    double length, width, height;

    cout << "Enter length of the room: ";
    cin >> length;
    cout << "Enter width of the room: ";
    cin >> width;
    cout << "Enter height of the room: ";
    cin >> height;

    room.setDimensions(length, width, height);

    cout << "Area of the room: " << room.calculateArea() << endl;
    cout << "Volume of the room: " << room.calculateVolume() << endl;

    return 0;
} 