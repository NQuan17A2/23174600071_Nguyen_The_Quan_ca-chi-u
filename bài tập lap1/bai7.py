'''
a1x+b1y=c1
a2x+b2y=c2
'''
a1,b1,c1=map(float,input("nhập lần lượt hệ số của phươgn trình dạng a1,b1,c1:   ").split(','))
a2,b2,c2=map(float,input("nhập lần lượt hệ số của phươgn trình dạng a2,b2,c2:   ").split(','))
he_so_nhan=a2/a1 
a1_=a1*he_so_nhan
b1_=b1*he_so_nhan
c1_=c1*he_so_nhan
y=(c2-c1_)/(b2-b1_)
x=(c1-b1*y)/a1
print ("vậy nghiệm của hệ phương trình trên là: x={},y={}".format(round(x,2),round(y,2)))
