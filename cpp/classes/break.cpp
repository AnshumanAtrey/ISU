#include <iostream>
using namespace std;

int main() {
    // Initialize a variable to count from 1 to 10
    for (int i = 1; i <= 10; i++) {
        // Check if the current number is 5
        if (i == 5) {
            // Break the loop when i is 5
            break; // Exit the loop
        }
        // Print the current number
        cout << i << " ";
    }
    
    // Indicate that the loop has been exited
    cout << "\nLoop exited at i = 5." << endl;

    return 0; // Indicate that the program ended successfully
}

