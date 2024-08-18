## Nhập n. Tạo set gồm n số nguyên nhập từ bàn phím.
## Xóa từng phần tử trong set đó

n = int(input("Nhap so n vao day: "))
newlist = []
for x in range(n):
    newlist.append(int(input(f"Nhập số thứ {x + 1}:")))

newset = set(newlist)

while newset:
    e = newset.pop()
    print(newset)