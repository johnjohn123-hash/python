## Thêm vào list 15 số được nhập từ bàn phím, xóa các phần tử tại vị trí lẻ
newlist = []

# Nhập 15 số từ bàn phím
for x in range(15):
    newlist.append(int(input(f"Nhập số thứ {x + 1}:")))

my_list = newlist[1::2]

# In danh sách sau khi xóa
print("Danh sách sau khi xóa các phần tử ở vị trí lẻ:")
print(my_list)


