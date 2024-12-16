#include <iostream> 
#include <string>
using namespace std;
string reverseString(string s){
    string revs = s;
    int n = revs.length();
    for (int i=0; i<n/2;i++){
        swap(revs[i],revs[n-i-1]);
    }
    return revs;
}
bool isPalindrome(string s){
    int n=s.length();
    for (int i = 0; i < n / 2; ++i) {
        if (s[i] != s[n - i - 1]) {
            return false;
        }
    }
    return true;
}

int main() {
    string input;
    cout << "Enter a string: ";
    cin>>input;

    int choice;
    cout << "Press 1 to reverse the string or 2 to check if it's a palindrome: ";
    cin >> choice;

    if (choice == 1) {
        string reversed = reverseString(input);
        cout << "Reversed string: " << reversed << endl;
    } else if (choice == 2) {
        if (isPalindrome(input)) {
            cout << "The string is a palindrome." << endl;
        } else {
            cout << "The string is not a palindrome." << endl;
        }
    } else {
        cout << "Invalid choice." << endl;
    }

    return 0;
}