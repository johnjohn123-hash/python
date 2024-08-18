## Thêm vào list 15 số được nhập từ bàn phím, đếm xem có bao nhiêu số lẻ trong list đó
newlist = []
my_list = []
for i in range(5):
    ##ChatGPT
    number = int(input(f"Nhập số thứ {i + 1}:"))
    my_list.append(number)
    ###ChatGPT



print("List sau khi nhập:", my_list)

for x in my_list:
    if x % 2 != 0:
        newlist.append(x)

print(f"So luong so le co trong list ban dau la: {(len(newlist))}")