## Thêm vào list 15 số được nhập từ bàn phím, thay đổi giá trị của các vị trí lẻ thành 0

newlist = []

# Nhập 15 số từ bàn phím
for x in range(15):
    newlist.append(int(input(f"Nhập số thứ {x + 1}:")))

for i in range(1, 15, 2):
    newlist[i] = 0



print(newlist)