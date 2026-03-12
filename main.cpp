#include <iostream>
using namespace std;

int main()
{
    int n;
    // TODO: ask user for input
    cin >> n;

    // TODO: outer loop for each row
    for (int row = 1; row <= n; row++) {
        // TODO: inner loop to print letters for this row
        for (int col = 0; col < row; col++) {
            if (col > 0) cout << " ";
            // TODO: print the letter for this column
            cout << (char)('A' + col);
        }
        // TODO: print newline after each row
        cout << endl;
    }

    return 0;
}
