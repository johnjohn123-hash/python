## Nhập vào 1 chuỗi, nhiệm vụ là kiểm tra xem mọi nguyên âm có xuất hiện hay không.
## Nguyên âm là các âm là 'a', 'e','i'.'o', 'u' hoặc 'A', 'E', 'I', 'O', 'U'
set_nguyen_am_viet_thuong = {'a', 'e','i', 'o', 'u'}
set_nguyen_am_viet_hoa = {'A', 'E', 'I', 'O', 'U'}

chuoi_nhap_input= input("Nhap chuoi vao day")
set_input = set(chuoi_nhap_input)
if set_input.difference(set_nguyen_am_viet_hoa) == set_nguyen_am_viet_hoa:
    print('Accepted')
elif set_input.difference(set_nguyen_am_viet_thuong) == set_nguyen_am_viet_thuong:
    print('Accepted')
elif set_input.difference(set_nguyen_am_viet_hoa) != (set_nguyen_am_viet_hoa):
    print(f"All vowels except {set_nguyen_am_viet_hoa.difference(set_input)} are not present")