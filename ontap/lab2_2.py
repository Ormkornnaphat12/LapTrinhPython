import math

"""
Số thân thiện: số n và số đảo ngược của n có ước chung lớn nhất = 1
"""

def is_friendly(n):
    """
    Kiểm tra số n có phải là số thân thiện hay không
    """
    if n <= 0:
        return False
    reversed_n = int(str(n)[::-1])
    return math.gcd(n, reversed_n) == 1
a = int(input("Nhập a (10 ≤ a): "))
b = int(input("Nhập b (b ≤ 30000): "))

if a < 10 or b > 30000 or a > b:
    print("Vui lòng nhập a, b thỏa mãn: 10 ≤ a ≤ b ≤ 30000")
else:
    friendly_numbers = []
    for num in range(a, b + 1):
        if is_friendly(num):
            friendly_numbers.append(num)
    
    # In kết quả
    print(f"\nCác số thân thiện từ {a} đến {b}:")
    print(friendly_numbers)
    print(f"\nSố lượng số thân thiện: {len(friendly_numbers)}")