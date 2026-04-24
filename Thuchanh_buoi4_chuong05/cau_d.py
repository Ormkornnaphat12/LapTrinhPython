print('--- d) Nhan 1 doi so la so nguyen cua n.Cho biet n co la boi so cua 13 hoac 19 hay khong ---')
BoiSo = lambda b : str(b)+ ' la boi so' if b%13==0 or b%19==0 else str(b) + ' khong la boi so'
nhap_so = input('Nhap vao so nguyen: ')
kiemtra = int(nhap_so)
print(BoiSo(kiemtra))
