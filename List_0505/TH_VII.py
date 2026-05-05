#Buoi 5
import math
LaSNT = lambda n: n > 1 and all(n % i for i in range(2, int(math.sqrt(n)) + 1))
nb = [ ]
while True:
    try:
        vl = int(input("Nhap so nguyen duong: "))
        nb.append(vl)
    except ValueError:
        print("Vui long nhap so nguyen duong!")
        continue
    choice = input("Ban co muon tiep tuc nhap khong? (y/n): ")
    if choice.lower() != 'y':
        break
if not nb:
    print("Ban chua nhap so nao!")
else:
    print("\n" + "="*40)
    print(f"Danh sach vua nhap: {nb}")
    print("-" * 40) 
    print("Cac so nguyen to trong danh sach la:")
snt = list(filter(LaSNT, nb))
print("a) So nguyen to:",snt)
so_duong = list(filter(lambda x: x > 0, nb))
so_am = list(filter(lambda x: x < 0, nb))
TbD_post = sum(so_duong) / len(so_duong) if so_duong else 0
TbA_post = sum(so_am) / len(so_am) if so_am else 0
print(f"b.1) Trung binh cong cua cac so nguyen to duong: {TbD_post:.2f}")
print(f"b.2) Trung binh cong cua cac so nguyen to am: {TbA_post:.2f}" )
print("c) So lon:", max(nb))
print("So nho:", min(nb))
Kt_tangdan = lambda lst: all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
if Kt_tangdan(nb):
    print("d) Danh sach tang dan")
else:    
    print("d) Danh sach khong tang dan")   


    