import math
def tamGiac(a,b,c):
    sx = sorted([a, b, c]) #sap xep canh
    a, b, c = sx[0], sx[1], sx[2]
    if a+b<=c:  #kiem tra bat dang thuc tam giac
        return "KHONG PHAI LA 3 CANH CUA TAM GIAC !!!"
    if a==b==c:
        return "Tam Giac Deu."
    tgVuong = abs(a**2 + b**2 - c**2) <1e-9  #dinh ly pytago
    tgCan = (a==b) or (b==c) or (c==a)
    if tgVuong and tgCan: # 
        return "Tam Giac Vuong Can."
    elif tgVuong:
        return "Tam Giac Vuong."
    elif tgCan:
        return "Tam Giac Can."
    else:
        return "Tam Giac Thuong."
a = float(input("Nhap Canh a = "))
b = float(input("Nhap Canh b = "))
c = float(input("Nhap Canh c = "))
print(tamGiac(a, b, c))