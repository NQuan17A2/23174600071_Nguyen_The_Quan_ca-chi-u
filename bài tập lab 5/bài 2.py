def shortest_common_substring(str1, str2):
    m = len(str1)
    n = len(str2)
    
    # Tạo một bảng để lưu trữ độ dài của chuỗi con chung và độ dài của chuỗi con chung ngắn nhất
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0
    end_index = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i
            else:
                dp[i][j] = 0

    if max_length == 0:
        return ""

    return str1[end_index - max_length:end_index]

def main():
    str1 = input("Nhập chuỗi ký tự thứ nhất: ")
    str2 = input("Nhập chuỗi ký tự thứ hai: ")

    shortest_substring = shortest_common_substring(str1, str2)

    if shortest_substring:
        print("Chuỗi ký tự con chung ngắn nhất là:", shortest_substring)
    else:
        print("Không có chuỗi ký tự con chung.")

if __name__ == "__main__":
    main()