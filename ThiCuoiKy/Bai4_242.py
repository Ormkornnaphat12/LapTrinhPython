import math 
dongNhat = lambda n: all(x == str(n)[0] for x in str(n)) # ham kiem tra cac chu so giong nhau
print("=== SO DONG NHAT ===")
for i in range(1, 1000):
    if dongNhat(i):
        print(i, end=" ")
print()
hoanThien = lambda n: sum(i for i in range(1, n) if n%i==0) ==n  #tong cac uoc so thuc tru chinh no bang chinh no
print("=== SO HOAN THIEN ===")
for i in range(1, 1000): # tao day so tu 1 den 999, thuc thi tu 1 den 99
    if hoanThien(i):
        print(i, end=" ")
print()