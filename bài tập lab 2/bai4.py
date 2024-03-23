n=float(input("Nhập vào điểm số của bài kiểm tra: "))
if 0 < n <= 5:
    print("Điểm kém")
elif 5 < n <= 7:
    print("Điểm trung bình")
elif 7 < n <= 8.5:
    print("Điểm khá")
else:
    print("Điểm tốt")