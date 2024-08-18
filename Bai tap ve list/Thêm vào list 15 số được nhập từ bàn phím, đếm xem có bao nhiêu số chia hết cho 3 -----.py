## Thêm vào list 15 số được nhập từ bàn phím, đếm xem có bao nhiêu số chia hết cho 3 -----

newlist = []
newlist2 = []

# Nhập 15 số từ bàn phím
for x in range(15):
    newlist.append(int(input(f"Nhập số thứ {x + 1}:")))

for x in newlist:
    if x % 3 == 0:
        newlist2.append(x)

print(f"Co tong cong la {len(newlist2)} so chia het cho 3")
