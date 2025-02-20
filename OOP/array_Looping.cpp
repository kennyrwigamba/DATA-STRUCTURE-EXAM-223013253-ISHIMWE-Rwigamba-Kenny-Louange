#include <iostream>
using namespace std;

void arrayLooping() {
    int numbers[5] = {10, 20, 30, 40, 50};
    for (int i = 0; i < 5; i++) {
        cout << numbers[i] << endl;
    }
}

int main() {
    arrayLooping();
    return 0;
}
