
def reshape_matrix(a: list[list[int | float]], new_shape: tuple[int, int]):
    old_rows = len(a)
    old_cols = len(a[0])
    new_rows, new_cols = new_shape

    # Check if reshaping is possible
    if old_rows * old_cols != new_rows * new_cols:
        
        return []

    

    # Collect all elements in row-wise order
    all_values = []
    for row in a:
        all_values.extend(row)

    # Rebuild new matrix row by row
    reshaped = []
    idx = 0
    for i in range(new_rows):
        row = []
        for j in range(new_cols):
            row.append(all_values[idx])
            idx += 1
        reshaped.append(row)

    return reshaped
