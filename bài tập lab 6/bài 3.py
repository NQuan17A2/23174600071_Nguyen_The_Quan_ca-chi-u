def main():
    # Nhập dãy số từ người dùng
    number_list = input("Nhập dãy số, cách nhau bằng dấu cách: ").split()

    # Chuyển đổi các phần tử của danh sách thành số dấu phẩy động
    number_list = [float(num) for num in number_list]

    # Tìm số lớn nhất và số nhỏ nhất
    max_number = max(number_list)
    min_number = min(number_list)

    # In kết quả
    print(f"Số lớn nhất trong dãy số là: {max_number}")
    print(f"Số nhỏ nhất trong dãy số là: {min_number}")

if __name__ == "__main__":
    main()