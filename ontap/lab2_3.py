# ==================== BÀI 117: TỔNG BÌNH PHƯƠNG CÁC SỐ CON ====================
"""
Số con: một dãy chữ số liền nhau của n
"""

def tong_binh_phuong_subnumber(n):
    """
    Tính tổng bình phương tất cả các số con của n
    """
    s = str(n)
    length = len(s)
    total = 0
    subnumbers = []  
    
    # Duyệt tất cả các subnumber
    for i in range(length):
        for j in range(i + 1, length + 1):
            sub = int(s[i:j])
            subnumbers.append(sub)
            total += sub ** 2
    
    return total, subnumbers
n = int(input("Nhập số nguyên dương n = "))

if n <= 0:
    print("Vui lòng nhập số nguyên dương (n > 0)")
else:
    tong, cac_so_con = tong_binh_phuong_subnumber(n)
    
    # In chi tiết
    print(f"\nVới n = {n}")
    print("Các số con:", cac_so_con)
    print(f"Tổng bình phương các số con S = {tong}")