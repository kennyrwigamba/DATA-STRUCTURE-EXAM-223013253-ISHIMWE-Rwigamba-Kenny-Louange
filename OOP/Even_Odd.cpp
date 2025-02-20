#include <iostream>
using namespace std;

void checkEvenOrOdd() {
    int number;
    cout << "Enter a number: ";
    cin >> number;
    if (number % 2 == 0) {
        cout << number << " is even." << endl;
    } else {
        cout << number << " is odd." << endl;
    }
}

int main() {
    checkEvenOrOdd();
    return 0;
}
