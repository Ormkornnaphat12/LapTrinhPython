import math
def bangCuuChuong(a,b):
    start = min(a,b)
    end = max(a,b)
    for i in range(start, end+1):
        print("Bang Cuu Chuong", i,":")
        for j in range(1, 11):     #day so chay tu 1 den 10 va thuc thi
            print(i, "X", j, "=", i*j)
n = input("Nhap Vao  a Va b (a,b cach nhau boi dau phay) = ")
a, b = map(int,n.replace(' ','').split(','))
bangCuuChuong(a, b)

def soNT(n):  # Ham kiem tra so nguyen to
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def lkSNT(n):
    for i in range(2, n):  # chay tu 2 den n-1
        if soNT(i):
            print(i, end=" ")
n = int(input("Nhap Vao So Nguyen n = "))
lkSNT(n)

def uocSNT(n):
    print("Cac Uoc So Cua", n ,"Vua La So Nguyen To : ", end="")
    for i in range(2, n+1):
        if n%i==0 and soNT(i):
            print(i, end=" ")
    print()
n = int(input("\nNhap vao so nguyen duong n = "))
uocSNT(n)





