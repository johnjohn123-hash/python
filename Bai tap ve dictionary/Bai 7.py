##  Nhập vào 1 key, xóa items chứa key đó

thisdict = {
    "so1": 1,
    "so2": 2,
    "so3": 3,
    "so4": 4,
}

giatri = input("Nhap gia tri vao day")


if giatri in thisdict.keys():
    thisdict.pop(giatri)
else:
    print("Nhap sai gia tri roi")

print(thisdict)