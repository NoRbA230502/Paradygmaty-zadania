def validate_and_execute(operation):
    try:
        if not isinstance(operation, str):
            raise ValueError("Operacja musi być ciągiem znaków (string).")
        allowed_operations = {"+", "@", "T"}

        tokens = operation.split()
        if len(tokens) < 3 and "T" not in tokens:
            raise ValueError("Nieprawidłowy format operacji.")

        matrices = {
            "A": [[1, 2], [3, 4]],
            "B": [[5, 6], [7, 8]],
            "C": [[1, 0], [0, 1]]
        }

        matrix_1 = matrices.get(tokens[0])
        if matrix_1 is None:
            raise ValueError(f"Macierz {tokens[0]} nie istnieje.")


        if "T" in tokens:
            return [[row[i] for row in matrix_1] for i in range(len(matrix_1[0]))]


        matrix_2 = matrices.get(tokens[2])
        if matrix_2 is None:
            raise ValueError(f"Macierz {tokens[2]} nie istnieje.")


        operation_type = tokens[1]
        if operation_type not in allowed_operations:
            raise ValueError(f"Nieznana operacja: {operation_type}.")


        if operation_type == "+":
            if len(matrix_1) != len(matrix_2) or len(matrix_1[0]) != len(matrix_2[0]):
                raise ValueError("Macierze muszą mieć takie same wymiary do dodawania.")
            return [[matrix_1[i][j] + matrix_2[i][j] for j in range(len(matrix_1[0]))] for i in range(len(matrix_1))]

        elif operation_type == "@":
            if len(matrix_1[0]) != len(matrix_2):
                raise ValueError("Liczba kolumn pierwszej macierzy musi równać się liczbie wierszy drugiej macierzy do mnożenia.")
            return [[sum(matrix_1[i][k] * matrix_2[k][j] for k in range(len(matrix_2))) for j in range(len(matrix_2[0]))] for i in range(len(matrix_1))]

    except Exception as e:
        return str(e)


if __name__ == "__main__":
    print("Dodawanie macierzy A + B:")
    print(validate_and_execute("A + B"))
    print("Mnożenie macierzy A @ C:")
    print(validate_and_execute("A @ C"))
    print("Transponowanie macierzy A T:")
    print(validate_and_execute("A T"))
