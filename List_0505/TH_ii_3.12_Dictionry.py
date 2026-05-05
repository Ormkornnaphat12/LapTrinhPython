from collections import Counter
S1 = input("Nhap chuoi S1: ")
S2 = input("Nhap chuoi S2: ")
counter_S1 = Counter(S1)
counter_S2 = Counter(S2)
c = counter_S1 & counter_S2
print("Cac ky tu xuat hien trong ca 2 chuoi S1 va S2:")
print(list(c.keys()))
dict_S1 = dict(counter_S1)
dict_S2 = dict(counter_S2)
dict_S1_not_in_S2 = [char for char in dict_S1 if char not in dict_S2]
dict_S2_not_in_S1 = [char for char in dict_S2 if char not in dict_S1]
print("Cac ky tu xuat hien trong S1 nhung khong xuat hien trong S2:")
print(dict_S1_not_in_S2)
print("Cac ky tu xuat hien trong S2 nhung khong xuat hien trong S1:")
print(dict_S2_not_in_S1)
Count_diff = len(dict_S1_not_in_S2) + len(dict_S2_not_in_S1)
print(f"So luong ky tu xuat hien trong S1 nhung khong xuat hien trong S2 va nguoc lai: {Count_diff}")