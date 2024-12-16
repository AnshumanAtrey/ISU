#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    ifstream inFile("example.txt");
    string line;

    // Check if the file was opened successfully
    if (!inFile) {
        cerr << "Error opening file!" << endl;
        return 1; // Exit with error code
    }

    // Reading from the file
    cout << "Contents of the file:" << endl;
    while (getline(inFile, line)) {
        cout << line << endl; // Print each line
    }

    inFile.close(); // Close the file
    return 0;
} 