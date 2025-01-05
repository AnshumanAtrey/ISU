#include <iostream>

int main() {
    //cout : character output
    //cin : character input
    // Declare a variable to store user input
    int number;

    // Output a message to the user
    std::cout << "Please enter a number: ";

    // Read a number from standard input
    std::cin >> number;

    // Output the number back to the user
    std::cout << "You entered: " << number << std::endl;

    return 0;
}