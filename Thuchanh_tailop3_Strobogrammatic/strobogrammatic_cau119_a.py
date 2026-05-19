import math
def laSNT(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if  n % 2 == 0 or n % 3 == 0:
        return False
    for i in range (5, int(math.sqrt(n)) +1, 6) :
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True 
#def Strobogrammatic(s, map):
    #if n == 0:
     #   return [""]
    #elif n == 1:
     #   return ["0", "1", "8"]
    #else:
        #result = list()
       # middles = list(Strobogrammatic (n-2))
      #  for middle in middles:
     #       result.append("1" +middles+ "1")
    #        result.append("6" +middles+ "9")
   #         result.append("8" +middles+ "8")
  #          result.append("9" +middles+ "6")
 #       return result
#print(Strobogrammatic(3))
def check_dictionary (n, strobogrammatic_map):
    s = str(n)
    left, right = 0, len(s) - 1
    while left <= right:
        if s[left] not in strobogrammatic_map or strobogrammatic_map[s[left]] != s[right]:
            return False
        left += 1
        right -= 1
    return True
def Strobogrammatic(s, strobogrammatic_map):
    s = str(s)
    r = []
    for char in reversed(s):
        if char not in strobogrammatic_map:
            return None
        r.append(strobogrammatic_map[char])
    return "".join(r)
map_base = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
#is_strobo_base = lambda n: (s := str(n)) == Strobogrammatic(s, map_base)
map_extend = {'0':'0', '1':'1', '2':'2', '5':'5', '6':'9', '8':'8', '9':'6'}
#is_strobo_extend = lambda n: (s := str(n)) == Strobogrammatic(s, map_extend)
cau_a, cau_b, cau_c, cau_d, cau_e = [], [], [], [], []
print("Dang tinh toan du lieu tu 0 den 1.000.000. Vui long cho...")
for ns in range(1000000):
    check_prime = laSNT(ns)
    check_strobo = check_dictionary(ns, map_base)     #is_strobo_base(ns)
    check_extend = check_dictionary(ns, map_extend)  #is_strobo_extend(ns)
    if check_strobo:
        cau_a.append(ns)
        if check_prime:
            cau_b.append(ns)
    if check_extend:
        cau_c.append(ns)
        if check_prime:
            cau_d.append(ns)
    if not check_strobo and not check_prime:
        rotated_str = Strobogrammatic(str(ns), map_base)
        if rotated_str is not None:
            if laSNT(int(rotated_str)):
                cau_e.append(ns)

print("\n" + "="*50)
print(f"a.- So luong so strobogrammatic nho hon 1 trieu: {len(cau_a)}")

print(f"\nb.- Cac so nguyen to strobogrammatic nho hon 1 trieu:\n{cau_b}")

print(f"\nc.- So luong so strobogrammatic mo rong nho hon 1 trieu: {len(cau_c)}")

print(f"\nd.- Cac so nguyen to strobogrammatic mo rong nho hon 1 trieu:\n{cau_d}")

print(f"\ne.- So luong so thoa man cau (e): {len(cau_e)}")
print(f"    Goi y thu xem 10 so dau tien cua cau e: {cau_e[:10]}")
print("="*50)


