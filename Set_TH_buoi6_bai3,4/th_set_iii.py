#su dung tap hop viet chuong trinh cho nhap so dien thoai
# vd S="0913158020"
def so_thieu(s):
    all_numbers = set('0123456789')
    number_on_S = set(s)
    Result = all_numbers - number_on_S
    return sorted(list(Result))
S = input("Nhap so dien thoai: ")
print("Cac so thieu:",so_thieu(S))

