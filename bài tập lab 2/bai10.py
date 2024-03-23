print("Các thể loại phim:")
print("1. Hành động")
print("2. Kinh dị")
print("3. Tình cảm")
print("4. Hài hước")
print("5. Hoạt hình")

the_loai = input("Nhập số tương ứng với thể loại phim bạn muốn xem: ")
thoi_gian = input("Nhập thời gian muốn xem (sáng, trưa, chiều, tối): ")

if the_loai == "1":
    if thoi_gian == "tối":
        print("Phim Hành động sẽ chiếu vào buổi tối")
    else:
        print("Không có suất chiếu")
elif the_loai == "2":
    if thoi_gian == "tối":
        print("Phim Kinh dị sẽ chiếu vào buổi tối")
    else:
        print("Không có suất chiếu")
elif the_loai == "3":
    if thoi_gian == "tối":
        print("Phim Tình cảm sẽ chiếu vào buổi tối")
    else:
        print("Không có suất chiếu")
elif the_loai == "4":
    if thoi_gian == "sáng" or thoi_gian == "trưa" or thoi_gian == "chiều" or thoi_gian == "tối":
        print("Phim Hài hước sẽ chiếu vào buổi",thoi_gian)
    else:
        print("Không có suất chiếu")
elif the_loai == "5":
    if thoi_gian == "sáng" or thoi_gian == "trưa":
        print("Phim Hoạt hình sẽ chiếu vào buổi",thoi_gian)
    else:
        print("Không có suất chiếu")
else:
    print("Lựa chọn không hợp lệ")