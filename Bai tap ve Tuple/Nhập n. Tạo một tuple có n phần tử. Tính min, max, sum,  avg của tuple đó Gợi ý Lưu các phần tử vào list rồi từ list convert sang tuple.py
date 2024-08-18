## Nhập n. Tạo một tuple có n phần tử. Tính min, max, sum,  avg của tuple đó
##(Gợi ý: Lưu các phần tử vào list rồi từ list convert sang tuple)
n = int(input("Nhap so n vao day: "))
newlist = []
for x in range(n):
    newlist.append(int(input(f"Nhập số thứ {x + 1}:")))

newtuple = tuple(newlist)

print(newtuple)

mynewlist = list(newtuple)
print(mynewlist)

print(min(mynewlist))
print(max(mynewlist))
print(sum(mynewlist))
print(sum(mynewlist)/len(mynewlist))