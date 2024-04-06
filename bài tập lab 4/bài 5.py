import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Không thể chia cho 0!"
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        return "Không thể tính căn bậc hai của số âm!"
    return math.sqrt(a)

def main():
    while True:
        try:
            num1 = float(input("Nhập số thứ nhất: "))
            num2 = float(input("Nhập số thứ hai: "))
        except ValueError:
            print("Vui lòng nhập số hợp lệ.")
            continue
        
        print("a) Tổng:", add(num1, num2))
        print("b) Hiệu:", subtract(num1, num2))
        print("c) Tích:", multiply(num1, num2))
        print("d) Thương:", divide(num1, num2))
        print("e) Lũy thừa:", power(num1, num2))
        print("f) Căn bậc hai của số thứ nhất:", square_root(num1))
        print("g) Căn bậc hai của số thứ hai:", square_root(num2))
        
        choice = input("Bạn có muốn tiếp tục không? (yes/no): ")
        if choice.lower() != 'yes':
            break

if __name__ == "__main__":
    main()