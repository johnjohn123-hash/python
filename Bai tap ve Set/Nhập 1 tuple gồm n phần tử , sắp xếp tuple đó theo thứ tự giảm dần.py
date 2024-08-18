## Nhập 1 tuple gồm n phần tử , sắp xếp tuple đó theo thứ tự giảm dần

n = int(input("Nhap so n vao day: "))
newlist = []
for x in range(n):
    newlist.append(int(input(f"Nhập số thứ {x + 1}:")))
    newlist.sort(reverse=True)

new_tuple = tuple(newlist)

print(new_tuple)




