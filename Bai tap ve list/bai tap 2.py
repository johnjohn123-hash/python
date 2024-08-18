##Dùng for để tạo một cái list có giá trị từ 0 đến 20. Tao hai list, mot list chua so chan va mot list chi chua so le
list_toan_so_chan = []
list_toan_so_le = []

thislist = [x for x in range (21)]

for x in thislist:
    if x % 2 == 1:
        list_toan_so_le.append(x)
    else:
        list_toan_so_chan.append(x)

print(list_toan_so_chan)
print(list_toan_so_le)

##Tim so lon nhat, be nhat va tong cua cac so trong day so, trung binh cua list toan so chan

print(max(list_toan_so_chan))
print(min(list_toan_so_chan))
print(sum(list_toan_so_chan))
print(len(list_toan_so_chan))

print(f"Trung binh cong cua day so toan so chan la { sum(list_toan_so_chan) // len(list_toan_so_chan) }")