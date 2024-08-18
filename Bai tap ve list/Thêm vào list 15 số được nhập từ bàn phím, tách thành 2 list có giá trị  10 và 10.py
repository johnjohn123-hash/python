##Thêm vào list 15 số được nhập từ bàn phím, tách thành 2 list có giá trị > 10 và <= 10

newlist_1 = []
list_nhohon10 =[]
list_lonhon10 = []

for x in range(15):
    newlist_1.append(int(input(f"Nhập số thứ {x + 1}:")))

for x in newlist_1:
    if x > 10:
        list_lonhon10.append(x)
    else:
        list_nhohon10.append(x)

print(list_lonhon10)
print(list_nhohon10)


