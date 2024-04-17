def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_perfect(num):
    if num <= 1:
        return False
    divisor_sum = 1
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            divisor_sum += i
            if i != num // i:
                divisor_sum += num // i
    return divisor_sum == num

def main():
    # Nhập số lượng phần tử của mảng từ người dùng
    n = int(input("Nhập số lượng phần tử của mảng: "))

    # Khởi tạo một danh sách để lưu trữ các phần tử
    arr = []

    # Nhập các phần tử của mảng từ người dùng
    for i in range(n):
        num = int(input(f"Nhập phần tử thứ {i + 1}: "))
        arr.append(num)

    # Tìm và in ra các số nguyên tố trong mảng
    print("Các số nguyên tố trong mảng là:")
    for num in arr:
        if is_prime(num):
            print(num, end=" ")

    # Tìm và in ra các số hoàn hảo trong mảng
    print("\nCác số hoàn hảo trong mảng là:")
    for num in arr:
        if is_perfect(num):
            print(num, end=" ")

if __name__ == "__main__":
    main()