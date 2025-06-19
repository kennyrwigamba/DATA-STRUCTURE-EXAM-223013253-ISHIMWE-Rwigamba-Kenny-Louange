# 34. Matrix Operations Suite

Simple C++ program that performs matrix operations using inheritance and polymorphism.

## How It Works

1. **Creates matrices** using dynamic memory (`double**`)
2. **Uses inheritance** - one base class, three derived operation classes
3. **Demonstrates polymorphism** - stores operations in array and calls them
4. **Uses pointer arithmetic** - accesses elements with `*(*(matrix + i) + j)`

## Operations

- **Addition**: Adds two matrices (must be same size)
- **Multiplication**: Multiplies two matrices (A columns = B rows)
- **Transpose**: Flips matrix rows and columns

## Example Output

```
Matrix A (2x3):
1 2 3
4 5 6

Matrix B (3x2):
7 8
9 10
11 12

A + B: Not possible (different sizes)
A * B: Works (2x2 result)
A^T: Works (3x2 result)
```
