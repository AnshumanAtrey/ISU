#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ofstream outFile("example.txt", ios::app); // Open file in append mode

    // Check if the file was opened successfully
    if (!outFile) {
        cerr << "Error opening file for appending!" << endl;
        return 1; // Exit with error code
    }

    // Appending to the file
    outFile << "This line is appended to the file." << endl;
    outFile.close(); // Close the file

    cout << "Data appended to file successfully." << endl;
    return 0;
} 