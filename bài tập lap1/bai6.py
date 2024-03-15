#vecto1=[a1,a2]
#vecto2=[b1,b2]
a1,a2=map(float,input("nhập tọa độ của a (nhập a1,a2):  ").split(","))
b1,b2=map(float,input("nhập tọa độ của b (nhập b1,b2):  ").split(",") )
tvh=a1*b1+a2*b2
print ("vecto a+b là ({},{}) \n vecto a-b là b({},{}) ".format(a1+b1,a2+b2,a1-b1,a2-b2))
print ('độ dài vecto a là {}, độ dài vecto b là {}'.format(((a1**2)+(a2**2))**0.5,((b1**2)+(b2**2))**0.5))
print ("sin góc xen giữa của hai vecto bằng {}".format(  tvh/((((a1**2)+(a2**2))**0.5)*(((b1**2)+(b2**2))**0.5))))
