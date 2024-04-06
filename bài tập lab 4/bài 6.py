def number_to_words(number):
    # Dictionary chứa cách đọc các chữ số
    words_dict = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }

    # Chuyển số thành chuỗi và thay thế mỗi chữ số bằng từ tương ứng
    words = [words_dict[char] for char in str(number)]
    return ' '.join(words)

def main():
    try:
        number = int(input("Nhập một số: "))
        print("Kết quả in ra màn hình là:", number_to_words(number))
    except ValueError:
        print("Vui lòng nhập một số nguyên.")

if __name__ == "__main__":
    main()