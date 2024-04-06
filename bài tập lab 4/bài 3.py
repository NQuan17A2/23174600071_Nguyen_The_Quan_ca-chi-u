def count_digits(number):
    count = 0
    while number != 0:
        count += 1
        number //= 10
    return count

def main():
    number = int(input("Nhập vào một số nguyên: "))
    digit_count = count_digits(abs(number))
    print("Số chữ số của số nguyên:", digit_count)

if __name__ == "__main__":
    main()