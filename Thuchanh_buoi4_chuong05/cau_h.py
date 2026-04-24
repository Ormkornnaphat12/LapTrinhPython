print('--- h) Nhan 1 doi so la so nguyen cua n. Cho biet n co phai la so nguyen to hay ko ---')
La_SNT = lambda n : str(n) + ' LA SO NGUYEN TO' if n>1 and all(n%i!=0 for i in range(2, int(n**0.5)+1)) else str(n)+' KHONG LA SO NGUYEN TO'
Nhap_nt = input('Nhap vao so nguyen n: ')
test = int(Nhap_nt)
print('n la: ',La_SNT(test))