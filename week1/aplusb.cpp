#include <iostream>

int aplusb(int a, int b) {
    return a + b;
}

int main() {
    int a = 0;
    int b = 0;
    std::cin >> a;
    std::cin >> b;
    std::cout << aplusb(a, b);
    return 0;
}