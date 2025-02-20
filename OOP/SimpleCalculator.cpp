#include <iostream>
using namespace std;

float add(float a, float b) {
    return a + b;
}

float subtract(float a, float b) {
    return a - b;
}

float multiply(float a, float b) {
    return a * b;
}

float divide(float a, float b) {
    if (b != 0) {
        return a / b;
    } else {
        cout << "Cannot divide by zero." << endl;
        return 0;
    }
}

void calculator() {
    int choice;
    float num1, num2;

    cout << "Select operation:" << endl;
    cout << "1. Add" << endl;
    cout << "2. Subtract" << endl;
    cout << "3. Multiply" << endl;
    cout << "4. Divide" << endl;
    cout << "Enter choice (1/2/3/4): ";
    cin >> choice;

    cout << "Enter first number: ";
    cin >> num1;
    cout << "Enter second number: ";
    cin >> num2;

    switch (choice) {
        case 1:
            cout << "The sum is: " << add(num1, num2) << endl;
            break;
        case 2:
            cout << "The difference is: " << subtract(num1, num2) << endl;
            break;
        case 3:
            cout << "The product is: " << multiply(num1, num2) << endl;
            break;
        case 4:
            cout << "The quotient is: " << divide(num1, num2) << endl;
            break;
        default:
            cout << "Invalid input" << endl;
            break;
    }
}

int main() {
    calculator();
    return 0;
}
