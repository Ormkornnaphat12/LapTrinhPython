def change_money(x):
    price = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    x = int(input("Nhap vao so tien x = "))
    total = 0
    type_of_money = 0
    print(f"So tien {x} co the doi thanh : ")
    for money in price:
        if x >= money:
            count = x // money
            x = x % money
            if count > 0:
                print(f"Loai {money} gom {count} to")
                total += count
                type_of_money += 1
    print(f"Co tong cong {total} to tien")
    print(f"Co tong cong {type_of_money} loai to tien")
def pay():
    a = int(input("Nhap vao so tien khach phai tra a = "))
    b = int(input("Nhap vao so tien khach thuc te tra b = "))
    if a > b:
        print("So tien khach hang con thieu la : ",a-b)
    elif a == b:
        print("CAM ON KHACH HANG. HEN GAP LAI !")
    else:
        tien_thua = b - a
        print("Tien thua cua khach hang la : ",tien_thua)
        change_money(tien_thua)
        print("Nhan phim ENTER de ket thuc....!")
        print("CAM ON KHACH HANG. HEN GAP LAI !")
pay()
