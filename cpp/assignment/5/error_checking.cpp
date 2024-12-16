#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ofstream outFile("example.txt");

    // Error checking for file creation
    if (!outFile) {
        cerr << "Error: Unable to create file!" << endl;
        return 1; // Exit with error code
    }

    outFile << "This is a test file." << endl;
    outFile.close(); // Close the file
    cout << "File created and written successfully." << endl;
    return 0;
} 