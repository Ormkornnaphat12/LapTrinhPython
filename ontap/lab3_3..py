def generate_strobogrammatic(n, n_goc, pairs):
    if n == 0:
        return ['']
    if n == 1:
        return [p[0] for p in pairs if p[0] == p[1]]
    prev_list = generate_strobogrammatic(n - 2, n_goc, pairs)
    result = [] 
    for num in prev_list:
        for pair in pairs:
            if n == n_goc and pair[0] == '0':
                continue
            result.append(pair[0] + num + pair[1])
    return result
n = int(input("Enter the length of strobogrammatic numbers to generate (2 to 10): "))
if 2 <= n <= 10:
    pairs_base = [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]
    pairs_extend = [('0', '0'), ('1', '1'), ('2', '2'), ('5', '5'), ('6', '9'), ('8', '8'), ('9', '6')]
    strobo_base = generate_strobogrammatic(n, n, pairs_base)
    result_a = sorted([int(num) for num in strobo_base])
    strobo_extend = generate_strobogrammatic(n, n, pairs_extend)
    result_b = sorted([int(num) for num in strobo_extend])
    print("\n" + "="*50)
    print(f"RESULT: n = {n} CHỮ SỐ:")
    print("-" * 50)
    print(f"a.- Số lượng số strobogrammatic cơ bản: {len(result_a)}")
    print(f"    Danh sach cu the: {result_a if len(result_a) <= 20 else str(result_a[:15]) + '...'}") 
    print("-" * 50)
    print(f"b.- So luong so Strobogrammatic : {len(result_b)}")
    print(f"Danh sach cu the: {result_b if len(result_b) <= 20 else str(result_b[:15]) + '...'}")
    print("="*50)
else:
    print("VUI LONG NHAP LAI SO NGUYEN TU 2 DEN 10!")