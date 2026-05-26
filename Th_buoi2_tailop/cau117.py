import math

while True:
    try:
        n = input("Nhap vao so nguyen duong n = ").strip()
        val = int(n)
        if val > 0:
            tong = 0
            do_dai = len(n)
            ds_con = []
            for i in range(do_dai):
                for j in range(i + 1, do_dai + 1):
                    sub_str = n[i:j]
                    sub_num = int(sub_str)
                    ds_con.append(sub_num)
                    tong += sub_num ** 2  
            print(f"Cac so con tim duoc tu n: {ds_con}")
            print(f"Tong binh phuong S = {tong}")
            break
        else:
            print("VUI LONG NHAP SO NGUYEN LON HON 0. NHAP LAI !!!!!")
    except ValueError:
        print("ERROR!")

