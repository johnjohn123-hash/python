## Nhập vào a, b, c. Tìm nghiệm của pt ax  + b = c

##Nếu a ≠ 0, phương trình có thể được giải theo công thức x = (c - b) / a, do đó nó có một nghiệm duy nhất.
##Nếu a = 0 và b = c, thì mọi giá trị của x đều thỏa mãn phương trình, nghĩa là phương trình có vô số nghiệm.
##Nếu a = 0 và b ≠ c, thì không có giá trị nào của x thỏa mãn phương trình, nghĩa là phương trình vô nghiệm.

from math import sqrt

a = int(input("Nhap so thu nhat vao day: "))
b = int(input("Nhap so thu hai vao day: "))
c = int(input("Nhap so thu ba vao day: "))

if a != 0:
    print(f"Phuong trinh co nghiem la: {(c - b) / a}")
elif a == 0 and b == c:
    print("Phuong trinh co vo so nghiem")
elif a == 0 and b != c:
    print("Phuong trinh vo nghiem")