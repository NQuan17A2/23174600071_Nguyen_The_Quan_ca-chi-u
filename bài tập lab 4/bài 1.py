def main():
    numbers = []
    while True:
        num = int(input("Nhập một số nguyên dương: "))
        if num <= 0:
            print("Số bạn nhập không hợp lệ. Hãy nhập lại.")
            continue
        numbers.append(num)
        if sum(numbers) > 1000:
            break

    odd_numbers = [x for x in numbers if x % 2 != 0]
    even_numbers = [x for x in numbers if x % 2 == 0]

    print("Các số đã nhập từ bàn phím là:", " ".join(map(str, numbers)))
    print("Các số lẻ đã nhập là:", " ".join(map(str, odd_numbers)))
    print("Các số chẵn đã nhập:", " ".join(map(str, even_numbers)))
    print("Số lượng các số nguyên đã nhập:", len(numbers))

if __name__ == "__main__":
    main()


    