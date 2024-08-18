## Cho hai danh sách, tìm giá trị còn thiếu và giá trị bổ sung trong cả hai danh sách.
## (giá trị còn thiếu là giá trị không có ở list hiện tại mà có ở list còn lại, giá trị bổ sung thì ngược lại)

list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]

set1 = set(list1)
set2 = set(list2)

missing_value_in_list_1 = set2.difference(set1)
print(missing_value_in_list_1)

additional_values_in_list_1 = set1.difference(set2)
print(additional_values_in_list_1)

missing_value_in_list_2 = set1.difference(set2)
print(missing_value_in_list_2)

additional_values_in_list_2 = set2.difference(set1)
print(additional_values_in_list_2)

##Output : Missing values in list1 = [8, 7]
##Additional values in list1 = [1, 2, 3]
##Missing values in list2 = [1, 2, 3]
##Additional values in list2 = [7, 8]