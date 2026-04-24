print('--- Viet ham giai thua (factorial number) cua mot so nguen duong n ---')
def factorial_number (n):
    if n==0 or n==1:
        return 1
    return n*factorial_number(n-1)
nhap_fn = input('Nhap n = ')
n = int(nhap_fn)
print(f"{n}! = ",factorial_number(n))