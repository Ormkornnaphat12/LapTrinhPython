import math
#Viet chuong trinh python su dung lambda de tinh cho cac truong hop sau:
# 1) Ham nhan 1 doi so la  so nguyen n va tra ve tri tuyet doi cua n.
abs_value = lambda n : n if n >= 0 else -n 
n = int(input("Nhap vao so nguyen n = "))
print ("|",n,"|", abs_value(n))
# 2) Ham nhan 1 doi so la so nguyen n va tra ve gia tri cua n+15
add_15 = lambda n: n+15
n = int(input("Nhap vao so nguyen n = "))
print (n, "+ 15 = ",add_15(n)) 
# 3) Ham nhan 2 doi so la so nguyen (x,y) tra ve tich cua x, y
tich_xy = lambda x, y: x*y
x = int(input("Nhap Vao X = "))
y = int(input("Nhap Vao Y = "))
print(x, "X", y, "=", tich_xy)
# 4) Ham nhan 1 doi so la so nguyen n. Cho biet n co phai la boi so cua 13 hoac 19 khong ?
boiso = lambda n: n%13 == 0 or n%19==0
n = int(input("Nhap vao so nguyen n = "))
if boiso(n):
    print(n, "La Boi So Cua 13 Hoac 19 ")
else:
    print(n, "KHONG LA BOI SO CUA 13 HOAC 19 !!!")
print()
# 5) Ham nhan 1 doi so la so thuc r la ban kinh cua hinh tron. Cho biet dien tich hinh tron   
hinh_tron = lambda r: math.pi*r**2
r = float(input("Nhap Vao Ban Kinh Hinh Tron r = "))
print(f"Dien Tich Hinh Tron = {hinh_tron(n):.2f}")
# 6) Ham nhan 2 doi so la so thuc d, r la chieu dai va chieu rong cua hinh chu nhat. Cho biet chu vi hinh chu nhat 
chu_vi = lambda d,r: 2*(d+r)
dai = float(input("Nhap Chieu Dai Cua Hinh Chu Nhat =  "))
rong = float(input("Nhap Vao Chieu Rong Cua HInh Chu Nhat = "))
print("Chu Vi Hinh Chu Nhat = ",chu_vi(dai, rong))
# 7) Ham nhan 1 doi so la so nguyen n. Cho biet n co la so chinh phuong hay khong? (So chinh phuong la so can bac hai la 1 so nguyen nhu: 4, 9, 16,..)
so_chinhphuong = lambda n: int(math.sqrt(n))**2==n if n>=0 else False
n = int(input("Nhap Vao So Nguyen n = "))
if so_chinhphuong(n):
    print(n, " La So Chinh Phuong")
else:
    print(n," KHONG LA SO CHINH PHUONG !!!")
print()
# 8) Ham nhan 1 doi so la so nguyen cua n. Cho biet n co phai la so nguyen to hay khong?
soNT = lambda n: False if n<2 else all(n%i!=0 for i in range(2, int(math.sqrt(n))+1))
n = int(input("Nhap Vao So Nguyen n = "))
if soNT(n):
    print(n, " La So Nguyen To ")
else:
    print(n," KHONG LA SO NGUYEN TO !!!")
print()
# 9) Ham nhan 3 tham so la so nguyen (a, b, c). Cho biet a, b, c co la 3 canh hop le cua 1 tam giac hay khong? Neu 3 canh hop le cua tam giac, cho bik do la tam giac gi?(thuong, can, deu, vuong,..)
def tam_giac(a, b, c):
    sx = sorted([a, b, c])
    a, b, c = sx[0], sx[1], sx[2]
    if a+b<=c:
        return "KHONG PHAI 3 CANH TAM GIAC !!!"
    if a==b==c:
        return "Tam Giac Deu "
    elif a==b or b==c or a==c:
        if abs(a**2 + b**2 - c**2) < 1e-9:
            return "Tam Giac Vuong Can "
        return "Tam Giac Can "
    elif abs(a**2 + b**2 - c**2) < 1e-9:
        return "Tam Gic Vuong "
    else:
        return "Tam Giac Thuong "
a = float(input("Nhap canh a = "))
b = float(input("Nhap canh b = "))
c = float(input("Nhap canh c = "))
print(tam_giac(a, b, c))