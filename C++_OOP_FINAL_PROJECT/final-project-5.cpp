#include <iostream>
using namespace std;

// Abstract base class for matrix operations
class MatrixOperation {
public:
    virtual ~MatrixOperation() {}
    virtual double** execute(double** A, double** B, int r1, int c1, int r2, int c2) = 0;
};

// Matrix Addition Operation
class AddOperation : public MatrixOperation {
public:
    double** execute(double** A, double** B, int r1, int c1, int r2, int c2) override {
        if (r1 != r2 || c1 != c2) {
            cout << "Error: Matrices must have same dimensions for addition" << endl;
            return nullptr;
        }
        
        // Allocate result matrix
        double** result = new double*[r1];
        for (int i = 0; i < r1; i++) {
            *(result + i) = new double[c1];
        }
        
        // Perform addition using pointer arithmetic
        for (int i = 0; i < r1; i++) {
            for (int j = 0; j < c1; j++) {
                *(*(result + i) + j) = *(*(A + i) + j) + *(*(B + i) + j);
            }
        }
        
        return result;
    }
};

// Matrix Multiplication Operation
class MultiplyOperation : public MatrixOperation {
public:
    double** execute(double** A, double** B, int r1, int c1, int r2, int c2) override {
        if (c1 != r2) {
            cout << "Error: A columns must equal B rows for multiplication" << endl;
            return nullptr;
        }
        
        // Allocate result matrix (r1 x c2)
        double** result = new double*[r1];
        for (int i = 0; i < r1; i++) {
            *(result + i) = new double[c2];
        }
        
        // Perform multiplication using pointer arithmetic
        for (int i = 0; i < r1; i++) {
            for (int j = 0; j < c2; j++) {
                *(*(result + i) + j) = 0;
                for (int k = 0; k < c1; k++) {
                    *(*(result + i) + j) += *(*(A + i) + k) * *(*(B + k) + j);
                }
            }
        }
        
        return result;
    }
};

// Matrix Transpose Operation
class TransposeOperation : public MatrixOperation {
public:
    double** execute(double** A, double** B, int r1, int c1, int r2, int c2) override {
        // Only use matrix A for transpose (ignore B)
        
        // Allocate result matrix (c1 x r1)
        double** result = new double*[c1];
        for (int i = 0; i < c1; i++) {
            *(result + i) = new double[r1];
        }
        
        // Perform transpose using pointer arithmetic
        for (int i = 0; i < r1; i++) {
            for (int j = 0; j < c1; j++) {
                *(*(result + j) + i) = *(*(A + i) + j);
            }
        }
        
        return result;
    }
};

// Utility functions
double** allocateMatrix(int rows, int cols) {
    double** matrix = new double*[rows];
    for (int i = 0; i < rows; i++) {
        *(matrix + i) = new double[cols];
    }
    return matrix;
}

void deallocateMatrix(double** matrix, int rows) {
    for (int i = 0; i < rows; i++) {
        delete[] *(matrix + i);
    }
    delete[] matrix;
}

void printMatrix(double** matrix, int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            cout << *(*(matrix + i) + j) << " ";
        }
        cout << endl;
    }
}

int main() {
    // Allocate matrices A and B dynamically
    int r1 = 2, c1 = 3;  // Matrix A: 2x3
    int r2 = 3, c2 = 2;  // Matrix B: 3x2
    
    double** A = allocateMatrix(r1, c1);
    double** B = allocateMatrix(r2, c2);
    
    // Initialize matrix A using pointer arithmetic
    *(*(A + 0) + 0) = 1; *(*(A + 0) + 1) = 2; *(*(A + 0) + 2) = 3;
    *(*(A + 1) + 0) = 4; *(*(A + 1) + 1) = 5; *(*(A + 1) + 2) = 6;
    
    // Initialize matrix B using pointer arithmetic
    *(*(B + 0) + 0) = 7; *(*(B + 0) + 1) = 8;
    *(*(B + 1) + 0) = 9; *(*(B + 1) + 1) = 10;
    *(*(B + 2) + 0) = 11; *(*(B + 2) + 1) = 12;
    
    cout << "Matrix A - (" << r1 << "x" << c1 << "):" << endl;
    printMatrix(A, r1, c1);
    cout << "\nMatrix B - (" << r2 << "x" << c2 << "):" << endl;
    printMatrix(B, r2, c2);
    
    // Create dynamic array of MatrixOperation pointers
    MatrixOperation** ops = new MatrixOperation*[3];
    *(ops + 0) = new AddOperation();
    *(ops + 1) = new MultiplyOperation();
    *(ops + 2) = new TransposeOperation();
    
    // Demonstrate addition: A + B (this will fail due to different dimensions)
    cout << "\nAttempting Matrix Addition (A + B):" << endl;
    double** resultAdd = (*(ops + 0))->execute(A, B, r1, c1, r2, c2);
    if (resultAdd) {
        printMatrix(resultAdd, r1, c1);
        deallocateMatrix(resultAdd, r1);
    } else {
        cout << "A + B is not possible because A is " << r1 << "x" << c1 
             << " and B is " << r2 << "x" << c2 << endl;
    }
    
    // Demonstrate multiplication: A * B
    cout << "\nMatrix Multiplication (A * B):" << endl;
    double** resultMult = (*(ops + 1))->execute(A, B, r1, c1, r2, c2);
    if (resultMult) {
        printMatrix(resultMult, r1, c2);
        deallocateMatrix(resultMult, r1);
    }
    
    // Demonstrate transpose: A^T
    cout << "\nMatrix Transpose (A^T):" << endl;
    double** resultTrans = (*(ops + 2))->execute(A, B, r1, c1, r2, c2);
    if (resultTrans) {
        printMatrix(resultTrans, c1, r1);
        deallocateMatrix(resultTrans, c1);
    }
    
    // For addition, create matrix C with same dimensions as A
    double** C = allocateMatrix(r1, c1);
    *(*(C + 0) + 0) = 1; *(*(C + 0) + 1) = 1; *(*(C + 0) + 2) = 1;
    *(*(C + 1) + 0) = 1; *(*(C + 1) + 1) = 1; *(*(C + 1) + 2) = 1;
    
    cout << "\nMatrix C - (" << r1 << "x" << c1 << "):" << endl;
    printMatrix(C, r1, c1);
    
    // Demonstrate addition: A + C (this will work)
    cout << "\nMatrix Addition (A + C):" << endl;
    double** resultAdd2 = (*(ops + 0))->execute(A, C, r1, c1, r1, c1);
    if (resultAdd2) {
        printMatrix(resultAdd2, r1, c1);
        deallocateMatrix(resultAdd2, r1);
    }
    
    // Clean up memory
    deallocateMatrix(A, r1);
    deallocateMatrix(B, r2);
    deallocateMatrix(C, r1);
    
    // Delete operations using pointer arithmetic
    for (int i = 0; i < 3; i++) {
        delete *(ops + i);
    }
    delete[] ops;
    
    return 0;
}