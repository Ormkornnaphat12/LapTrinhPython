
menh_gia = [500, 200, 100, 50, 20, 10, 5, 2, 1]
def doi_tien(X):
    """
    Hàm đổi số tiền X thành các loại tiền với số tờ ít nhất
    Trả về: tuple (so_to_dict, tong_so_to, so_loai)
    """
    so_to = {}
    so_tien_con_lai = X   
    for mg in menh_gia:
        so_to[mg] = so_tien_con_lai // mg
        so_tien_con_lai = so_tien_con_lai % mg
    tong_so_to = 0
    so_loai = 0   
    for mg in menh_gia:
        if so_to[mg] > 0:
            tong_so_to += so_to[mg]
            so_loai += 1  
    return so_to, tong_so_to, so_loai
def in_ket_qua(so_tien, so_to, tong_so_to, so_loai):
    """
    Hàm in kết quả đổi tiền (chỉ in các loại có số tờ > 0)
    """
    print(f"\nSo tien {so_tien} duoc doi thanh:")   
    for mg in menh_gia:
        if so_to[mg] > 0: 
            print(f"Loai {mg} gom {so_to[mg]} to") 
    print(f"TONG CONG CO {tong_so_to} TO")
    print(f"Tong so loai = {so_loai}")
print("=== PHẦN 1: ĐỔI TIỀN (CHỈ IN LOẠI CÓ TỜ > 0) ===\n")
X = int(input("Nhập số tiền cần đổi X = "))
so_to, tong_so_to, so_loai = doi_tien(X)
in_ket_qua(X, so_to, tong_so_to, so_loai)
print("\n" + "="*60)
print("=== PHẦN 2: TRẢ TIỀN THỪA KHI KHÁCH HÀNG TRẢ NHIỀU HƠN ===\n")
a = int(input("Nhập số tiền hàng cần phải trả (a) = "))
b = int(input("Nhập số tiền khách hàng thực tế trả (b) = "))
if a > b:
    thieu = a - b
    print(f"\nSố tiền khách hàng còn thiếu là {thieu}")
elif a == b:
    print("\nCám ơn khách hàng. Hẹn gặp lại")
else: 
    tien_thua = b - a
    print(f"\nSố tiền cần thối lại cho khách hàng: {tien_thua}")
    so_to_thoi, tong_so_to_thoi, so_loai_thoi = doi_tien(tien_thua)
    print("\n=== NHÂN VIÊN THU NGÂN CẦN THỐI LẠI CHO KHÁCH HÀNG ===")
    in_ket_qua(tien_thua, so_to_thoi, tong_so_to_thoi, so_loai_thoi)
    input("\nNhấn Enter để kết thúc...")
    print("\nCám ơn khách hàng. Hẹn gặp lại")