## Cho 2 list, liệt kê giá trị có ở list thứ 1 mà không có ở list thứ 2

list1 = [10, 15, 20, 25, 30, 35, 40]
list2 = [25, 40, 35]

set1 = set(list1)

set2 = set(list2)

ket_qua = set1.difference(set2)
ket_qua_list = list(ket_qua)
print(ket_qua_list)