import math
hsg_dt = float(input("Nhập hệ số góc của đường thẳng: "))
hstd_dt = float(input("Nhập hệ số tự do của đường thẳng: "))

x,y = map(float,input("Nhập tọa độ x,ycủa tâm đường tròn: ").split(","))
bk = float(input("Nhập bán kính của đường tròn: "))

kc = abs(hstd_dt-y)/math.sqrt(1+hsg_dt**2)

if kc < bk:
    print("Đường thẳng cắt đường tròn.")
elif kc == bk:
    print("Đường thẳng tiếp xúc đường tròn.")
else:
    print("Đường thẳng nằm ngoài đường tròn.")