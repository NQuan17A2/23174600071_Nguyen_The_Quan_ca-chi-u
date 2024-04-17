def input_matrix(rows, cols):
    # Nhập ma trận từ người dùng
    matrix = []
    print("Nhập các phần tử của ma trận:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Nhập phần tử [{i + 1}][{j + 1}]: "))
            row.append(element)
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    # In ma trận ra màn hình
    for row in matrix:
        print(row)

def matrix_sum(matrix):
    # Tính tổng của các phần tử trong ma trận
    total = sum(sum(row) for row in matrix)
    return total

def matrix_product(matrix1, matrix2):
    # Tính tích của hai ma trận
    if len(matrix1[0]) != len(matrix2):
        return None
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

def transpose_matrix(matrix):
    # Tạo và in ra ma trận chuyển vị của ma trận ban đầu
    transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transpose

def main():
    # Nhập số hàng và số cột của ma trận
    m = int(input("Nhập số hàng của ma trận: "))
    n = int(input("Nhập số cột của ma trận: "))

    # Nhập ma trận từ người dùng
    matrix = input_matrix(m, n)

    # In ra ma trận vừa nhập
    print("Ma trận vừa nhập là:")
    print_matrix(matrix)

    # Tính tổng của các phần tử trong ma trận
    total = matrix_sum(matrix)
    print("Tổng của các phần tử trong ma trận là:", total)

    # Nhập ma trận thứ hai từ người dùng
    k = int(input("Nhập số hàng của ma trận thứ hai: "))
    l = int(input("Nhập số cột của ma trận thứ hai: "))
    matrix2 = input_matrix(k, l)

    # Tính tích của hai ma trận
    product = matrix_product(matrix, matrix2)
    if product is not None:
        print("Tích của hai ma trận là:")
        print_matrix(product)
    else:
        print("Không thể tính tích của hai ma trận.")

    # In ra ma trận chuyển vị của ma trận ban đầu
    transpose = transpose_matrix(matrix)
    print("Ma trận chuyển vị của ma trận ban đầu là:")
    print_matrix(transpose)

if __name__ == "__main__":
    main()