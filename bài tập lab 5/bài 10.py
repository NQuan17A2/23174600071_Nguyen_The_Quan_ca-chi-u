def remove_spaces(string):
    return string.replace(" ", "")

def main():
    string = input("Nhập chuỗi ký tự: ")
    result = remove_spaces(string)
    print("Chuỗi sau khi xóa khoảng trắng:", result)

if __name__ == "__main__":
    main()