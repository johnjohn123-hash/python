##  Viết hàm liệt kê số lẻ trong list
def my_fuction(thislist):

    newlist = thislist.copy()

    for x in thislist:
        if x % 2 == 0:
            newlist.remove(x)

    return newlist

print(my_fuction([1, 3, 3, 4, 5, 6, 7, 8, 9, 10]))








