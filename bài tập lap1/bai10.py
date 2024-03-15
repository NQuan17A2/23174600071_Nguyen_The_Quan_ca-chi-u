def giaithua(n):             #tạo hàm giai thừa 
 list1=[n]
 a=n
 for i in range (n): 
        a=a-1
        if a==0:
                break
        list1.append(a)
 tich=1
 for i in list1:
      tich=tich*i
 return float(tich)

 
sobi=int (input("nhập số bi muốn rút ra :    "))
khong_gian_mau_ckn= (giaithua(50)/(giaithua(50-sobi)))     #tính không gian mẫu theo công thức tổng quát 
#1 tính xs rút đc all bi đỏ 
if sobi<=20: 
 tat_ca_bi_mau_do=(giaithua(20)/(giaithua(20-sobi)))           
 xs_all_red=tat_ca_bi_mau_do/khong_gian_mau_ckn
 print ("xác suất rút đc tất cả bi đều là màu đỏ là :",xs_all_red)
else :
    print("số lượng bi đỏ chỉ có tối đa 20")

#2 tính xs rút đc ít nhất 1 bi xanh 
tat_ca_bi_khong_phai_mau_xanh=(giaithua(35)/(giaithua(35-sobi)))    #ít nhất 1 bi xanh tương đương phần bù của không có viên bi xanh nào 
xs_no_blue=tat_ca_bi_khong_phai_mau_xanh/khong_gian_mau_ckn
xs_it_nhat_1_vien_mau_xanh=1-xs_no_blue
print ("xác suất để rút đc ít nhất một bi màu xanh là: ",xs_it_nhat_1_vien_mau_xanh)
#3 tính xs rút đc đúng 2 bi vàng 
xs_rut_1_bi_vang=((giaithua(15)/(giaithua(15-1)))/(giaithua(50)/(giaithua(50-1))))    
xs_rut_dc_dung_2bivang=xs_rut_1_bi_vang*xs_rut_1_bi_vang                 #áp dungj quy tắc nhân xs 
print ("xác suất rút đc đúng 2 bi vàng là:",xs_rut_dc_dung_2bivang)