## Nhập độ dài cạnh và góc alpha tạo bởi 2 cạnh của hình thoit, tính chu vi và diện tích hình thoiđó

from math import sqrt
import math

canh_hinh_thoi = int(input("Nhap chieu dai canh hinh thoi vao day: "))
while canh_hinh_thoi < 0:
    canh_hinh_thoi = canh_hinh_thoi * (-1)
while canh_hinh_thoi == 0:
    canh_hinh_thoi = int(input("Nhap lai chieu dai canh hinh thoi voi gia tri lon hon 0: "))

goc_alpha = int(input("Nhap goc alpha vao day:"))
while goc_alpha < 0:
    goc_alpha = goc_alpha * (-1)
goc_alpha = math.radians(goc_alpha)

duong_cheo_1 = 2 * (sqrt(canh_hinh_thoi**2 - 2*(canh_hinh_thoi**2)*math.cos(goc_alpha)))
duong_cheo_2 = 2 * canh_hinh_thoi * math.sin((goc_alpha)/2)

print(f"Chu vi hinh thoi la: {canh_hinh_thoi * 4}")
print(f"Dien tich hinh thoi la: {(duong_cheo_2 * duong_cheo_1) / 2}")

