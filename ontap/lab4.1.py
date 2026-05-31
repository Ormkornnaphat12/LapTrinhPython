import math

# a) Số thân thiện
thanThien = lambda n: math.gcd(n, int(str(n)[::-1])) == 1
print("=== SO THAN THIEN ===")
for i in range(1, 1000):
    if thanThien(i):
        print(i, end=" ")
print()

# b) Số chính phương
chinhPhuong = lambda n: int(math.sqrt(n)) ** 2 == n
print("\n=== SO CHINH PHUONG ===")
for i in range(1, 1000):
    if chinhPhuong(i):
        print(i, end=" ")
print()

# c) Số đồng nhất
dongNhat = lambda n: all(x == str(n)[0] for x in str(n))
print("\n=== SO DONG NHAT ===")
for i in range(1, 1000):
    if dongNhat(i):
        print(i, end=" ")
print()

# d) Số hoàn thiện
hoanThien = lambda n: sum(i for i in range(1, n) if n % i == 0) == n
print("\n=== SO HOAN THIEN ===")
for i in range(1, 1000):
    if hoanThien(i):
        print(i, end=" ")
print()

# e) Số phong phú
phongPhu = lambda n: sum(i for i in range(1, n) if n % i == 0) > n
print("\n=== SO PHONG PHU ===")
for i in range(1, 1000):
    if phongPhu(i):
        print(i, end=" ")
print()

# f) Số tăng dần
tangDan = lambda n: all(str(n)[i] <= str(n)[i+1] for i in range(len(str(n)) - 1))
print("\n=== SO TANG DAN ===")
for i in range(1, 1000):
    if tangDan(i):
        print(i, end=" ")
print()