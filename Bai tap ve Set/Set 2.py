## Tìm giao của 3 arr, nhập vào số k và kiểm tra k có trong giao của 3 tập hợp k
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

a1 = set(ar1)
diemchung = a1.intersection(ar2,ar3)
print(diemchung)

so_k = int(input("Nhap so k vao day:"))
print(so_k in diemchung)


















