dai = float(input("Nhap Chieu Dai Day Hinh Khoi Chu Nhat (cm) = "))
rong = float(input("Nhap Chieu Rong Day Hinh Khoi Hinh Chu Nhat (cm) = "))
cao = float(input("Nhap Chieu Cao Hinh Khoi Hinh Chu Nhat (cm) = "))
soLe = int(input("So Luong So Le Can Hien Thi = "))
dtDay = dai*rong
theTich = dai*rong*cao
print(f"Dien Tich Day Hinh Chu Nhat = {dtDay:.{soLe}f} cm\u00b2") #cm^2
print(f"The Tich Hinh Khoi = {theTich:.{soLe}f}cm\u00b3") #cm^3
