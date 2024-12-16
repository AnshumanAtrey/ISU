//create a program to calculate and display student grades according to this :
//100-90 : A+
//90-80 : A
//80-70 : B+
//70-60 : B
//60-50 : C
//50-40 : D
//40-30 : E
#include <iostream>
using namespace std;
string grading(int grade){
    if(grade>90 && grade<=100){
        return "A+";
    }
    else if(grade>80 && grade<=90){
        return "A";
    }
    else if(grade>70 && grade<=80){
        return "B+";
    }
    else if(grade>60 && grade<=70){
        return "B";
    }
    else if(grade>50 && grade<=60){
        return "C";
    }
    else if(grade>40 && grade<=50){
        return "D";
    }
    else if(grade>30 && grade<=40){
        return "E";
    }
    else{
        return "Invalid grade";
    }
}
int main(){
    int grade;
    cout<<"Enter your grade : ";
    cin>>grade;
    cout<<"Your grade is : "<<grading(grade)<<endl;
    return 0;
}