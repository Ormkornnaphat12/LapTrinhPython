#to chuc va xay dung cac ham so cho tat ca cac bai thuc hanh sau:
#1) cho nhap 2 nguyen a, b tren cung 1 dong (cach nhau boi dau phay-','). In ra cac bang cuu chuong tu a den b (khi a<b) hoac tu b den a (khi b<a)
import math
def Bang_cuu_chuong(a, b):
    start = min(a, b)
    end = max(a, b)
    for i in range(start, end+1):
        print("Bang cuu chuong", i,":")
        for j in range(1,11):
            print(i, "x",j, "=", i*j)
n = input("Nhap vao so nguyen a va b (cach nhau boi dau phay) = ")
a,b = map(int,n.split(','))
Bang_cuu_chuong(a, b)

#2) cho nhap so nguyen duogn n. Kiem tra xem n co phai la so nguyen to hay khong
def soNT(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
    

def KiemTraSNT(n): 
    if soNT(n):
        print(n,"La So Nguyen To")
    else:
        print(n,"KHONG PHAI LA SO NGUYEN TO!")
n = int(input("Nhap vao so nguyen n = "))
KiemTraSNT(n)
        
# 3) Cho nhap so nguyen duong n. Liet ke cac so nguyen to < n
def LkSNT(n):
    for i in range(n):
        if soNT(i):
            print(i, end=" ")
n = int(input("Nhap vao so nguyen n = "))
LkSNT(n)
# 4) Cho nhap so nguyen duong n. Dem cac so nguyen to < n
def DemSNT(n):
    count = 0
    for i in range (2,n):
        if soNT(i):
            count+=1
    return count
n = int(input("\nNhap vao so nguyen n = "))
count = DemSNT(n)
print ("So luong so nguyen to cua", n ," = ", count)


# 5) Cho nhap vao so nguyen duong n, liet ke cac uoc so cua n la so nguyen to.
#vd: nhap n=36. Cac uoc so cua 36 gom: 1,2,3,4,6,9,12,18
#Nhung chi in ra : cac so vua la uoc so cua 36, vua la so nguyen to: 2,3
def lk_uocso(n):
    print("Cac uoc so cua", n ,"vua la so nguyen to : ", end="")
    for i in range(2, n+1):
        if n%i==0 and soNT(i):
            print(i, end=" ")
    print()
n = int(input("Nhap vao so nguyen duong n = "))
lk_uocso(n)


