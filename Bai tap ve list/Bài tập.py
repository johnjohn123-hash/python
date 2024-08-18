##Dùng for để tạo một cái list có giá trị từ 0 đến 20. Loại bỏ các số lẻ trong đó
thislist = [x for x in range(21)]

# for i in range(21):
#     thislist.append(i)
print(thislist)

for x in thislist:
    if x % 2 == 1:
        thislist.remove(x)

print(thislist)