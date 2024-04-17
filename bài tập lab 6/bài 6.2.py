def input_square_matrix(n):
    # Nhập ma trận vuông từ người dùng
    matrix = []
    print("Nhập các phần tử của ma trận vuông:")
    for i in range(n):
        row = []
        for j in range(n):
            element = float(input(f"Nhập phần tử [{i + 1}][{j + 1}]: "))
            row.append(element)
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    # In ma trận ra màn hình
    for row in matrix:
        print(row)

def matrix_transpose(matrix):
    # Tạo và in ra ma trận chuyển vị của ma trận ban đầu
    transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transpose

def matrix_inverse(matrix):
    # Tìm ma trận nghịch đảo của ma trận vuông
    determinant = determinant_of_matrix(matrix)
    if determinant == 0:
        return None
    else:
        n = len(matrix)
        adjoint_matrix = adjoint_of_matrix(matrix)
        inverse_matrix = [[adjoint_matrix[i][j] / determinant for j in range(n)] for i in range(n)]
        return inverse_matrix

def determinant_of_matrix(matrix):
    # Tính định thức của ma trận vuông
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        determinant = 0
        for j in range(n):
            determinant += matrix[0][j] * cofactor(matrix, 0, j)
        return determinant

def cofactor(matrix, i, j):
    # Tính phần tử của ma trận phụ hợp
    sign = (-1) ** (i + j)
    minor_matrix = minor(matrix, i, j)
    minor_determinant = determinant_of_matrix(minor_matrix)
    return sign * minor_determinant

def minor(matrix, i, j):
    # Tạo ma trận con bằng cách loại bỏ dòng và cột chứa phần tử (i, j)
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]

def adjoint_of_matrix(matrix):
    # Tính ma trận phụ hợp của ma trận vuông
    n = len(matrix)
    adjoint = [[cofactor(matrix, i, j) for j in range(n)] for i in range(n)]
    return matrix_transpose(adjoint)

def is_symmetric(matrix):
    # Kiểm tra xem ma trận đã cho có phải là ma trận đối xứng hay không
    return matrix == matrix_transpose(matrix)

def main():
    # Nhập kích thước của ma trận vuông
    n = int(input("Nhập kích thước của ma trận vuông: "))

    # Nhập ma trận vuông từ người dùng
    square_matrix = input_square_matrix(n)

    # In ra ma trận vuông vừa nhập
    print("Ma trận vuông vừa nhập là:")
    print_matrix(square_matrix)

    # Tìm và in ra ma trận nghịch đảo của ma trận vuông
    inverse = matrix_inverse(square_matrix)
    if inverse is not None:
        print("Ma trận nghịch đảo của ma trận vuông là:")
        print_matrix(inverse)
    else:
        print("Ma trận không có ma trận nghịch đảo.")

    # Kiểm tra xem ma trận đã cho có phải là ma trận đối xứng hay không
    if is_symmetric(square_matrix):
        print("Ma trận đã cho là ma trận đối xứng.")
    else:
        print("Ma trận đã cho không là ma trận đối xứng.")

if __name__ == "__main__":
    main()