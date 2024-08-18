## Thêm vào list 6 số được nhập từ bàn phím, xóa hết số lẻ và sắp xếp dãy thu được theo thứ tự giảm dần
newlist = []

for x in range(6):
    newlist.append(int(input(f"Nhập số thứ {x + 1}:")))

newlist_1 = newlist.copy()
for x in newlist:
    if x % 2 != 0:
        newlist_1.remove(x)
        print(x % 2)
newlist_1.sort()
print(newlist_1[::-1])

