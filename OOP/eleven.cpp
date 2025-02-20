#include <iostream>
using namespace std;

int add(int a, int b) {
    return a + b;
}

int main() {
    int sum = add(25, 10);
    cout << "The sum is: " << sum << endl;
    return 0;
}
