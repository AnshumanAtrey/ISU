#include <iostream>
using namespace std;

// Function to calculate the sum of first N natural numbers using recursion
int sumNaturalNumbers(int n) {
    // Base case: if n is 0, return 0
    if (n == 0) {
        return 0;
    }
    // Recursive case: add n to the sum of first (n-1) natural numbers
    return n + sumNaturalNumbers(n - 1);
}

int main() {
    int N;
    cout << "Enter a positive integer N: ";
    cin >> N;

    // Calculate and display the sum
    int sum = sumNaturalNumbers(N);
    cout << "Sum of first " << N << " natural numbers is: " << sum << endl;

    return 0;
} 