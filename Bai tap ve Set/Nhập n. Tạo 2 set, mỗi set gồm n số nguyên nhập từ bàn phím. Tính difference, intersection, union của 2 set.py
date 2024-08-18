##Nhập n. Tạo 2 set, mỗi set gồm n số nguyên nhập từ bàn phím.
##Tính difference, intersection, union của 2 set

a = [1,2,3,4,5]
b = [5,6,4,8,9]

a1= set(a)

diemchung =a1.intersection(b)
print(diemchung)

print (len(diemchung) >0)

n = int(input("Nhap so n vao day cho set 1: "))
newlist1 = []
for x in range(n):
    newlist1.append(int(input(f"Nhập số thứ {x + 1}:")))

newset1 = set(newlist1)

n = int(input("Nhap so n vao day cho set 2: "))
newlist2 = []
for x in range(n):
    newlist2.append(int(input(f"Nhập số thứ {x + 1}:")))

newset2 = set(newlist2)

su_khac_biet = newset1.difference(newset2)
tong_hop_phan_tu = newset1.union(newset2)
diem_chung= newset1.intersection(newset2)

print(su_khac_biet)
print(tong_hop_phan_tu)
print(diem_chung)







