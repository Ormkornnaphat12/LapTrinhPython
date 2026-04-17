n = int(input("Nhap so nguyen duong n = "))
Chan=0
Le=0
while n>0:
     digit=n%10
     if digit%2==0:
        Chan+=1
     else:
         Le+=1
print("So luong so chan: ",Chan)
print("So luong So le: ",Le)
