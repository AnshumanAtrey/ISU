#include <iostream>
using namespace std;

// Function to calculate the nth Fibonacci number using recursion
int fibonacci(int n) {
    // Base cases: return n for 0 and 1
    if (n == 0) {
        return 0;
    } else if (n == 1) {
        return 1;
    }
    // Recursive case: sum of the two preceding numbers
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    int N;
    cout << "Enter the number of terms in Fibonacci series: ";
    cin >> N;

    cout << "Fibonacci series: ";
    for (int i = 0; i < N; i++) {
        cout << fibonacci(i) << " "; // Print each Fibonacci number
    }
    cout << endl;

    return 0;
} 