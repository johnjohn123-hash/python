## Nhập chiều dài hình vuông, tính chu vi và diện tích hình vuông đó

from math import sqrt
chieu_dai_canh = int(input("Nhap chieu dai canh hinh vuong vao day: "))

while chieu_dai_canh <= 0:
    chieu_dai_canh = int(input("Nhap lai chieu dai canh hinh vuong voi gia tri lon hon 0: "))

print(f"Chu vi hinh vuong la: {(chieu_dai_canh)*4}")
print(f"Dien tich hinh vuong la: {(chieu_dai_canh)**(chieu_dai_canh)}")