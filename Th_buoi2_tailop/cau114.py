import math
so_than_thien = lambda n:  math.gcd(n, int(str(n)[::-1])) == 1
while True:
    try:
        a = int(input("Nhap vao so nguyen (a >= 10)  a = ")) 
        b = int(input("Nhap vao so nguyen (b >= a) b = "))
        if 10 <= a <= b <= 30000:
            ds = [i for i in range (a, b + 1 ) if so_than_thien(i)]
            print(f"Cac so than thien trong khoang {a} -  {b} = ")
            print(ds)
            print(f"Total: {len(ds)}")
            break
        else:
            print("VUI LONG NHAP LAI ! CHI NHAN SO NGUYEN TRONG KHOANG QUY DINH !!!!")
    except ValueError:
        print("Error!")

    

 