##Cho 1 dict gồm các giá trị số nguyên, xóa item có value là số chẵn

thisdict = {
    "so1": 1,
    "so2": 2,
    "so3": 3,
    "so4": 4,
}
thisdict2 = thisdict.copy()

for x in thisdict:
    if thisdict.get(x) % 2 ==0:
        thisdict2.pop(x)

print(thisdict2)





