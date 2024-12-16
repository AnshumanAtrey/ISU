#include <iostream>

using namespace std;

int main() {
    // Using escape sequences in string literals

    // New line
    cout << "Hello, World!\n"; // Prints "Hello, World!" and moves to the next line

    // Tab
    cout << "Name:\tJohn Doe\n"; // Prints "Name:    John Doe" with a tab space

    // Quotes
    cout << "She said, \"Hello!\"\n"; // Prints: She said, "Hello!"

    // Backslash
    cout << "This is a backslash: \\\n"; // Prints: This is a backslash: \

    // Single quote
    cout << "It\'s a sunny day!\n"; // Prints: It's a sunny day!

    // Carriage return
    cout << "12345\rABCDE\n"; // Prints: ABCDE (overwrites 12345 with ABCDE)

    // Alert (bell)
    cout << "This will make a sound if your terminal supports it:\a\n"; // May produce a sound

    return 0;
}