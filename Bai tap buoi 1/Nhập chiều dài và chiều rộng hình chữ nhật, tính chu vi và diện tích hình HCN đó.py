## Nhập chiều dài và chiều rộng hình chữ nhật, tính chu vi và diện tích hình HCN đó


chieu_dai = int(input("Nhap chieu dai hinh chu nhat vao day: "))

while chieu_dai <=0:
    chieu_dai = int(input("Nhap lai chieu dai voi gia tri lon hon 0: "))


chieu_rong = int(input("Nhap chieu rong hinh chu nhat vao day: "))

while chieu_rong <= 0:
    chieu_rong = int(input("Nhap lai chieu rong voi gia tri lon hon 0: "))

print(f"Chu vi hinh chu nhat la: {((chieu_dai) + (chieu_rong))*2}")
print(f"Dien tich hinh chu nhat la: {(chieu_dai)*(chieu_rong)}")