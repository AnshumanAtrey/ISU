#include <iostream>
#include <fstream>
using namespace std;

int main() {
    // Create a text file
    ofstream outFile("example.txt");
    
    // Check if the file was created successfully
    if (!outFile) {
        cerr << "Error creating file!" << endl;
        return 1; // Exit with error code
    }

    cout << "File created successfully." << endl;
    outFile.close(); // Close the file
    return 0;
} 