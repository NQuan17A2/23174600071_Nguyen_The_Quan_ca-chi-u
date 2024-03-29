# A
def kiem_tra_so_nguyen_to(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def in_so_nguyen_to_tu_100_den_1000():
    print("Các số nguyên tố từ 100 đến 1000:")
    for num in range(100, 1001):
        if kiem_tra_so_nguyen_to(num):
            print(num, end=" ")

in_so_nguyen_to_tu_100_den_1000()

# B
def kiem_tra_so_chinh_phuong(num):
    return num == int(num ** 0.5) ** 2

def in_so_chinh_phuong_tu_1_den_1000():
    print("Các số chính phương từ 1 đến 1000:")
    for num in range(1, 1001):
        if kiem_tra_so_chinh_phuong(num):
            print(num, end=" ")

in_so_chinh_phuong_tu_1_den_1000()

# C
def in_chuoi_fibonacci():
    a, b = 0, 1
    print("Chuỗi Fibonacci sao cho số cuối cùng trong chuỗi nhỏ hơn 100:")
    while a < 100:
        print(a, end=" ")
        a, b = b, a + b

in_chuoi_fibonacci()

# D
def kiem_tra_so_hoan_hao(num):
    tong_uoc = 0
    for i in range(1, num):
        if num % i == 0:
            tong_uoc += i
    return tong_uoc == num

def in_so_hoan_hao_be_hon_500():
    print("Các số hoàn hảo nhỏ hơn 500:")
    for num in range(2, 500):
        if kiem_tra_so_hoan_hao(num):
            print(num, end=" ")

in_so_hoan_hao_be_hon_500()

# E
def tinh_so_ngu_giac(n):
    return n * (3 * n - 1) // 2

def tinh_tong_so_ngu_giac():
    tong = 0
    for i in range(1, 201):
        tong += tinh_so_ngu_giac(i)
    return tong

print("Tổng của các số ngũ giác trong đoạn từ 1 đến 200 là:", tinh_tong_so_ngu_giac())