#include <iostream>
#include <string>
using namespace std;

class BankAccount {
private:
    string accountHolder; // Name of the account holder
    double balance;        // Current balance of the account

public:
    // Constructor to initialize account holder and balance
    BankAccount(string name, double initialBalance) {
        accountHolder = name;
        balance = initialBalance;
    }

    // Method to deposit money into the account
    void credit(double amount) {
        if (amount > 0) {
            balance += amount; // Increase balance
            cout << "Deposited: $" << amount << endl;
        } else {
            cout << "Invalid deposit amount." << endl;
        }
    }

    // Method to withdraw money from the account
    void debit(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount; // Decrease balance
            cout << "Withdrawn: $" << amount << endl;
        } else if (amount > balance) {
            cout << "Insufficient funds." << endl;
        } else {
            cout << "Invalid withdrawal amount." << endl;
        }
    }

    // Method to display account details
    void displayAccountInfo() const {
        cout << "Account Holder: " << accountHolder << endl;
        cout << "Current Balance: $" << balance << endl;
    }
};

int main() {
    // Create a BankAccount object
    BankAccount account("John Doe", 1000.0);

    // Display initial account information
    account.displayAccountInfo();

    // Perform some transactions
    account.credit(500.0); // Deposit
    account.debit(200.0);  // Withdraw
    account.debit(1500.0); // Attempt to withdraw more than balance

    // Display updated account information
    account.displayAccountInfo();

    return 0;
}