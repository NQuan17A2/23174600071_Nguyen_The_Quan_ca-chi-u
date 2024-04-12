def count_characters(string):
    lowercase_count = 0
    uppercase_count = 0
    digit_count = 0
    special_count = 0
    
    for char in string:
        if char.islower():
            lowercase_count += 1
        elif char.isupper():
            uppercase_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            special_count += 1
    
    return lowercase_count, uppercase_count, digit_count, special_count

def main():
    string = input("Nhập chuỗi ký tự: ")
    
    lowercase_count, uppercase_count, digit_count, special_count = count_characters(string)
    
    print("Số lượng chữ thường:", lowercase_count)
    print("Số lượng chữ hoa:", uppercase_count)
    print("Số lượng chữ số:", digit_count)
    print("Số lượng ký tự đặc biệt:", special_count)

if __name__ == "__main__":
    main()