
"""
Số strobogrammatic: số có giá trị không đổi khi xoay 180 độ
Các chữ số hợp lệ: 0, 1, 6, 8, 9
- 0 -> 0
- 1 -> 1
- 6 -> 9
- 8 -> 8
- 9 -> 6
"""

def is_strobogrammatic(n):
    """
    Kiểm tra xem số n có phải là số strobogrammatic hay không
    """

    s = str(n)
    
   
    mapping = {
        '0': '0',
        '1': '1',
        '6': '9',
        '8': '8',
        '9': '6'
    }
    left = 0
    right = len(s) - 1
    
    while left <= right:
        if s[left] not in mapping or s[right] not in mapping:
            return False
        if mapping[s[left]] != s[right]:
            return False
        left += 1
        right -= 1
    return True
def is_strobogrammatic_v2(n):
    """
    Kiểm tra số strobogrammatic bằng cách tạo số đảo ngược và thay thế
    """
    s = str(n)
    mapping = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
    rotated = ''.join(mapping.get(ch, '') for ch in reversed(s))
    if len(rotated) != len(s):
        return False
    return rotated == s
def generate_strobogrammatic(length):
    """
    Sinh tất cả các số strobogrammatic có độ dài cho trước
    """
    def helper(n, length):
        if n == 0:
            return [""]
        if n == 1:
            return ["0", "1", "8"]
        middle = helper(n - 2, length)
        result = []
        for m in middle:
            if n != length: 
                result.append("0" + m + "0")
            result.append("1" + m + "1")
            result.append("6" + m + "9")
            result.append("8" + m + "8")
            result.append("9" + m + "6")
        return result
    return helper(length, length)
def list_strobogrammatic(limit=None):
    """
    Liệt kê các số strobogrammatic
    limit: giới hạn số lớn nhất (nếu None thì liệt kê độ dài 1-6)
    """
    results = []
    if limit:
        n = 0
        while True:
            if is_strobogrammatic(n):
                results.append(n)
            n += 1
            if n > limit:
                break
    else:
        for length in range(1, 7):  
            nums = generate_strobogrammatic(length)
            for num_str in nums:
                if num_str == "0" or not num_str.startswith('0'):
                    results.append(int(num_str))
            results.sort()
    return results
if __name__ == "__main__":
    print("=== SỐ STROBOGRAMMATIC ===\n")
    print("--- PHẦN 1: KIỂM TRA SỐ ---")
    test_numbers = [0, 1, 8, 11, 69, 88, 96, 101, 916, 68910, 1001, 1961]   
    for num in test_numbers:
        if is_strobogrammatic(num):
            print(f"{num}: Là số strobogrammatic")
        else:
            print(f"{num}: KHÔNG là số strobogrammatic")
    print("\n--- PHẦN 2: LIỆT KÊ SỐ STROBOGRAMMATIC (đến 10000) ---")
    strobos = list_strobogrammatic(limit=10000)
    print("Các số strobogrammatic ≤ 10000:")
    print(strobos)
    print(f"\nSố lượng: {len(strobos)}")
    print("\n--- PHẦN 3: SINH THEO ĐỘ DÀI ---")
    for length in range(1, 5):
        nums = generate_strobogrammatic(length)
        filtered = [int(num) for num in nums if num == "0" or not num.startswith('0')]
        print(f"Số strobogrammatic có {length} chữ số: {sorted(filtered)}")