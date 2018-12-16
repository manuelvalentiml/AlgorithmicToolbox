#include <iostream>
#include <vector>

using std::vector;
using std::cin;
using std::cout;

int max_pairwise_product_naive(const vector<int>& numbers) {
    int result  = 0;
    int n = numbers.size();
    for (int i = 0; i < n; ++i) {
        for (int j = i+1; j < n; ++j) {
            int new_mult = numbers[i] * numbers[j];
            if (new_mult > result) {
                result = new_mult;
            }
        }
    }
    return result;
}

int main() {
    int n;
    cin >> n;
    vector<int> numbers(n);
    for (int i = 0; i < n; ++i) {
        cin >> numbers[i];
    }

    int result = max_pairwise_product_naive(numbers);
    cout << result << "\n";
    return 0;
}