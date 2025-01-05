#include <iostream>

int main() {
    // For Loop
    for (int i = 0; i < 5; i++) {
        // Code to execute in each iteration
        std::cout << "For Loop iteration: " << i << std::endl;
    }

    // While Loop
    int j = 0;
    while (j < 5) {
        // Code to execute in each iteration
        std::cout << "While Loop iteration: " << j << std::endl;
        j++;
    }

    // Do-While Loop
    int k = 0;
    do {
        // Code to execute in each iteration
        std::cout << "Do-While Loop iteration: " << k << std::endl;
        k++;
    } while (k < 5);

    return 0;
}
