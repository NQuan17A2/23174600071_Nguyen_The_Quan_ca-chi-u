#A
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def print_primes():
    num = 2
    print("Các số nguyên tố nhỏ hơn 100 là:")
    while num < 100:
        if is_prime(num):
            print(num, end=" ")
        num += 1

print_primes()


#B
def print_square_numbers():
    num = 1
    print("Các số chính phương nhỏ hơn 100 là:")
    while num**2 < 100:
        print(num**2, end=" ")
        num += 1

print_square_numbers()


#C
def print_fibonacci():
    a, b = 0, 1
    print("Các số Fibonacci nhỏ hơn 1000 là:")
    while a < 1000:
        print(a, end=" ")
        a, b = b, a + b

print_fibonacci()