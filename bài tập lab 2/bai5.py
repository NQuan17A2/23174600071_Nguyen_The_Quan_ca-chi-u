so_lg=int(input("Nhập vào số lượng người mua vé xem phim: "))
if so_lg == 1:
    tong_tien=12000
    print("Tổng số tiên phải trả là:",tong_tien,"đồng")
elif 2 <= so_lg <= 4:
    tong_tien=(so_lg*12000)*(1-(5/100))
    print("Tổng số tiên phải trả là:",tong_tien,"đồng")
elif 4 < so_lg <= 10:
    tong_tien=(so_lg*12000)*(1-(10/100))
    print("Tổng số tiên phải trả là:",tong_tien,"đồng")
else:
    tong_tien=(so_lg*12000)*(1-(20/100))
    print("Tổng số tiên phải trả là:",tong_tien,"đồng")
