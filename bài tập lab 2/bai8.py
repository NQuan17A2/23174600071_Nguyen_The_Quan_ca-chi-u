hsg1 = float(input("Nhập hệ số góc của đường thẳng thứ nhất: "))
hstd1 = float(input("Nhập hệ số tự do của đường thẳng thứ nhất: "))
hsg2 = float(input("Nhập hệ số góc của đường thẳng thứ hai: "))
hstd2 = float(input("Nhập hệ số tự do của đường thẳng thứ hai: "))
if hsg1 == hsg2:
    print("Hai đường thẳng là đường thẳng song song.")
elif hsg1 * hsg2 == -1:
    print("Hai đường thẳng là đường thẳng vuông góc.")
else:
    print("Hai đường thẳng cắt nhau.")