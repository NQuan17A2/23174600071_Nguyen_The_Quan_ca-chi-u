def can_transform_string(string1, string2):
    # Độ dài của hai chuỗi
    len1 = len(string1)
    len2 = len(string2)
    
    # Nếu độ dài hai chuỗi khác nhau quá xa, không thể thay đổi
    if abs(len1 - len2) > 1:
        return False
    
    # Nếu hai chuỗi có cùng độ dài, kiểm tra xem có thể chỉ cần thay đổi một ký tự hay không
    if len1 == len2:
        diff_count = 0
        for i in range(len1):
            if string1[i] != string2[i]:
                diff_count += 1
            if diff_count > 1:
                return False
        return diff_count == 1
    
    # Nếu hai chuỗi có độ dài khác nhau một ký tự, kiểm tra xem có thể chỉ cần thêm hoặc xóa một ký tự
    shorter = min(len1, len2)
    longer = max(len1, len2)
    i = j = 0
    diff_count = 0
    while i < shorter and j < longer:
        if string1[i] != string2[j]:
            diff_count += 1
            if len1 < len2:
                j += 1
            elif len1 > len2:
                i += 1
        else:
            i += 1
            j += 1
        if diff_count > 1:
            return False
    return True

def main():
    string1 = input("Nhập chuỗi ký tự thứ nhất: ")
    string2 = input("Nhập chuỗi ký tự thứ hai: ")

    if can_transform_string(string1, string2):
        print("Có thể thay đổi chuỗi '{}' thành chuỗi '{}'.".format(string1, string2))
    else:
        print("Không thể thay đổi chuỗi '{}' thành chuỗi '{}'.".format(string1, string2))

if __name__ == "__main__":
    main()