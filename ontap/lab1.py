# ==================== BÀI 14: ĐỔI TIỀN VỚI SỐ TỜ ÍT NHẤT ====================
#co 9 loai tien 1, 2, 5, 10, 20, 50, 100, 200, 500. Cho nhap so tien x.Chuyen so x ra cac loai tien sao cho so luong la it nhat. In ra so to tien cua moi loai, tong so to tien cua tat ca cac loai.
menh_gia = [500, 200, 100, 50, 20, 10, 5, 2, 1]
X = int(input("Nhập số tiền cần đổi X = "))
so_tien_goc = X
so_to = {}
for mg in menh_gia:
    so_to[mg] = X // mg  
    X = X % mg          
print(f"\nSo tien {so_tien_goc} duoc doi thanh:")
tong_so_to = 0
for mg in menh_gia:
    print(f"Loai {mg} gom {so_to[mg]} to")
    tong_so_to += so_to[mg]
print(f"TONG CONG CO {tong_so_to} TO")