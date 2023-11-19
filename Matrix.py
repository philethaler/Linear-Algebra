def main():
    # (c) Provide 10 sample square matrices for testing
    sample_matrices = [
        [[2, 1], [4, 3]],          # Invertible matrix
        [[1, 2], [2, 4]],          # Singular matrix
        [[1, 0, 0], [0, 2, 0], [0, 0, 3]],  # Invertible diagonal matrix
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],  # Singular matrix
        [[1, 0], [0, 1]],          # Invertible identity matrix
        [[0, 0], [0, 0]],          # Singular zero matrix
        [[1, 2, 3], [0, 1, 4], [5, 6, 0]],  # Invertible matrix
        [[1, 1, 1], [0, 1, 1], [0, 0, 0]],  # Singular upper triangular matrix
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],  # Singular matrix
        [[1, 1], [1, 1]],          # Singular matrix
        [[1, 2, 3], [0, 1, 4], [5, 6, 0]] #Exercise 3
    ]

    for i, matrix in enumerate(sample_matrices):
        print(f"Matrix {i + 1}:")
        try:
            inverse = matrix_inverse(matrix)
            print("Inverse:")
            for row in inverse:
                print(row)
        except ValueError as e:
            print(f"Error: {e}")
        print("=" * 30)

    # Take a coefficient matrix A and a right-hand side vector b as inputs
    A = input_matrix()
    b = list(map(float, input("Please enter a right-hand side vector b separated by space: ").split()))

    print("Coefficient Matrix A:")
    for row in A:
        print(row)
    print("Right-hand side vector b:", b)

    # Use the inverse to solve the linear system Ax = b
    solution = solve_linear_system(A, b)
    print("Linear System Solution:")
    print(solution)


def is_invertible(matrix):
    # Check if the matrix is a square matrix
    if len(matrix) != len(matrix[0]):
        return False

    # Check if the determinant is non-zero
    det = matrix_determinant(matrix)
    return det != 0

def matrix_minor(matrix, row, column):
    # Create a minor matrix by excluding the specified row and column so that the calculating of the determinant is easier
    result = []
    for i in range(len(matrix)):
        if i != row:
            minor_row = []
            for j in range(len(matrix[i])):
                if j != column:
                    minor_row.append(matrix[i][j])
            result.append(minor_row)
    return result


def matrix_determinant(matrix):
    #us the matrix_minor function to determine the determinant of the matrix
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for i in range(n):
            det += ((-1) ** i) * matrix[0][i] * matrix_determinant(matrix_minor(matrix, 0, i))
        return det



def matrix_inverse(matrix):
    if not is_invertible(matrix):
        raise ValueError("Matrix is singular and therefore not invertible.")

    n = len(matrix)
    identity_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        identity_matrix[i][i] = 1

    # Perform Gaussian elimination to transform the left half into the identity matrix
    for i in range(n):
        # Make all the diagonal elements 1
        diag_element = matrix[i][i]
        for j in range(n):
            matrix[i][j] /= diag_element
            identity_matrix[i][j] /= diag_element

        for k in range(n):
            if i != k:
                factor = matrix[k][i]
                for j in range(n):
                    matrix[k][j] -= factor * matrix[i][j]
                    identity_matrix[k][j] -= factor * identity_matrix[i][j]

    return identity_matrix

def solve_linear_system(A, b):
    try:
        A_inv = matrix_inverse(A)
        x = [sum(A_inv[i][j] * b[j] for j in range(len(b))) for i in range(len(A_inv))]
        return x
    except ValueError as e:
        return str(e)
    

def input_matrix():
    while True:
        try:
            n = int(input("Please enter the size of the square matrix: "))

            if n <= 0:
                raise ValueError("Invalid size. Please use a positive number.")

            matrix = []
            for i in range(n):
                row = list(map(float, input(f"Please enter values for row {i + 1} separated by space: ").split()))

                if len(row) != n:
                    raise ValueError("Invalid number of elements in the row.")
                matrix.append(row)

            return matrix
        except ValueError as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
