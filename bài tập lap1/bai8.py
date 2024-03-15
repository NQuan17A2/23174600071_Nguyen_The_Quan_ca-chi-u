import math
x,z=map(float,input('nhập hai giá trị thực x,z:  ').split(','))
fxz=((x**2)*(math.sin(z))+(abs(x)**0.5))/(math.log(z)+math.e**(x-1))
print ("giá trị của hàm số f(x,z) là {}".format(round(fxz,2)))