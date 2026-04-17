n = int(input("Nhap vao so nguyen duong: "))
Max=0
while n>0:
      digit=n%10
      if digit > Max:
        Max = digit
      n//=10
print("So Lon Nhat: ", Max)