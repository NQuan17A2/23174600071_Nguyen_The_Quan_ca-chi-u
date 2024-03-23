chieu_cao = float(input("Nhập chiều cao (m): "))
can_nang = float(input("Nhập cân nặng (kg): ")) 

bmi=can_nang / (chieu_cao**2)

if bmi < 18.5:
    phan_loai = "Gầy"
elif 18.5 <= bmi < 25.0:
    phan_loai = "Bình thường"
elif 25.0 <= bmi < 30.0:
    phan_loai = "Hơi béo"
else:
    phan_loai = "Béo"

# In kết quả chỉ số BMI và phân loại BMI
print("Chỉ số BMI của bạn:", bmi)
print("Phân loại BMI:", phan_loai)