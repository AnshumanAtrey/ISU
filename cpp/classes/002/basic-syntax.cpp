//header file
#include <iostream> 

//standerd namespace
//By including this directive, the compiler knows to look for identifiers (like cout, cin, string, etc.) in the std namespace automatically, simplifying the code.
using namespace std;

//main function 
int main(){
    //declare variables
    int num1, num2, sum;
    //input values
    cout << "Enter first number: ";
    cin >> num1;
    cout << "Enter second number: ";
    cin >> num2;
    //expressions
    sum = num1 + num2;
    //output result
    cout << "Sum of two numbers is: " << sum;
    //return statement
    return 0;
}