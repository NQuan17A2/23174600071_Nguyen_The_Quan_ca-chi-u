def decimal_to_binary(decimal):
    if decimal == 0:
        return '0'
    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary

def main():
    decimal_number = int(input("Nhập số nguyên dương (hệ thập phân): "))
    if decimal_number < 0:
        print("Vui lòng nhập số nguyên dương.")
        return
    binary_number = decimal_to_binary(decimal_number)
    print("Số nhị phân tương ứng là:", binary_number)

if __name__ == "__main__":
    main()