#include <iostream>
#include <vector>

using namespace std;

void displayMatrix(const vector<vector<int>>& matrix) {
    for (const auto& row : matrix) {
        for (int val : row) {
            cout << val << " ";
        }
        cout << endl;
    }
}

vector<vector<int>> addMatrices(const vector<vector<int>>& A, const vector<vector<int>>& B) {
    int rows = A.size();
    int cols = A[0].size();
    vector<vector<int>> result(rows, vector<int>(cols, 0));

    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            result[i][j] = A[i][j] + B[i][j];
        }
    }
    return result;
}

vector<vector<int>> multiplyMatrices(const vector<vector<int>>& A, const vector<vector<int>>& B) {
    int rowsA = A.size();
    int colsA = A[0].size();
    int colsB = B[0].size();
    vector<vector<int>> result(rowsA, vector<int>(colsB, 0));

    for (int i = 0; i < rowsA; ++i) {
        for (int j = 0; j < colsB; ++j) {
            for (int k = 0; k < colsA; ++k) {
                result[i][j] += A[i][k] * B[k][j];
            }
        }
    }
    return result;
}

int main() {
    vector<vector<int>> A = {{1, 2, 3}, {4, 5, 6}};
    vector<vector<int>> B = {{7, 8, 9}, {10, 11, 12}};

    cout << "Matrix A:" << endl;
    displayMatrix(A);

    cout << "Matrix B:" << endl;
    displayMatrix(B);

    vector<vector<int>> sum = addMatrices(A, B);
    cout << "Sum of A and B:" << endl;
    displayMatrix(sum);

    vector<vector<int>> product = multiplyMatrices(A, B);
    cout << "Product of A and B:" << endl;
    displayMatrix(product);

    return 0;
}
