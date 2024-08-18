##Nhập vào 2 tuple cùng kích thước, tính số dư của tuple thứ 1 cho tuple thứ 2

tuple_1 = (10, 4, 5, 6)
tuple_2 = (5, 6, 7, 5)
ket_qua = []


for x in range (4):
    ket_qua.append(tuple_1 [x] % tuple_2 [x])
    a =tuple(ket_qua)

print(a)