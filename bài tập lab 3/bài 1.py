def nhap_so_nguyen_duong():
    while True:
        n = int(input("Nhập một số nguyên dương n: "))
        if n <= 0:
            print("Vui lòng nhập số nguyên dương lớn hơn 0.")
        else:
            return n

def tinh_tong_a(n):
    tong = 0
    for i in range(1, n + 1):
        tong += i
    return tong

def tinh_tong_b(n):
    tong = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            tong += j
    return tong

def tinh_tong_c(n):
    tong = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            tong += 2 * j
        tong -= i + 1
    return tong

def tinh_tong_d(n):
    tong = 0
    for i in range(1, n + 1):
        tong += i * (i + 1)
    return tong

def main():
    n = nhap_so_nguyen_duong()
    print("a) Số tổng của dãy là:", tinh_tong_a(n))
    print("b) Số tổng của dãy là:", tinh_tong_b(n))
    print("c) Số tổng của dãy là:", tinh_tong_c(n))
    print("d) Số tổng của dãy là:", tinh_tong_d(n))

if __name__ == "__main__":
    main()