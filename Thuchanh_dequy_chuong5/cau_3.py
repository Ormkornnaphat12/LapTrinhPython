print('--- Viet ham nhan 2 tham so la 2 so nguyen duong a, b. Tinh a^b ---')
def luy_thua(a,b):
    if b==0 :
        return 1
    return a*luy_thua(a,b-1)
nhapa = input('Nhap co so a = ')
a = int(nhapa)
nhapb = input('Nhap so mu b =')
b = int(nhapb)
print(f"{a}^{b} = ",luy_thua(a,b))