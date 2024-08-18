## Thêm vào list 15 số được nhập từ bàn phím, in ra danh sách từ vị trí thứ 2 đến vị trí thứ 9

newlist = []

# Nhập 15 số từ bàn phím
for x in range(15):
    newlist.append(int(input(f"Nhập số thứ {x + 1}:")))

for x in range(1,10):
    print (newlist[x])



