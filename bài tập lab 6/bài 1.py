def main():
    # Nhập số lượng phần tử của mảng từ người dùng
    n = int(input("Nhập số lượng phần tử của mảng: "))

    # Khởi tạo một danh sách để lưu trữ các phần tử
    arr = []

    # Nhập các phần tử của mảng từ người dùng
    for i in range(n):
        num = int(input(f"Nhập phần tử thứ {i + 1}: "))
        arr.append(num)

    # Tính tổng các số chẵn và các số lẻ
    sum_even = 0
    sum_odd = 0
    for num in arr:
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num

    # In kết quả
    print(f"Tổng các số chẵn trong mảng là: {sum_even}")
    print(f"Tổng các số lẻ trong mảng là: {sum_odd}")

if __name__ == "__main__":
    main()