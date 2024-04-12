def remove_non_numeric_characters(text):
    numeric_text = ''.join(char for char in text if char.isdigit())
    return numeric_text

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def main():
    text = input("Nhập chuỗi ký tự: ")

    numeric_text = remove_non_numeric_characters(text)

    if numeric_text:
        number = int(numeric_text)
        if is_prime(number):
            print("Chuỗi ký tự sau khi loại bỏ:", numeric_text)
            print("Chuỗi ký tự là một số nguyên tố.")
        else:
            print("Chuỗi ký tự sau khi loại bỏ:", numeric_text)
            print("Chuỗi ký tự không phải là số nguyên tố.")
    else:
        print("Không có số nguyên trong chuỗi ký tự.")

if __name__ == "__main__":
    main()