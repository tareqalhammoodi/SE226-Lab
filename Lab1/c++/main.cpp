//SE226 – LAB#1
#include <iostream>
#include <string>
using namespace std;
int main() {
    //Exercise-1
    string UserName;
    cout << "What is your name? ";
    cin  >> UserName;
    cout << "Hello " + UserName + ". \n";
    int StudentID;
    cout << "What is your Student ID? ";
    cin  >> StudentID;
    cout << "Your ID is " << StudentID << "\n\n";
    //Exercise-2
    int var1;
    cout << "Please enter the first number : \n";
    cin  >> var1;
    int var2;
    cout << "Please enter the second number : \n";
    cin  >> var2;
    int sum  = var1 + var2;
    int diff = var1 - var2;
    int prod = var1 * var2;
    cout << "The value of the first variable is :" << var1 << "\n";
    cout << "The value of the second variable is :" << var2 << "\n";
    cout << "The summation of the two variables is : " << sum << "\n";
    cout << "The difference of the two variables is : " << diff << "\n";
    cout << "The multiplication of the two variables is : " << prod << "\n\n";
    //Exercise-3
    string StudentName;
    cout << "Please enter your Full Name : ";
    cin  >> StudentName;
    int labGrade;
    cout << "Please enter your Lab grade : ";
    cin  >> labGrade;
    int midtermGrade;
    cout << "Please enter your Midterm grade : ";
    cin  >> midtermGrade;
    int finalGrade;
    cout << "Please enter your Final grade : ";
    cin  >> finalGrade;
    float lastScore      = (((float)labGrade * 25 / 100) + ((float)midtermGrade * 35 / 100) + ((float)finalGrade * 40 / 100));
    cout << "Name:       " << StudentName   << "\n"
         << "Lab:        " << labGrade      << "\n"
         << "Midterm:    " << midtermGrade  << "\n"
         << "Final:      " << finalGrade    << "\n"
         << "Last score: " << lastScore     << "\n\n";
    //Exercise-4
    cout << "*"     << "\n"
         << "**"    << "\n"
         << "***"   << "\n"
         << "**"    << "\n"
         << "*"     << "\n";
    return 0;
}
