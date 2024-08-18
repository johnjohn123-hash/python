## Nhập vào 1 chuỗi, kiểm tra xem chuỗi có phải là chuỗi nhị phân hay không
##(Chuỗi nhị phân là chuỗi chỉ gồm 0 và 1.
##Dùng set cho string đó và kiểm tra xem chỉ còn đúng 0 với 1 hay k)

my_string= input("Nhap chuoi vao day")
myset = set(my_string)
chuoi_nhi_phan = {' ', '1', '0'}

if myset == chuoi_nhi_phan:
    print("TRUE")
else:
    print("FALSE")

