def merge_strings(string1, string2):
    merged_string = ''
    min_length = min(len(string1), len(string2))
    
    for i in range(min_length):
        merged_string += string1[i] + '-' + string2[i] + '-'
    
    if len(string1) > min_length:
        merged_string += '-'.join(string1[min_length:]) + '-'
    elif len(string2) > min_length:
        merged_string += '-'.join(string2[min_length:]) + '-'
    
    # Loại bỏ dấu gạch nối cuối cùng nếu có
    if merged_string.endswith('-'):
        merged_string = merged_string[:-1]
    
    return merged_string

def main():
    string1 = input("Nhập chuỗi ký tự thứ nhất: ")
    string2 = input("Nhập chuỗi ký tự thứ hai: ")

    merged_string = merge_strings(string1, string2)

    print("Chuỗi kết quả sau khi trộn:", merged_string)

if __name__ == "__main__":
    main()