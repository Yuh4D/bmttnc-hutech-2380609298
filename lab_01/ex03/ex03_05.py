def dem_so_lan_xuat_hien(lst):
    count_dick = {}
    for item in lst:
        if item in count_dick:
            count_dick[item] += 1
        else:
            count_dick[item] = 1
        return count_dick

input_string = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
word_list = input_string.split()
so_lan_xuat_hien = dem_so_lan_xuat_hien(word_list)
print("Số lần xuất hiện của các phần tử: ", so_lan_xuat_hien)
