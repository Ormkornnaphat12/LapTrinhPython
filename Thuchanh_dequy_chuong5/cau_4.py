print('--- Viet ham nhan 2 tham so la 2 so nguyen duong a, b. Tim uoc so chung lon nhat (greatest common divisor -gcd cua a va b) ---')
def gcd(a,b):
    if b==0:
        return a
    return gcd(b, a%b)
nhap_a = input('Nhap vao a: ')
a = int(nhap_a)
nhap_b = input('Nhap vao b: ')
b = int(nhap_b)
print(f"Uoc so chung lon nhta cua {a} va {b} la: ",gcd(a,b))