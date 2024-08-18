## Tính bình phương của các phần tử chia 4 dư 3 trong list  [-10, 4, 47, 53, 3, 132, 423, 123, 55, 12, 100, 101, 23, 54, 49, 17, 23]

thislist = [-10, 4, 47, 53, 3, 132, 423, 123, 55, 12, 100, 101, 23, 54, 49, 17, 23]
newlist = []

for x in thislist:
    if x % 4 == 3:
        newlist.append(x)

print(newlist)


for x in newlist:
    binh_phuong = x**2
    print(binh_phuong)

