n = int(input("Nhap vao so nguyen: "))
Tong=0
Tich=1
while n>0:
    digit=n%10
    Tong+=digit
    Tich*=digit
    n//=10
print("Tong =",Tong)
print("Tich = ",Tich)