def count_special_characters(string):
    special_characters = {}
    total_characters = len(string)
    
    for char in string:
        if not char.isalnum():
            if char in special_characters:
                special_characters[char] += 1
            else:
                special_characters[char] = 1
    
    return special_characters, total_characters

def calculate_percentage(character_count, total_characters):
    percentage = {}
    
    for char, count in character_count.items():
        percentage[char] = (count / total_characters) * 100
    
    return percentage

def main():
    string = input("Nhập chuỗi ký tự: ")
    
    special_characters, total_characters = count_special_characters(string)
    
    if special_characters:
        print("Các ký tự đặc biệt và số lần xuất hiện:")
        for char, count in special_characters.items():
            print("Ký tự '{}' xuất hiện {} lần".format(char, count))
        
        percentages = calculate_percentage(special_characters, total_characters)
        print("\nTỷ lệ phần trăm của mỗi ký tự đặc biệt:")
        for char, percent in percentages.items():
            print("Ký tự '{}' chiếm {:.2f}%".format(char, percent))
    else:
        print("Không có ký tự đặc biệt trong chuỗi.")

if __name__ == "__main__":
    main()