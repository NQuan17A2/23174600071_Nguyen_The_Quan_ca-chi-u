def generate_fibonacci(n):
    # Tạo danh sách Fibonacci sử dụng list comprehension
    fibonacci = [0, 1] + [fibonacci[i-1] + fibonacci[i-2] for i in range(2, n)]
    return fibonacci

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime_numbers():
    # Tạo danh sách số nguyên tố nhỏ hơn 100 sử dụng list comprehension
    primes = [num for num in range(2, 100) if is_prime(num)]
    return primes

def main():
    # Nhập số Fibonacci muốn tạo
    n = int(input("Nhập số Fibonacci muốn tạo: "))
    
    # Tạo và in ra danh sách Fibonacci
    fibonacci_list = generate_fibonacci(n)
    print(f"Danh sách Fibonacci gồm {n} số đầu tiên là:")
    print(fibonacci_list)

    # Tạo và in ra danh sách số nguyên tố nhỏ hơn 100
    prime_list = generate_prime_numbers()
    print("\nDanh sách các số nguyên tố nhỏ hơn 100 là:")
    print(prime_list)

if __name__ == "__main__":
    main()