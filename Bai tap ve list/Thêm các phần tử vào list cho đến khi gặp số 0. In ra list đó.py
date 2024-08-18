## Thêm phần tử vào list cho đến khi gặp số 0. In ra list đó

newlist = []

while True:
    number = int(input(f"Nhập số: "))
    if number == 0:
        break
    newlist.append(number)

print(newlist)