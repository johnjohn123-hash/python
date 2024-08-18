## Cho hai list trùng lặp với nhau ngoại trừ một phần tử, tức là thiếu một phần tử của một trong
## các list, tìm phần tử còn thiếu đó.

A = [1, 4, 5, 7, 9]
B = [4, 5, 7, 9]

seta = set(A)
setb = set(B)

phan_tu_thieu = seta.difference(setb)

print(phan_tu_thieu)
