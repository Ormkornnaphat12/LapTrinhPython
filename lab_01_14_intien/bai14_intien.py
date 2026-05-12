def change_money():    
    price = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    x = int(input("Nhap vao so tien x = "))
    total = 0
    print(f"So tien {x} co the doi thanh : ")
    for money in price:
        if x >= money:
            count = x // money
            x = x % money
        else:
            count = 0
        print(f"Loai {money} gom {count} to")
        total += count
    print(f"Co tong cong {total} to tien")
change_money()