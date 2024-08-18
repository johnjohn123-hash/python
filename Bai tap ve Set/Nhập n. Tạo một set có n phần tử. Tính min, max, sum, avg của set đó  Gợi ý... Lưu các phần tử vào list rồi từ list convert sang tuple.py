## Nhập n. Tạo một set có n phần tử. Tính min, max, sum, avg của set đó
## Gợi ý... Lưu các phần tử vào list rồi từ list convert sang tuple
n = int(input("Nhap so n vao day: "))
newlist = []
for x in range(n):
    newlist.append(int(input(f"Nhập số thứ {x + 1}:")))

newset = set(newlist)

print(newset)

mynewlist = list(newset)

print(min(mynewlist))
print(max(mynewlist))
print(sum(mynewlist))
print(sum(mynewlist)/len(mynewlist))