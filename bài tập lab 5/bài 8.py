def extract_substring_1(string):
    if len(string) > 10:
        return string[1:8]
    else:
        return "Chuỗi không đủ dài."

def extract_substring_2(string):
    if len(string) > 10:
        return string[4:9]
    else:
        return "Chuỗi không đủ dài."

def extract_substring_3(string):
    if len(string) > 10:
        return string[-3:]
    else:
        return "Chuỗi không đủ dài."

def convert_to_lowercase(string):
    return string.lower()

def convert_to_uppercase(string):
    return string.upper()

def reverse_string(string):
    return string[::-1]

def main():
    string = input("Nhập chuỗi ký tự (độ dài hơn 10 ký tự): ")

    if len(string) <= 10:
        print("Chuỗi không đủ dài.")
        return

    print("Chuỗi ký tự con từ vị trí 2 đến 8:", extract_substring_1(string))
    print("Chuỗi ký tự con từ vị trí 5 gồm 5 ký tự:", extract_substring_2(string))
    print("Chuỗi ký tự con từ cuối chuỗi gồm 3 ký tự:", extract_substring_3(string))
    print("Chuỗi chuyển đổi thành chữ thường:", convert_to_lowercase(string))
    print("Chuỗi chuyển đổi thành chữ hoa:", convert_to_uppercase(string))
    print("Chuỗi đảo ngược:", reverse_string(string))

if __name__ == "__main__":
    main()