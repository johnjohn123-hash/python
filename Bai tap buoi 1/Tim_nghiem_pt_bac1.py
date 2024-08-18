##Nhập vào hai số a và b. Tìm nghiệm của phương trình ax+b=

a = int(input("Nhap so thu nhat vao day: "))
while a == 0:
    a = int(input("Nhap lai so thu nhat vao day: "))
b = int(input("Nhap so thu hai vao day: "))

if a == 0:
    print("Nhap so a sai vi khong chia cho 0 duoc")
else:
    print(f"Nghiem cua phuong trinh la: {-b / a}")



