so_gio_su_dung=float (input("nhập số giờ sử dụng máy lọc nước:   "))
so_kwh= so_gio_su_dung*220*1.5
so_tien_phai_tra=so_kwh*5000
print('số tiền phải trả cho {} giờ sử dụng máy lọc nước là {}'.format(so_gio_su_dung,so_tien_phai_tra))