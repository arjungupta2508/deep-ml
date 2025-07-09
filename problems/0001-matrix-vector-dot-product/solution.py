def matrix_dot_vector(matrix: list[list[int | float]], vector: list[int | float]) -> list[int | float] | int:
    # Check if matrix is not empty and all rows are the same length
    if not matrix or not all(len(row) == len(matrix[0]) for row in matrix):
        return -1
    
    num_cols = len(matrix[0])
    if len(vector) != num_cols:
        return -1

    # Perform dot product manually
    result = []
    for row in matrix:
        dot_product = sum(row[i] * vector[i] for i in range(num_cols))
        result.append(dot_product)
    
    return result
