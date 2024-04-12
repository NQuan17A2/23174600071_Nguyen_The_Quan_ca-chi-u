def find_word_positions(text, word):
    positions = []
    start = 0
    while True:
        start = text.find(word, start)
        if start == -1:
            break
        positions.append(start)
        start += 1
    return positions

def most_frequent_word(text):
    words = text.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    most_frequent = max(word_count, key=word_count.get)
    return most_frequent

def main():
    text = input("Nhập chuỗi văn bản: ")
    word_to_find = input("Nhập từ cần tìm kiếm: ")

    positions = find_word_positions(text, word_to_find)

    if positions:
        print("Vị trí của từ '{}' trong chuỗi:".format(word_to_find), positions)
    else:
        print("Từ '{}' không xuất hiện trong chuỗi.".format(word_to_find))

    most_frequent = most_frequent_word(text)
    print("Từ xuất hiện nhiều nhất trong chuỗi là:", most_frequent)

if __name__ == "__main__":
    main()