//SE226 – LAB#6
#include <iostream>
#include <cmath>
using namespace std;

//Task3
/*
        This function calculates the sum of the series ∑(-1)^(k+1)/k.
        The function uses a recursive approach
        and updates a global variable to store the result.
        Parameters:
        n (int): the upper limit of the summation
        Returns:
        None
 */

double result = 0.0;

double SUM(int n) {
    if ( n != 0 ) {
        result += pow(-1, n+1) / n;
        SUM(n - 1);
        return result;
    } else {
        return 0.0;
    }
}

//Task4
double SUM() {
    int N;
    cout << "Enter a value of n : " << endl;
    cin >> N;
    SUM(N);
}


int main() {
    int N;
    while (true) {
        cout << "Enter a value of n : " << endl;
        cin >> N;
        if (N < 1) {
            SUM(N);                                                                             //none already
            cout << "Invalid number, n should be greater or equal to 1 , Try again!" << endl;
        } else {
            SUM(N);
            cout << "The result is : " << result << endl;
            break;
        }
    }

    result = 0.0;

    SUM();
    cout << "The result is : " << result << endl;

    return 0;
}
