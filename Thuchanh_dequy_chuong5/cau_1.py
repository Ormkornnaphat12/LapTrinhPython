print('--- Cho nhap so nguyen n. Tinh tong cac chu so co trong n ---')
def Tong_chu_so (n):
    if n==0:
      return 0
    return (n%10) + Tong_chu_so(n//10)
nhap = input('Nhap vao so nguyen duogn n: ')
n=int(nhap)
print(f"Tong cac chu so cua {n} la:{Tong_chu_so(n)} ")