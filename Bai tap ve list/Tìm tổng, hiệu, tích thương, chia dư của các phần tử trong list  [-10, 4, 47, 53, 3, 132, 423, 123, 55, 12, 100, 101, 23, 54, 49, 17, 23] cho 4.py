## Tìm tổng, hiệu, tích thương, chia dư của các phần tử trong list [-10, 4, 47, 53, 3, 132, 423, 123, 55, 12, 100, 101, 23, 54, 49, 17, 23] cho 4

thislist = [-10, 4, 47, 53, 3, 132, 423, 123, 55, 12, 100, 101, 23, 54, 49, 17, 23]


# Cong voi 4
list_cong_voi_4 = []
for x in thislist:
    cong_voi_4 = x + 4
    list_cong_voi_4.append(cong_voi_4)
print(list_cong_voi_4)

## Tru cho 4
list_tru_voi_4 = []
for x in thislist:
    tru_voi_4 = x - 4
    list_tru_voi_4.append(tru_voi_4)
print(list_tru_voi_4)

## Nhan cho 4
list_nhan_voi_4 = []
for x in thislist:
    nhan_voi_4 = x * 4
    list_nhan_voi_4.append(nhan_voi_4)
print(list_nhan_voi_4)

## Nhan cho 4
list_chia_voi_4 = []
for x in thislist:
    chia_voi_4 = x % 4
    list_chia_voi_4.append(chia_voi_4)
print(list_chia_voi_4)



