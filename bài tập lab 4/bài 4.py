def main():
    n = int(input("Nhập vào số nguyên n (n > 10): "))
    
    # Tính tổng a
    a_sum = 0
    a = 1
    while a_sum <= n:
        a_sum += a * 6
        a += 1
    
    # Tính tổng b
    b_sum = 0
    b = 1
    while b_sum <= n:
        b_sum += b
        b += 1
    
    # Tính tổng c
    c_sum = 0
    c = 1
    while c_sum <= n:
        c_sum += c * 3
        c += 1
    
    # Tính tổng d
    d_sum = 0
    d = 1
    sign = 1
    while d_sum <= n:
        d_sum += sign * d
        d += 1
        sign *= -1
    
    print("a) Tổng a:", a_sum)
    print("b) Tổng b:", b_sum)
    print("c) Tổng c:", c_sum)
    print("d) Tổng d:", d_sum)

if __name__ == "__main__":
    main()