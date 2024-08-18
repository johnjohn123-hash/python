##Nhập độ dài 3 cạnh của tam giác, kiểm tra đó có phải tam giác vuông, tam giác cân, tam giác đều không
##Tính diện tích và chu vi của tam giác đó

from math import sqrt

chieu_dai_canh_1 = int(input("Nhap chieu dai canh 1 vao day: "))
while chieu_dai_canh_1 < 0:
    chieu_dai_canh_1 = (chieu_dai_canh_1) * (-1)

chieu_dai_canh_2 = int(input("Nhap chieu dai canh 2 vao day: "))
while chieu_dai_canh_2 < 0:
    chieu_dai_canh_2 = (chieu_dai_canh_2) * (-1)

chieu_dai_canh_3 = int(input("Nhap chieu dai canh 3 vao day: "))
while chieu_dai_canh_3 < 0:
    chieu_dai_canh_3 = (chieu_dai_canh_3) * (-1)

nua_chu_vi = ((chieu_dai_canh_1 + chieu_dai_canh_2 + chieu_dai_canh_3) / 2)
print(nua_chu_vi)

if chieu_dai_canh_1 == chieu_dai_canh_2 == chieu_dai_canh_3:
    print("Day la tam giac deu")
elif chieu_dai_canh_1 == chieu_dai_canh_2 or chieu_dai_canh_1 == chieu_dai_canh_3 or chieu_dai_canh_2 == chieu_dai_canh_3:
    print("Day la tam giac can")
elif chieu_dai_canh_1 ** 2 + chieu_dai_canh_2 ** 2 == chieu_dai_canh_3 ** 2 or chieu_dai_canh_1 ** 2 + chieu_dai_canh_3 ** 2 == chieu_dai_canh_2 ** 2 or chieu_dai_canh_2 ** 2 + chieu_dai_canh_3 ** 2 == chieu_dai_canh_1 ** 2:
    print("Day la tam giac vuong")
else:
    print("Day la tam giac thuong")

print(f"Chu vi cua tam giac la: {chieu_dai_canh_1 + chieu_dai_canh_2 + chieu_dai_canh_3}")
x = nua_chu_vi * (nua_chu_vi - chieu_dai_canh_1) * (nua_chu_vi - chieu_dai_canh_2) * (nua_chu_vi - chieu_dai_canh_3)
print(f"Dien tich cua tam giac la: {sqrt(x)}")
