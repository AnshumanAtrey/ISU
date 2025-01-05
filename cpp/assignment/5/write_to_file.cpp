#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ofstream outFile("example.txt");

    // Check if the file was created successfully
    if (!outFile) {
        cerr << "Error creating file!" << endl;
        return 1; // Exit with error code
    }

    // Writing to the file
    outFile << "Hello, World!" << endl;
    outFile << "This is a sample text file." << endl;
    outFile.close(); // Close the file

    cout << "Data written to file successfully." << endl;
    return 0;
} 