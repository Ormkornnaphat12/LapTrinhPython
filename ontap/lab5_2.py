#Cho nhap chieu dai, chieu rong va chieu cao cua khoi hinh chu nhat(cm). Tinh va xuat ket qua 
# theo ket qua theo vd sau voi cach in dien tich va the tich theo hai cach
# -- Nhap chieu dai day hinh khoi chu nhat (cm): >? 2.134. ---=7.38cm^2
# -- Nhap chieu rong day hinh khoi chu nhat (cm): >?3.4567 ---=30.24cm^3
#-- Nhap chieu cao hinh khoi chu nhat (cm):>4.1
dai = float(input("Nhap Chieu Dai Day Hinh Khoi Chu Nhat(cm) = "))
rong = float(input("Nhap Chieu Rong Day Hinh Khoi Chu Nhat(cm) = "))
cao = float(input("Nhap Chieu Cao Hinh Khoi Chu Nhat(cm) = "))
so_le = int(input("So Luong So Le Can Hien Thi = "))
dien_ich_day = dai*rong
the_tich = dai*rong*cao
print(f"Cach 1: Dien Tich Day Hinh Chu Nhat ={dien_ich_day:.{so_le}f} cm\u00b2 " )
print(f"cach 1: The Tich Hinh Khoi = {the_tich:.{so_le}f} cm\u00b3 ")

print(f"cach 2: Dien Tich Day Hinh Chu Nhat = {format(dien_ich_day, f'.{so_le}f')} cm\u00b2")
print(f"cach 2: The Tich Hinh Khoi = {format(the_tich, f'.{so_le}f')} cm\u00b3")