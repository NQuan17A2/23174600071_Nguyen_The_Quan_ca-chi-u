def check_arithmetic_sequence(sequence):
    # Kiểm tra xem dãy số có tạo thành cấp số cộng không
    if len(sequence) < 2:
        return False
    
    # Tính sai số giữa các phần tử liên tiếp
    common_difference = sequence[1] - sequence[0]
    
    for i in range(1, len(sequence) - 1):
        if sequence[i + 1] - sequence[i] != common_difference:
            return False
    return True, common_difference

def main():
    # Nhập dãy số từ người dùng
    sequence = list(map(int, input("Nhập dãy số, cách nhau bằng dấu cách: ").split()))

    # Kiểm tra xem dãy số tạo thành cấp số cộng hay không
    result = check_arithmetic_sequence(sequence)

    if result:
        print(f"Dãy số {sequence} tạo thành cấp số cộng với sai số {result[1]}.")
    else:
        print("Dãy số không tạo thành cấp số cộng.")

if __name__ == "__main__":
    main()