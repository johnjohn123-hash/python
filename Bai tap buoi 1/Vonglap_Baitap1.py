## Tìm các số chia hết cho 3 trong khoảng từ a đến b
## Nhập các số a, b và in ra kết quả cách nhau bằng một dấu cách

so_thu_nhat = int(input("Nhap so thu nhat vao day"))
so_thu_hai = int(input("Nhap so thu hai vao day"))

if so_thu_nhat > so_thu_hai:
    so_thu_nhat, so_thu_hai = so_thu_hai, so_thu_nhat

so_thu_nhat = so_thu_nhat +  (3 - so_thu_nhat%3)

for i in range (so_thu_nhat, so_thu_hai + 1, 3):
    if i % 3 == 0:
        print(i,end=" ")

