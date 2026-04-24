print('--- g) Nhan 1 doi so la so nguyen cua n. Cho biet n co phai la so chinh phuong  hay ko ---')
La_SCP = lambda n : str(n)+' LA SO CHINH PHUONG' if n>=0 and(n**0.5).is_integer() else str(n)+ ' KHONG PHAI LA SO CHINH PHUONG'
p = input('Nhap vao so nguyen n: ')
kt_scp = int(p)
print('n la : ', La_SCP(kt_scp))