##Nhập 10 số vào list1, 5 số vào list2. Thêm list2 vào vị trí thứ 7 trong list1

newlist_1 = []

for x in range(10):
    newlist_1.append(int(input(f"Nhập số thứ {x + 1}:")))

newlist_2 = []

for x in range(5):
    newlist_2.append(int(input(f"Nhập số thứ {x + 1}:")))

newlist_1.insert(6, newlist_2)

print(newlist_1)


