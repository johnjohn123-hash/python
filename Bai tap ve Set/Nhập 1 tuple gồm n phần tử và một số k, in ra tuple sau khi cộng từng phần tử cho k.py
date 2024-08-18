n = int(input("Nhap so n vao day: "))
k = int(input("Nhap so k vao day: "))
newlist = []
ket_qua_list = []
for x in range(n):
    newlist.append(int(input(f"Nhập số thứ {x + 1}:")))

for x in newlist:
    ket_qua = x + k
    ket_qua_list.append(ket_qua)


newtuple = tuple(ket_qua_list)

print(newtuple)