from functools import reduce

def perform_matrix_operation(matrices, operation):
    result = reduce(operation, matrices)
    return result

def sum_matrices(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def multiply_matrices(matrix1, matrix2):
    return [[sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix1))) for j in range(len(matrix2[0]))] for i in range(len(matrix1))]

def get_operation():
    print("Wybierz operację na macierzach:")
    print("1. Suma")
    print("2. Iloczyn")
    print("3. Niestandardowa operacja (wprowadź własną)")
    choice = input("Wybór operacji: ")

    if choice == "1":
        return sum_matrices
    elif choice == "2":
        return multiply_matrices
    elif choice == "3":
        print("Wprowadź niestandardową funkcję operacyjną:")
        def custom_operation(matrix1, matrix2):
            return [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
        return custom_operation
    else:
        print("Nieprawidłowy wybór. Użyję domyślnie sumy.")
        return sum_matrices


def main():
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]
    matrix3 = [[9, 10], [11, 12]]

    matrices = [matrix1, matrix2, matrix3]
    operation = get_operation()
    result = perform_matrix_operation(matrices, operation)

    print(f"Wynik operacji:")
    for row in result:
        print(row)

if __name__ == "__main__":
    main()
