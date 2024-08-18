##Nhập vào a, b, c, d. Tìm nghiệm của pt ax^2 + bx + c = d

from math import sqrt
a = int(input("Nhap so thu nhat vao day: "))
while a == 0:
    a = int(input("Nhap lai so thu nhat voi gia tri khac 0: "))
b = int(input("Nhap so thu hai vao day: "))
c = int(input("Nhap so thu ba vao day: "))
d = int(input("Nhap so thu tu vao day: "))

c -= d

delta = b**2 - 4*a*c
if delta < 0:
    print("Phuong trinh vo nghiem")
elif delta == 0:
    print(f"Phuong trinh co nghiem kep la: {-b/2*a}")
else:
    print(f"Phuong trinh co hai nghiem phan biet la: x1 = {(-b + sqrt(delta))/2*a} va x2 la: {(-b - sqrt(delta))/2*a}")



