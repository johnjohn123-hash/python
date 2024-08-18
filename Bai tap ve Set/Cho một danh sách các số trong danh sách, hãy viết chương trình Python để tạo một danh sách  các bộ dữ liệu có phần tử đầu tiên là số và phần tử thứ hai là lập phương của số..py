##Cho một danh sách các số trong danh sách, hãy viết chương trình Python để tạo một danh sách
##các bộ dữ liệu có phần tử đầu tiên là số và phần tử thứ hai là lập phương của số.

list= [2, 3, 4, 5, 6, 7]
ketqua_o_dang_list = []

for x in list:
    lap_phuong = x ** 3
    tuple = (x, lap_phuong)
    ketqua_o_dang_list.append(tuple)

print(ketqua_o_dang_list)




