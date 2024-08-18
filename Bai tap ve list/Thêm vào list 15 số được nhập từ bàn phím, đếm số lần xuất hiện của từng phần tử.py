newlist = []

# Nhập 15 số từ bàn phím
for x in range(15):
    newlist.append(int(input(f"Nhập số thứ {x + 1}:")))

# Tạo một từ điển để đếm số lần xuất hiện
count_dict = {}

for num in newlist:
    if num in count_dict:
        count_dict[num]+=1
    else:
        count_dict[num]=1


for num, count in count_dict.items():
    print(f"Số {num} xuất hiện {count} lần")
