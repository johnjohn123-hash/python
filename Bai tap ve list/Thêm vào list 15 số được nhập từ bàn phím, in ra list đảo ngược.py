newlist = []

# Nhập 15 số từ bàn phím
for x in range(15):
    newlist.append(int(input(f"Nhập số thứ {x + 1}:")))

newlist.reverse()
print(newlist)