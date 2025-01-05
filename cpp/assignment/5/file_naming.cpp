#include <iostream>
#include <fstream>
using namespace std;

int main() {
    string fileName;
    cout << "Enter the name of the file to create (with .txt extension): ";
    cin >> fileName;

    // Create a text file with the specified name
    ofstream outFile(fileName);
    
    // Check if the file was created successfully
    if (!outFile) {
        cerr << "Error creating file!" << endl;
        return 1; // Exit with error code
    }

    cout << "File '" << fileName << "' created successfully." << endl;
    outFile.close(); // Close the file
    return 0;
} 