n = input("Nhap so nguyen duong n: ")
Somayman = True
for numbers in n:
    if Somayman != '6' and Somayman != '8':
        Somayman = False
        break
if Somayman:
        print(f"{n} la so may man")
else:
        print(f"{n} khong phai so may man !")