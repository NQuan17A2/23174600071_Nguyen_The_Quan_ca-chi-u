a,b,c=map(int,input("Nhập vào 3 số nguyên bất kì: ").split(","))

if a>b and a>c:
    if b>c:
        so_lon_thu_hai=b
    else:
        so_lon_thu_hai=c
elif b>a and b>c:
    if a>c:
        so_lon_thu_hai=a
    else:
        so_lon_thu_hai=c
else:
    if b>a:
        so_lon_thu_hai=b
    else:
        so_lon_thu_hai=a
print("Số lớn thứ hai trong các số đó là:",so_lon_thu_hai)
