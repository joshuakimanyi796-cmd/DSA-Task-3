SAMPLE = [
    [0, 0, 0, 0, 9, 0],
    [0, 8, 0, 0, 0, 0],
    [4, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 5, 0, 0, 0],
]


def to_sparse(matrix):
    """Convert an ordinary 2-D list into the triplet representation."""
    rows, cols = len(matrix), len(matrix[0])
    sparse = [[rows, cols, 0]]                      # header row
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 0:
                sparse.append([i, j, matrix[i][j]])
    sparse[0][2] = len(sparse) - 1                  # count of non-zero values
    return sparse


def to_dense(sparse):
    """Rebuild the full matrix from its triplet form (used to verify the result)."""
    rows, cols, _ = sparse[0]
    matrix = [[0] * cols for _ in range(rows)]
    for r, c, v in sparse[1:]:
        matrix[r][c] = v
    return matrix


def print_matrix(matrix):
    width = max(len(str(v)) for row in matrix for v in row)
    for row in matrix:
        print("   " + "  ".join(str(v).rjust(width) for v in row))


def print_sparse(sparse):
    print("   Row   Column   Value")
    print("   ---   ------   -----")
    for i, (r, c, v) in enumerate(sparse):
        tag = "   <- (rows, columns, non-zero count)" if i == 0 else ""
        print(f"   {r:>3}   {c:>6}   {v:>5}{tag}")


def read_matrix():
    """Read a matrix from the user; pressing Enter at the first prompt uses a demo matrix."""
    first = input("Enter number of rows (or press Enter to use a demo matrix): ").strip()
    if first == "":
        return [row[:] for row in SAMPLE]

    rows = int(first)
    cols = int(input("Enter number of columns: "))
    print(f"Enter the matrix row by row ({cols} numbers per row, separated by spaces):")
    matrix = []
    while len(matrix) < rows:
        line = input(f"  Row {len(matrix)}: ").replace(",", " ").split()
        try:
            values = [int(x) for x in line]
        except ValueError:
            print("  Numbers only, please retry this row.")
            continue
        if len(values) != cols:
            print(f"  Expected {cols} numbers, got {len(values)}. Retry this row.")
            continue
        matrix.append(values)
    return matrix


def main():
    matrix = read_matrix()
    rows, cols = len(matrix), len(matrix[0])

    print("\nOriginal matrix:")
    print_matrix(matrix)

    sparse = to_sparse(matrix)
    nonzero = sparse[0][2]
    total = rows * cols

    print("\nSparse (triplet) representation:")
    print_sparse(sparse)

    dense_cells = total
    sparse_cells = 3 * len(sparse)
    print(f"\nNon-zero elements : {nonzero} of {total}  "
          f"({100 * (total - nonzero) / total:.1f}% zeros)")
    print(f"Memory (cells)    : ordinary matrix = {dense_cells}, triplet array = {sparse_cells}")
    if sparse_cells < dense_cells:
        print(f"Saving            : {dense_cells - sparse_cells} cells "
              f"({100 * (dense_cells - sparse_cells) / dense_cells:.1f}%)")
    else:
        print("This matrix is not sparse enough for the triplet form to save memory.")

    print("\nCheck - matrix rebuilt from the triplet array:")
    print_matrix(to_dense(sparse))
    print("Rebuilt matrix equals original:", to_dense(sparse) == matrix)


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nProgram ended.")
    except ValueError:
        print("\nInvalid input - please enter whole numbers only.")
